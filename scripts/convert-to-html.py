#!/usr/bin/env python3
"""Convert wiki markdown files to HTML with sidebar, breadcrumbs, pagination."""

import re
import yaml
import html
import json
from pathlib import Path
from collections import defaultdict

WIKI_ROOT = Path(__file__).parent.parent
CONCEPTS_DIR = WIKI_ROOT / "concepts"
SOURCES_DIR = WIKI_ROOT / "sources"
SYNTHESES_DIR = WIKI_ROOT / "syntheses"
STYLES_DIR = WIKI_ROOT / "styles"
SCRIPTS_DIR = WIKI_ROOT / "scripts/js"
META_DIR = WIKI_ROOT / "meta"

SLUG_MAP = {}

CATEGORY_MAP = {
    'data-engineering': 'Data Engineering',
    'dbt': 'Data Engineering', 'analytics': 'Data Engineering', 'elt': 'Data Engineering',
    'data-modeling': 'Data Engineering', 'etl': 'Data Engineering', 'streaming': 'Data Engineering',
    'data-lake': 'Data Engineering', 'lakehouse': 'Data Engineering', 'data-governance': 'Data Engineering',
    'clickhouse': 'Data Engineering', 'orchestration': 'Data Engineering',
    'data-layout': 'Data Engineering', 'delta-lake': 'Data Engineering',
    'file-formats': 'Data Engineering', 'columnar': 'Data Engineering', 'table-formats': 'Data Engineering',
    'in-memory': 'Data Engineering', 'duckdb': 'Data Engineering', 'dataframes': 'Data Engineering',
    'query-engines': 'Data Engineering', 'ingestion': 'Data Engineering', 'apache': 'Data Engineering',
    'metrics': 'Data Engineering', 'dataops': 'Data Engineering', 'sql': 'Data Engineering',
    'roles': 'Data Engineering', 'database-architecture': 'Data Engineering',
    'design-principles': 'Software Design',
    'clean-code': 'Software Design', 'oop': 'Software Design', 'solid': 'Software Design',
    'design-patterns': 'Software Design', 'error-handling': 'Software Design',
    'reliability': 'Software Design', 'maintainability': 'Software Design',
    'engineering': 'Software Design', 'optimization': 'Software Design',
    'complexity': 'Software Design', 'encapsulation': 'Software Design',
    'testing': 'Testing', 'tdd': 'Testing', 'pytest': 'Testing', 'strategy': 'Testing',
    'system-design': 'System Architecture', 'architecture': 'System Architecture',
    'distributed-systems': 'System Architecture', 'scalability': 'System Architecture',
    'go': 'Go & Web', 'golang': 'Go & Web', 'http': 'Go & Web', 'middleware': 'Go & Web',
    'web': 'Go & Web', 'kubernetes': 'Go & Web', 'cloud-native': 'Go & Web',
    'operators': 'Go & Web', 'controllers': 'Go & Web', 'automation': 'Go & Web',
    'career': 'Career & Growth', 'interview': 'Career & Growth',
    'career-growth': 'Career & Growth', 'engineering-leadership': 'Career & Growth',
    'growth': 'Career & Growth', 'senior-to-staff': 'Career & Growth',
    'staff-engineering': 'Career & Growth', 'leadership': 'Career & Growth',
    'problem-solving': 'Career & Growth', 'algorithms': 'Career & Growth',
    'ai': 'AI & Agents', 'ai-engineering': 'AI & Agents', 'llm': 'AI & Agents',
    'knowledge-management': 'AI & Agents', 'harness': 'AI & Agents',
    'python': 'Python & Tools', 'bash': 'Python & Tools',
    'stream-processing': 'Stream Processing', 'batch-processing': 'Stream Processing',
    'cdc': 'Stream Processing', 'infrastructure': 'Infrastructure',
    'deployment': 'Infrastructure', 'databases': 'Infrastructure',
    'meta': 'Meta',
}

CAT_ORDER = ['Data Engineering', 'Software Design', 'Testing', 'System Architecture',
             'Go & Web', 'Stream Processing', 'Infrastructure', 'Career & Growth',
             'Python & Tools', 'AI & Agents', 'Meta']

def load_slug_map():
    for d in [CONCEPTS_DIR, SOURCES_DIR, SYNTHESES_DIR]:
        if not d.exists():
            continue
        for f in d.glob("*.md"):
            content = f.read_text()
            m = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
            if m:
                try:
                    fm = yaml.safe_load(m.group(1))
                    title = fm.get("title", f.stem)
                    ptype = fm.get("type", "concept")
                    if d == CONCEPTS_DIR:
                        rel = f"concepts/{f.stem}"
                    elif d == SOURCES_DIR:
                        rel = f"sources/{f.stem}"
                    else:
                        rel = f"syntheses/{f.stem}"
                    SLUG_MAP[rel] = {"title": title, "type": ptype, "tags": fm.get("tags", []), "sources": fm.get("sources", []), "concepts": fm.get("concepts", [])}
                    SLUG_MAP[f.stem] = {"title": title, "type": ptype, "tags": fm.get("tags", []), "sources": fm.get("sources", []), "concepts": fm.get("concepts", [])}
                except Exception:
                    pass

def convert_wikilinks(text, output_dir):
    is_concept = (output_dir == CONCEPTS_DIR)
    is_source = (output_dir == SOURCES_DIR)

    def replace_link(m):
        full = m.group(1).strip()
        if "|" in full:
            target, display = full.split("|", 1)
        else:
            target = full
            display = full
        target = target.strip()
        display = display.strip()

        if target.startswith("concepts/"):
            slug = target.replace("concepts/", "")
            href = f"../concepts/{slug}.html" if is_source else f"{slug}.html"
        elif target.startswith("sources/"):
            return f'<span class="wiki-link source-ref">{display}</span>'
        elif target.startswith("syntheses/"):
            slug = target.replace("syntheses/", "")
            href = f"../syntheses/{slug}.html"
        elif is_source:
            entry = SLUG_MAP.get(target)
            if entry and entry["type"] == "source":
                href = f"{target}.html"
            else:
                href = f"../concepts/{target}.html"
        else:
            entry = SLUG_MAP.get(target)
            if entry and entry["type"] == "source":
                return f'<span class="wiki-link source-ref">{display}</span>'
            elif entry and entry["type"] == "synthesis":
                href = f"../syntheses/{target}.html"
            else:
                href = f"{target}.html"
        return f'<a href="{href}" class="wiki-link">{display}</a>'

    return re.sub(r'\[\[(.*?)\]\]', replace_link, text)

def md_to_html(text, output_dir):
    lines = text.split('\n')
    html_lines = []
    in_code_block = False
    code_lang = ""
    code_content = []
    in_list = False
    list_type = None
    in_table = False

    def close_list():
        nonlocal in_list, list_type
        if in_list:
            html_lines.append(f'</{list_type}>')
            in_list = False
            list_type = None

    def close_code():
        nonlocal in_code_block, code_lang, code_content
        if in_code_block:
            lang_class = f' class="language-{code_lang}"' if code_lang else ''
            html_lines.append(f'<pre><code{lang_class}>{html.escape(chr(10).join(code_content))}</code></pre>')
            code_content = []
            in_code_block = False
            code_lang = ""

    for line in lines:
        if line.startswith('```'):
            if in_code_block:
                close_code()
            else:
                close_list()
                in_code_block = True
                code_lang = line[3:].strip()
            continue
        if in_code_block:
            code_content.append(line)
            continue

        heading_match = re.match(r'^(#{2,6})\s+(.*)', line)
        if heading_match:
            close_list()
            level = len(heading_match.group(1))
            content = convert_wikilinks(heading_match.group(2), output_dir)
            content = inline_format(content)
            slug = re.sub(r'[^a-z0-9-]', '', heading_match.group(2).lower().replace(' ', '-'))[:40]
            html_lines.append(f'<h{level} id="{slug}">{content}</h{level}>')
            continue

        if line.startswith('> '):
            close_list()
            content = convert_wikilinks(line[2:], output_dir)
            content = inline_format(content)
            html_lines.append(f'<blockquote>{content}</blockquote>')
            continue

        if '|' in line and line.strip().startswith('|'):
            close_list()
            cells = [c.strip() for c in line.split('|')[1:-1]]
            if all(set(c.strip()) <= set('-|: ') for c in cells):
                continue
            if not in_table:
                in_table = True
                html_lines.append('<table><thead><tr>')
                for cell in cells:
                    cell = inline_format(convert_wikilinks(cell, output_dir))
                    html_lines.append(f'<th>{cell}</th>')
                html_lines.append('</tr></thead><tbody>')
            else:
                html_lines.append('<tr>')
                for cell in cells:
                    cell = inline_format(convert_wikilinks(cell, output_dir))
                    html_lines.append(f'<td>{cell}</td>')
                html_lines.append('</tr>')
            continue

        if in_table:
            in_table = False
            html_lines.append('</tbody></table>')

        if re.match(r'^[-*]\s+', line):
            if not in_list:
                in_list = True
                list_type = 'ul'
                html_lines.append('<ul>')
            content = re.sub(r'^[-*]\s+', '', line)
            content = convert_wikilinks(content, output_dir)
            content = inline_format(content)
            html_lines.append(f'<li>{content}</li>')
            continue

        if re.match(r'^\d+\.\s+', line):
            if not in_list:
                in_list = True
                list_type = 'ol'
                html_lines.append('<ol>')
            content = re.sub(r'^\d+\.\s+', '', line)
            content = convert_wikilinks(content, output_dir)
            content = inline_format(content)
            html_lines.append(f'<li>{content}</li>')
            continue

        if line.strip() == '---' and not in_code_block:
            close_list()
            break

        if not line.strip():
            close_list()
            continue

        close_list()
        content = convert_wikilinks(line, output_dir)
        content = inline_format(content)
        html_lines.append(f'<p>{content}</p>')

    close_list()
    close_code()
    result = '\n'.join(html_lines)
    if '<table>' in result and '</table>' not in result:
        result += '</tbody></table>'
    return result

def inline_format(text):
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2" target="_blank" rel="noopener">\1</a>', text)
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    text = re.sub(r'`(.+?)`', r'<code>\1</code>', text)
    return text

PAGE_HEAD = '''<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — LLM Wiki</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{css_href}">
<link rel="stylesheet" href="https://unpkg.com/tippy.js@6/dist/tippy.css">
<link href="../pagefind/pagefind-ui.css" rel="stylesheet">
</head>
<body>
<header class="site-header">
  <button id="sidebar-toggle" class="icon-btn" aria-label="Toggle sidebar">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
  </button>
  <a href="{index_href}" class="site-title">LLM Wiki</a>
  <div class="header-actions">
    <div id="search"></div>
    <button id="theme-toggle" class="icon-btn" aria-label="Toggle theme">
      <svg class="icon-sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/></svg>
      <svg class="icon-moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>
    </button>
  </div>
</header>
<div id="sidebar-overlay"></div>
<div class="layout">
<aside class="sidebar" id="sidebar">
  <div class="sidebar-content">
    <h3>Concepts</h3>
    <nav id="sidebar-nav"><p style="color:var(--color-ink-dim);font-size:var(--text-sm);padding:0.5rem;">Loading…</p></nav>
    <div class="sidebar-resize-handle"></div>
  </div>
</aside>
<main class="main-content">'''

PAGE_FOOT = '''</main>
<aside class="right-sidebar" id="right-sidebar">
  <div class="toc-container">
    <h3>On This Page</h3>
    <nav id="toc"></nav>
  </div>
</aside>
</div>
<footer class="page-footer">
  <div class="page-footer-inner">
    <span><a href="{index_href}">LLM Wiki</a> · A living knowledge base</span>
    <span><a href="https://github.com/phamhoangtuan/llm-wiki">GitHub</a></span>
  </div>
</footer>
<button id="focus-toggle" class="icon-btn" title="Focus mode" aria-label="Toggle focus mode">
  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"><path d="M8 3H5a2 2 0 0 0-2 2v3m18 0V5a2 2 0 0 0-2-2h-3m0 18h3a2 2 0 0 0 2-2v-3M3 16v3a2 2 0 0 0 2 2h3"/></svg>
</button>
<script src="https://unpkg.com/@popperjs/core@2"></script>
<script src="https://unpkg.com/tippy.js@6"></script>
<script src="../pagefind/pagefind-ui.js"></script>
<script src="{scripts_href}/theme.js"></script>
<script src="{scripts_href}/sidebar.js"></script>
<script src="{scripts_href}/focus.js"></script>
<script src="{scripts_href}/toc.js"></script>
<script src="{scripts_href}/popovers.js"></script>
<script>window.addEventListener('DOMContentLoaded',function(){{if(window.PagefindUI)new PagefindUI({{element:'#search',showImages:false}});}});</script>
</body>
</html>'''

def build_page_head(title, depth):
    css_href = "../styles/main.css" if depth == 1 else "../../styles/main.css"
    scripts_href = "../scripts/js" if depth == 1 else "../../scripts/js"
    index_href = "../index.html" if depth == 1 else "../../index.html"
    return PAGE_HEAD.format(title=title, css_href=css_href, index_href=index_href, scripts_href=scripts_href)

def build_page_tail(depth):
    scripts_href = "../scripts/js" if depth == 1 else "../../scripts/js"
    index_href = "../index.html" if depth == 1 else "../../index.html"
    return PAGE_FOOT.format(scripts_href=scripts_href, index_href=index_href)

def build_connections_section(connections, output_dir):
    if not connections:
        return ""
    conn_items = []
    for line in connections:
        line = line.strip()
        if not line:
            continue
        m = re.match(r'^(Core to|Foundation for|Extends|Complements|Used by|Related to|Contrasts with|Informs|Drives|Enforced by|Supported by|Protects|Prevents|Managed by|Reduced by|Relies on|Requires|Depends on|Operationalizes|Enforced|Supports)\s+\[\[([^\]]+)\]\](.*)', line)
        if m:
            rel_type = m.group(1)
            target = m.group(2).strip()
            desc = m.group(3).strip().lstrip('—').strip()
            conn_items.append({"type": rel_type, "target": target, "desc": desc})
        else:
            m2 = re.match(r'.*?\[\[([^\]]+)\]\](.*)', line)
            if m2:
                target = m2.group(1).strip()
                desc = m2.group(2).strip().lstrip('—').strip()
                conn_items.append({"type": "Related", "target": target, "desc": desc})
    if not conn_items:
        return ""

    is_concept = (output_dir == CONCEPTS_DIR)
    is_source = (output_dir == SOURCES_DIR)
    cards_html = ""
    for c in conn_items:
        target = c["target"]
        if target.startswith("concepts/"):
            slug = target.replace("concepts/", "")
            href = f"../concepts/{slug}.html" if is_source else f"{slug}.html"
        elif target.startswith("sources/"):
            source_title = SLUG_MAP.get(target, {}).get("title", target)
            cards_html += f'\n    <div class="connection-card text-ref">\n      <span class="connection-type related">{c["type"]}</span>\n      <h4>{source_title}</h4>\n      <p>{c["desc"]}</p>\n    </div>'
            continue
        elif is_source:
            href = f"../concepts/{target}.html"
        elif is_concept:
            entry = SLUG_MAP.get(target)
            if entry and entry["type"] == "source":
                source_title = SLUG_MAP.get(target, {}).get("title", target)
                cards_html += f'\n    <div class="connection-card text-ref">\n      <span class="connection-type related">{c["type"]}</span>\n      <h4>{source_title}</h4>\n      <p>{c["desc"]}</p>\n    </div>'
                continue
            href = f"{target}.html"
        else:
            href = f"{target}.html"

        type_class = "related"
        if c["type"] in ("Core to", "Foundation for", "Core rule of"):
            type_class = "core"
        elif c["type"] in ("Extends", "Enforced by", "Enforced", "Supports"):
            type_class = "extends"
        elif c["type"] in ("Drives", "Prevents", "Protects"):
            type_class = "drives"

        title = SLUG_MAP.get(target, {}).get("title", target)
        cards_html += f'\n    <a class="connection-card" href="{href}">\n      <span class="connection-type {type_class}">{c["type"]}</span>\n      <h4>{title}</h4>\n      <p>{c["desc"]}</p>\n    </a>'

    return f'''<section class="connections-section">
  <h2>Connections</h2>
  <div class="connections-grid">{cards_html}
  </div>
</section>'''

def build_breadcrumb(tags, ptype, page_title, depth):
    cat = tags[0].replace('-', ' ').title() if tags else 'Uncategorized'
    index_href = "../index.html" if depth == 1 else "../../index.html"
    return f'''<nav class="breadcrumb">
  <a href="{index_href}">Home</a> <span class="sep">/</span>
  <a href="{index_href}#cat-{tags[0] if tags else 'uncategorized'}">{cat}</a> <span class="sep">/</span>
  <span>{page_title}</span>
</nav>'''

def build_pagination(md_files, current_slug, output_dir, depth):
    slugs = [f.stem for f in sorted(md_files)]
    try:
        idx = slugs.index(current_slug)
    except ValueError:
        return ""
    prev_html = ""
    next_html = ""
    prefix = "" if depth == 1 else "../"
    if idx > 0:
        prev_slug = slugs[idx - 1]
        prev_entry = SLUG_MAP.get(prev_slug, {})
        prev_title = prev_entry.get("title", prev_slug)
        prev_html = f'<a href="{prefix}{prev_slug}.html" class="prev">← {prev_title}</a>'
    if idx < len(slugs) - 1:
        next_slug = slugs[idx + 1]
        next_entry = SLUG_MAP.get(next_slug, {})
        next_title = next_entry.get("title", next_slug)
        next_html = f'<a href="{prefix}{next_slug}.html" class="next">{next_title} →</a>'
    if not prev_html and not next_html:
        return ""
    return f'<nav class="pagination">{prev_html}{next_html}</nav>'

def convert_file(md_path, output_dir, ptype, depth=1):
    content = md_path.read_text()
    m = re.match(r'^---\n(.*?)\n---\n(.*)', content, re.DOTALL)
    if not m:
        return
    fm = yaml.safe_load(m.group(1))
    body_md = m.group(2).strip()

    title = html.escape(str(fm.get("title", md_path.stem)))
    tags = fm.get("tags", [])
    updated = fm.get("updated", "2026-05-23")
    sources = fm.get("sources", [])

    tags_html = "".join(f'<span class="tag">{t}</span>' for t in tags)
    badge_class = "concept" if ptype == "concept" else ("source" if ptype == "source" else "synthesis")
    badge_label = "Concept" if ptype == "concept" else ("Source" if ptype == "source" else "Synthesis")

    body_html = md_to_html(body_md, output_dir)
    content_class = badge_class

    connections = []
    parts = body_md.split('\n---\n')
    after_separator = parts[-1] if len(parts) > 1 else ""
    for line in after_separator.split('\n'):
        line = line.strip()
        if line.startswith('- ') and ('[[' in line):
            connections.append(line[2:])
    connections_html = build_connections_section(connections, output_dir)

    breadcrumb = build_breadcrumb(tags, ptype, title, depth)
    pagination = build_pagination(sorted(output_dir.glob("*.md")), md_path.stem, output_dir, depth)

    if ptype == "source":
        author = fm.get("author", "Unknown")
        source_type = fm.get("source_type", "article")
        source_date = fm.get("source_date", "Unknown")
        ingested = fm.get("ingested", "Unknown")
        meta_html = f'<span>By {html.escape(str(author))}</span><span>{html.escape(str(source_type))}</span><span>{html.escape(str(source_date))}</span><span>Ingested: {html.escape(str(ingested))}</span>'
    elif ptype == "synthesis":
        sources_list = ", ".join(sources) if sources else "Unknown"
        created = fm.get("created", "2026-06-08")
        meta_html = f'<span>Created: {html.escape(str(created))}</span><span>Updated: {html.escape(str(updated))}</span>'
    else:
        source_name = ", ".join(sources) if sources else "Unknown"
        meta_html = f'<span>Source: {html.escape(str(source_name))}</span><span>Updated: {html.escape(str(updated))}</span>'

    head = build_page_head(title, depth)
    page = f'''{head}
<div class="breadcrumb-wrapper">{breadcrumb}</div>
<div class="page-hero">
  <div class="page-type-badge {badge_class}">{badge_label}</div>
  <h1>{title}</h1>
  <div class="page-meta">{meta_html}</div>
  <div class="page-tags">{tags_html}</div>
</div>
<div class="content-area {content_class}">
{body_html}
</div>
{connections_html}
{pagination}
{build_page_tail(depth)}'''

    output_path = output_dir / f"{md_path.stem}.html"
    output_path.write_text(page)

def generate_concepts_json():
    concepts = {}
    if CONCEPTS_DIR.exists():
        for f in sorted(CONCEPTS_DIR.glob("*.md")):
            content = f.read_text()
            m = re.match(r'^---\n(.*?)\n---\n(.*)', content, re.DOTALL)
            if not m:
                continue
            fm = yaml.safe_load(m.group(1))
            body = m.group(2).strip()
            title = fm.get("title", f.stem)
            tags = fm.get("tags", [])
            cat = 'Meta'
            for t in tags:
                if t in CATEGORY_MAP:
                    cat = CATEGORY_MAP[t]
                    break
            parts = body.split('\n---\n')
            main = parts[0]
            first_p = ""
            for line in main.split('\n'):
                line = line.strip()
                if line and not line.startswith('#') and not line.startswith('|') and not line.startswith('```') and not line.startswith('>'):
                    first_p = line[:200]
                    break
            concepts[f.stem] = {
                "title": title,
                "category": cat,
                "url": f"concepts/{f.stem}.html",
                "definition": first_p,
                "tags": tags,
            }
    META_DIR.mkdir(exist_ok=True)
    out = {"concepts": concepts}
    (META_DIR / "concepts.json").write_text(json.dumps(out, ensure_ascii=False, indent=2))

def generate_backlinks_json():
    links = defaultdict(list)
    for d in [CONCEPTS_DIR, SOURCES_DIR, SYNTHESES_DIR]:
        if not d.exists():
            continue
        for f in sorted(d.glob("*.md")):
            content = f.read_text()
            for match in re.finditer(r'\[\[([^\]]+)\]\]', content):
                target = match.group(1).split('|')[0].strip()
                links[target].append(f.stem)
    META_DIR.mkdir(exist_ok=True)
    (META_DIR / "backlinks.json").write_text(json.dumps(dict(links), ensure_ascii=False, indent=2))

def generate_moc_table():
    concepts = {}
    if CONCEPTS_DIR.exists():
        for f in sorted(CONCEPTS_DIR.glob("*.md")):
            content = f.read_text()
            m = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
            if not m:
                continue
            fm = yaml.safe_load(m.group(1))
            tags = fm.get("tags", [])
            cat = 'Meta'
            for t in tags:
                if t in CATEGORY_MAP:
                    cat = CATEGORY_MAP[t]
                    break
            if cat not in concepts:
                concepts[cat] = []
            concepts[cat].append((fm.get("title", f.stem), f.stem))

    sorted_cats = sorted(concepts.items(), key=lambda x: CAT_ORDER.index(x[0]) if x[0] in CAT_ORDER else 99)
    rows = ""
    for cat, items in sorted_cats:
        cat_slug = cat.lower().replace(' & ', '-').replace(' ', '-')
        links = ""
        for i, (title, slug) in enumerate(items):
            comma = '<span class="comma">, </span>' if i < len(items) - 1 else ''
            links += f'<span class="concept-item-wrapper"><a href="concepts/{slug}.html" class="concept-tag">{title}</a>{comma}</span>'
        rows += f'<tr id="row-{cat_slug}"><td class="cat-cell"><strong>{cat}</strong></td><td class="concepts-cell"><div class="concepts-list">{links}</div></td></tr>'
    return rows

    return rows

def update_index_html():
    index_path = WIKI_ROOT / "index.html"
    if not index_path.exists():
        return
    content = index_path.read_text()
    rows = generate_moc_table()
    n_concepts = len(list(CONCEPTS_DIR.glob("*.md"))) if CONCEPTS_DIR.exists() else 0
    n_cats = rows.count('<tr id="row-')
    desc = f'{n_concepts} concepts across {n_cats} categories.'

    content = re.sub(r'<!-- MOC_DESC -->.*?</p>', f'<!-- MOC_DESC -->{desc}</p>', content, flags=re.DOTALL)
    content = content.replace('<!-- MOC_TABLE -->', rows)
    index_path.write_text(content)

def main():
    load_slug_map()

    print("Generating concepts.json...")
    generate_concepts_json()
    print("Generating backlinks.json...")
    generate_backlinks_json()

    print("\nConverting concept pages...")
    for md_file in sorted(CONCEPTS_DIR.glob("*.md")):
        print(f"  → {md_file.stem}.html")
        convert_file(md_file, CONCEPTS_DIR, "concept", depth=1)

    # Source HTML pages are intentionally not generated — sources only exist as
    # canonical markdown in the repo, not on the public website.
    # print("\nConverting source pages...")
    # for md_file in sorted(SOURCES_DIR.glob("*.md")):
    #     print(f"  → {md_file.stem}.html")
    #     convert_file(md_file, SOURCES_DIR, "source", depth=1)

    if SYNTHESES_DIR.exists():
        print("\nConverting synthesis pages...")
        for md_file in sorted(SYNTHESES_DIR.glob("*.md")):
            print(f"  → {md_file.stem}.html")
            convert_file(md_file, SYNTHESES_DIR, "synthesis", depth=1)

    print("\nUpdating index.html MOC table...")
    update_index_html()

    print("\nDone!")

if __name__ == "__main__":
    main()
