#!/usr/bin/env python3
"""Convert wiki markdown files to HTML using the unified template."""

import re
import yaml
import html
import sys
from pathlib import Path

WIKI_ROOT = Path(__file__).parent.parent
CONCEPTS_DIR = WIKI_ROOT / "concepts"
SOURCES_DIR = WIKI_ROOT / "sources"
SYNTHESES_DIR = WIKI_ROOT / "syntheses"

# Build a slug-to-title map from all existing MD files
SLUG_MAP = {}

def load_slug_map():
    """Scan all MD files to build slug -> title mapping."""
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
                    # Determine the relative path
                    if d == CONCEPTS_DIR:
                        rel = f"concepts/{f.stem}"
                    elif d == SOURCES_DIR:
                        rel = f"sources/{f.stem}"
                    else:
                        rel = f"syntheses/{f.stem}"
                    SLUG_MAP[rel] = {"title": title, "type": ptype}
                    SLUG_MAP[f.stem] = {"title": title, "type": ptype}
                except:
                    pass

def convert_wikilinks(text):
    """Convert [[wikilinks]] and [[wikilinks|display]] to HTML anchor tags."""
    def replace_link(m):
        full = m.group(1).strip()
        if "|" in full:
            target, display = full.split("|", 1)
        else:
            target = full
            display = full

        target = target.strip()
        display = display.strip()

        # Determine the HTML file path
        # Check if it's a concepts/ or sources/ reference
        if target.startswith("concepts/"):
            slug = target.replace("concepts/", "")
            href = f"{slug}.html"
        elif target.startswith("sources/"):
            slug = target.replace("sources/", "")
            href = f"../sources/{slug}.html"
        elif target.startswith("syntheses/"):
            slug = target.replace("syntheses/", "")
            href = f"../syntheses/{slug}.html"
        else:
            # Try to find the slug
            slug = target
            href = f"{slug}.html"

        return f'<a href="{href}" class="wiki-link">{display}</a>'

    return re.sub(r'\[\[(.*?)\]\]', replace_link, text)

def md_to_html(text):
    """Simple markdown to HTML converter."""
    lines = text.split('\n')
    html_lines = []
    in_code_block = False
    code_lang = ""
    code_content = []
    in_list = False
    list_type = None

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
        # Code blocks
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

        # Headings
        heading_match = re.match(r'^(#{2,6})\s+(.*)', line)
        if heading_match:
            close_list()
            level = len(heading_match.group(1))
            content = convert_wikilinks(heading_match.group(2))
            content = inline_format(content)
            html_lines.append(f'<h{level}>{content}</h{level}>')
            continue

        # Blockquotes
        if line.startswith('> '):
            close_list()
            content = convert_wikilinks(line[2:])
            content = inline_format(content)
            html_lines.append(f'<blockquote>{content}</blockquote>')
            continue

        # Tables
        if '|' in line and line.strip().startswith('|'):
            close_list()
            cells = [c.strip() for c in line.split('|')[1:-1]]
            # Check if it's a separator line
            if all(set(c.strip()) <= set('-|: ') for c in cells):
                continue
            if not html_lines or not html_lines[-1].startswith('<table'):
                html_lines.append('<table><thead><tr>')
                for cell in cells:
                    cell = inline_format(convert_wikilinks(cell))
                    html_lines.append(f'<th>{cell}</th>')
                html_lines.append('</tr></thead><tbody>')
            else:
                html_lines.append('<tr>')
                for cell in cells:
                    cell = inline_format(convert_wikilinks(cell))
                    html_lines.append(f'<td>{cell}</td>')
                html_lines.append('</tr>')
            continue

        # Close table if we were in one
        if html_lines and html_lines[-1] == '</tbody></table>' or (html_lines and '</tbody>' in html_lines[-1] and '<table' not in html_lines[-1]):
            pass  # Already closed

        # Unordered lists
        if re.match(r'^[-*]\s+', line):
            if not in_list:
                in_list = True
                list_type = 'ul'
                html_lines.append('<ul>')
            content = re.sub(r'^[-*]\s+', '', line)
            content = convert_wikilinks(content)
            content = inline_format(content)
            html_lines.append(f'<li>{content}</li>')
            continue

        # Ordered lists
        if re.match(r'^\d+\.\s+', line):
            if not in_list:
                in_list = True
                list_type = 'ol'
                html_lines.append('<ol>')
            content = re.sub(r'^\d+\.\s+', '', line)
            content = convert_wikilinks(content)
            content = inline_format(content)
            html_lines.append(f'<li>{content}</li>')
            continue

        # Empty line
        if not line.strip():
            close_list()
            continue

        # Regular paragraph
        close_list()
        content = convert_wikilinks(line)
        content = inline_format(content)
        html_lines.append(f'<p>{content}</p>')

    close_list()
    close_code()

    # Close any open table
    result = '\n'.join(html_lines)
    if '<table>' in result and '</table>' not in result:
        result += '</tbody></table>'

    return result

def inline_format(text):
    """Apply inline markdown formatting."""
    # Bold
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    # Italic
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    # Inline code
    text = re.sub(r'`(.+?)`', r'<code>\1</code>', text)
    return text

CONCEPT_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — LLM Wiki</title>
<style>
  :root {{
    --bg: #0f1117; --surface: #1a1d27; --surface-2: #242736; --border: #2a2d3e;
    --text: #e4e6f0; --text-dim: #8b8fa8; --accent: #f0b429; --accent-dim: #b8860b;
    --accent-glow: rgba(240, 180, 41, 0.15); --green: #4ade80; --blue: #60a5fa;
    --rose: #fb7185; --purple: #a78bfa; --teal: #2dd4bf; --radius: 12px;
    --font: 'Segoe UI', system-ui, -apple-system, sans-serif;
    --mono: 'JetBrains Mono', 'Fira Code', 'Cascadia Code', monospace;
  }}
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{ font-family: var(--font); background: var(--bg); color: var(--text); line-height: 1.6; overflow-x: hidden; }}
  ::-webkit-scrollbar {{ width: 6px; }}
  ::-webkit-scrollbar-track {{ background: var(--bg); }}
  ::-webkit-scrollbar-thumb {{ background: var(--border); border-radius: 3px; }}
  .hero {{ min-height: 50vh; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; padding: 2rem; position: relative; overflow: hidden; }}
  .hero-bg {{ position: absolute; inset: 0; background: radial-gradient(ellipse 600px 400px at 30% 50%, rgba(96,165,250,0.08) 0%, transparent 70%), radial-gradient(ellipse 500px 500px at 70% 30%, rgba(240,180,41,0.06) 0%, transparent 70%), radial-gradient(ellipse 400px 400px at 50% 80%, rgba(167,139,250,0.04) 0%, transparent 70%); z-index: 0; }}
  .hero-content {{ position: relative; z-index: 1; max-width: 720px; }}
  .hero-badge {{ display: inline-flex; align-items: center; gap: 6px; background: rgba(96,165,250,0.12); border: 1px solid rgba(96,165,250,0.25); color: var(--blue); font-size: 0.8rem; font-weight: 600; padding: 6px 14px; border-radius: 100px; letter-spacing: 0.5px; margin-bottom: 1.5rem; }}
  .hero-badge::before {{ content: ''; width: 6px; height: 6px; border-radius: 50%; background: var(--blue); box-shadow: 0 0 8px var(--blue); }}
  .hero h1 {{ font-size: clamp(2.5rem, 6vw, 4rem); font-weight: 800; letter-spacing: -2px; line-height: 1.1; margin-bottom: 1rem; }}
  .hero h1 span {{ color: var(--blue); }}
  .hero-sub {{ font-size: clamp(1rem, 2vw, 1.2rem); color: var(--text-dim); max-width: 580px; margin: 0 auto 2rem; }}
  .hero-tags {{ display: flex; gap: 8px; justify-content: center; flex-wrap: wrap; margin-bottom: 1.5rem; }}
  .tag {{ font-size: 0.72rem; font-weight: 600; padding: 4px 10px; border-radius: 6px; background: var(--surface); border: 1px solid var(--border); color: var(--text-dim); }}
  .hero-meta {{ font-size: 0.78rem; color: var(--text-dim); opacity: 0.7; }}
  .hero-back {{ display: inline-flex; align-items: center; gap: 8px; color: var(--accent); font-size: 0.85rem; font-weight: 600; text-decoration: none; margin-bottom: 1.5rem; transition: opacity 0.2s; }}
  .hero-back:hover {{ opacity: 0.8; }}
  .hero-back svg {{ width: 16px; height: 16px; }}
  section {{ padding: 4rem 2rem; max-width: 900px; margin: 0 auto; }}
  .section-label {{ display: inline-block; font-size: 0.7rem; font-weight: 700; letter-spacing: 2px; text-transform: uppercase; color: var(--accent); margin-bottom: 0.75rem; }}
  .section-title {{ font-size: clamp(1.5rem, 3vw, 2rem); font-weight: 700; margin-bottom: 1rem; }}
  .section-desc {{ color: var(--text-dim); font-size: 1.05rem; margin-bottom: 2rem; }}
  .content-area {{ background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius); padding: 2.5rem; margin-bottom: 3rem; border-left: 3px solid var(--blue); }}
  .content-area h2 {{ font-size: 1.3rem; margin: 2rem 0 1rem; color: var(--text); }}
  .content-area h2:first-child {{ margin-top: 0; }}
  .content-area h3 {{ font-size: 1.1rem; margin: 1.5rem 0 0.75rem; color: var(--text); }}
  .content-area p {{ margin-bottom: 1rem; line-height: 1.7; }}
  .content-area ul, .content-area ol {{ margin: 0.5rem 0 1rem 1.5rem; }}
  .content-area li {{ margin-bottom: 0.4rem; line-height: 1.6; }}
  .content-area blockquote {{ margin: 1rem 0; padding: 1rem 1.25rem; background: var(--surface-2); border-radius: 8px; border-left: 3px solid var(--accent); font-style: italic; color: var(--text-dim); }}
  .content-area pre {{ background: var(--surface-2); border: 1px solid var(--border); border-radius: 8px; padding: 1.25rem; overflow-x: auto; margin: 1rem 0; }}
  .content-area pre code {{ font-family: var(--mono); font-size: 0.85rem; line-height: 1.6; color: var(--text); }}
  .content-area code {{ font-family: var(--mono); font-size: 0.85rem; background: var(--surface-2); padding: 2px 6px; border-radius: 4px; color: var(--rose); }}
  .content-area pre code {{ background: none; padding: 0; color: var(--text); }}
  .content-area table {{ width: 100%; border-collapse: collapse; margin: 1rem 0; }}
  .content-area th, .content-area td {{ border: 1px solid var(--border); padding: 0.6rem 0.75rem; text-align: left; font-size: 0.9rem; }}
  .content-area th {{ background: var(--surface-2); font-weight: 600; color: var(--text-dim); font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.5px; }}
  .content-area td code {{ font-size: 0.82rem; }}
  .content-area strong {{ color: var(--text); }}
  .wiki-link {{ color: var(--blue); text-decoration: none; border-bottom: 1px solid rgba(96,165,250,0.3); transition: border-color 0.2s; }}
  .wiki-link:hover {{ border-color: var(--blue); }}
  .connections-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 1rem; }}
  .connection-card {{ background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius); padding: 1.25rem; text-decoration: none; color: inherit; transition: border-color 0.2s, transform 0.2s; }}
  .connection-card:hover {{ border-color: var(--accent-dim); transform: translateY(-2px); }}
  .connection-card h4 {{ font-size: 0.88rem; color: var(--blue); margin-bottom: 0.4rem; }}
  .connection-card p {{ font-size: 0.82rem; color: var(--text-dim); margin: 0; }}
  .connection-type {{ font-size: 0.68rem; font-weight: 600; padding: 2px 8px; border-radius: 4px; margin-bottom: 0.5rem; display: inline-block; }}
  .connection-type.core {{ background: rgba(240,180,41,0.12); color: var(--accent); }}
  .connection-type.related {{ background: rgba(167,139,250,0.12); color: var(--purple); }}
  .connection-type.extends {{ background: rgba(96,165,250,0.12); color: var(--blue); }}
  .connection-type.drives {{ background: rgba(45,212,191,0.12); color: var(--teal); }}
  footer {{ text-align: center; padding: 3rem 2rem; border-top: 1px solid var(--border); color: var(--text-dim); font-size: 0.85rem; }}
  footer a {{ color: var(--accent); text-decoration: none; }}
  @media (max-width: 768px) {{ section {{ padding: 2.5rem 1.25rem; }} .content-area {{ padding: 1.5rem; }} }}
  @media (prefers-color-scheme: light) {{
    :root {{ --bg: #f8f9fb; --surface: #ffffff; --surface-2: #f0f1f5; --border: #e2e4ec; --text: #1a1d27; --text-dim: #6b7089; }}
  }}
</style>
</head>
<body>
<div class="hero">
  <div class="hero-bg"></div>
  <div class="hero-content">
    <a href="../index.html" class="hero-back">
      <svg viewBox="0 0 16 16" fill="none"><path d="M13 8H3M7 4L3 8l4 4" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
      Back to Wiki Index
    </a>
    <div class="hero-badge">Concept</div>
    <h1>{title}<span>.</span></h1>
    <div class="hero-tags">{tags_html}</div>
    <p class="hero-meta">Source: {source_name} · Updated: {updated}</p>
  </div>
</div>
<section>
  <div class="content-area">
{body_html}
  </div>
</section>
{connections_section}
<footer>
  <p>Part of the <a href="../index.html">LLM Wiki</a> · Based on <a href="https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f" target="_blank">Karpathy's LLM Wiki</a> pattern</p>
  <p style="margin-top:0.5rem;font-size:0.78rem;">All markdown. Zero lock-in.</p>
</footer>
<script>
  if (window.matchMedia('(prefers-color-scheme: light)').matches) {{
    document.documentElement.style.setProperty('--bg', '#f8f9fb');
    document.documentElement.style.setProperty('--surface', '#ffffff');
    document.documentElement.style.setProperty('--surface-2', '#f0f1f5');
    document.documentElement.style.setProperty('--border', '#e2e4ec');
    document.documentElement.style.setProperty('--text', '#1a1d27');
    document.documentElement.style.setProperty('--text-dim', '#6b7089');
  }}
</script>
</body>
</html>'''

SOURCE_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — LLM Wiki</title>
<style>
  :root {{
    --bg: #0f1117; --surface: #1a1d27; --surface-2: #242736; --border: #2a2d3e;
    --text: #e4e6f0; --text-dim: #8b8fa8; --accent: #f0b429; --accent-dim: #b8860b;
    --accent-glow: rgba(240, 180, 41, 0.15); --green: #4ade80; --blue: #60a5fa;
    --rose: #fb7185; --purple: #a78bfa; --teal: #2dd4bf; --radius: 12px;
    --font: 'Segoe UI', system-ui, -apple-system, sans-serif;
    --mono: 'JetBrains Mono', 'Fira Code', 'Cascadia Code', monospace;
  }}
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{ font-family: var(--font); background: var(--bg); color: var(--text); line-height: 1.6; overflow-x: hidden; }}
  ::-webkit-scrollbar {{ width: 6px; }} ::-webkit-scrollbar-track {{ background: var(--bg); }} ::-webkit-scrollbar-thumb {{ background: var(--border); border-radius: 3px; }}
  .hero {{ min-height: 50vh; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; padding: 2rem; position: relative; overflow: hidden; }}
  .hero-bg {{ position: absolute; inset: 0; background: radial-gradient(ellipse 600px 400px at 30% 50%, rgba(45,212,191,0.08) 0%, transparent 70%), radial-gradient(ellipse 500px 500px at 70% 30%, rgba(240,180,41,0.06) 0%, transparent 70%); z-index: 0; }}
  .hero-content {{ position: relative; z-index: 1; max-width: 720px; }}
  .hero-badge {{ display: inline-flex; align-items: center; gap: 6px; background: rgba(45,212,191,0.12); border: 1px solid rgba(45,212,191,0.25); color: var(--teal); font-size: 0.8rem; font-weight: 600; padding: 6px 14px; border-radius: 100px; letter-spacing: 0.5px; margin-bottom: 1.5rem; }}
  .hero-badge::before {{ content: ''; width: 6px; height: 6px; border-radius: 50%; background: var(--teal); box-shadow: 0 0 8px var(--teal); }}
  .hero h1 {{ font-size: clamp(2rem, 5vw, 3.5rem); font-weight: 800; letter-spacing: -2px; line-height: 1.1; margin-bottom: 1rem; }}
  .hero h1 span {{ color: var(--teal); }}
  .hero-sub {{ font-size: clamp(0.9rem, 1.5vw, 1.1rem); color: var(--text-dim); max-width: 580px; margin: 0 auto 1.5rem; }}
  .hero-tags {{ display: flex; gap: 8px; justify-content: center; flex-wrap: wrap; margin-bottom: 1.5rem; }}
  .tag {{ font-size: 0.72rem; font-weight: 600; padding: 4px 10px; border-radius: 6px; background: var(--surface); border: 1px solid var(--border); color: var(--text-dim); }}
  .hero-meta {{ font-size: 0.78rem; color: var(--text-dim); opacity: 0.7; }}
  .hero-back {{ display: inline-flex; align-items: center; gap: 8px; color: var(--accent); font-size: 0.85rem; font-weight: 600; text-decoration: none; margin-bottom: 1.5rem; transition: opacity 0.2s; }}
  .hero-back:hover {{ opacity: 0.8; }}
  .hero-back svg {{ width: 16px; height: 16px; }}
  section {{ padding: 4rem 2rem; max-width: 900px; margin: 0 auto; }}
  .section-label {{ display: inline-block; font-size: 0.7rem; font-weight: 700; letter-spacing: 2px; text-transform: uppercase; color: var(--accent); margin-bottom: 0.75rem; }}
  .section-title {{ font-size: clamp(1.5rem, 3vw, 2rem); font-weight: 700; margin-bottom: 1rem; }}
  .content-area {{ background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius); padding: 2.5rem; margin-bottom: 3rem; border-left: 3px solid var(--teal); }}
  .content-area h2 {{ font-size: 1.3rem; margin: 2rem 0 1rem; color: var(--text); }}
  .content-area h2:first-child {{ margin-top: 0; }}
  .content-area h3 {{ font-size: 1.1rem; margin: 1.5rem 0 0.75rem; color: var(--text); }}
  .content-area p {{ margin-bottom: 1rem; line-height: 1.7; }}
  .content-area ul, .content-area ol {{ margin: 0.5rem 0 1rem 1.5rem; }}
  .content-area li {{ margin-bottom: 0.4rem; line-height: 1.6; }}
  .content-area blockquote {{ margin: 1rem 0; padding: 1rem 1.25rem; background: var(--surface-2); border-radius: 8px; border-left: 3px solid var(--accent); font-style: italic; color: var(--text-dim); }}
  .content-area pre {{ background: var(--surface-2); border: 1px solid var(--border); border-radius: 8px; padding: 1.25rem; overflow-x: auto; margin: 1rem 0; }}
  .content-area pre code {{ font-family: var(--mono); font-size: 0.85rem; line-height: 1.6; color: var(--text); }}
  .content-area code {{ font-family: var(--mono); font-size: 0.85rem; background: var(--surface-2); padding: 2px 6px; border-radius: 4px; color: var(--rose); }}
  .content-area pre code {{ background: none; padding: 0; color: var(--text); }}
  .content-area strong {{ color: var(--text); }}
  .wiki-link {{ color: var(--blue); text-decoration: none; border-bottom: 1px solid rgba(96,165,250,0.3); transition: border-color 0.2s; }}
  .wiki-link:hover {{ border-color: var(--blue); }}
  .connections-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 1rem; }}
  .connection-card {{ background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius); padding: 1.25rem; text-decoration: none; color: inherit; transition: border-color 0.2s, transform 0.2s; }}
  .connection-card:hover {{ border-color: var(--accent-dim); transform: translateY(-2px); }}
  .connection-card h4 {{ font-size: 0.88rem; color: var(--blue); margin-bottom: 0.4rem; }}
  .connection-card p {{ font-size: 0.82rem; color: var(--text-dim); margin: 0; }}
  footer {{ text-align: center; padding: 3rem 2rem; border-top: 1px solid var(--border); color: var(--text-dim); font-size: 0.85rem; }}
  footer a {{ color: var(--accent); text-decoration: none; }}
  @media (max-width: 768px) {{ section {{ padding: 2.5rem 1.25rem; }} .content-area {{ padding: 1.5rem; }} }}
  @media (prefers-color-scheme: light) {{ :root {{ --bg: #f8f9fb; --surface: #ffffff; --surface-2: #f0f1f5; --border: #e2e4ec; --text: #1a1d27; --text-dim: #6b7089; }} }}
</style>
</head>
<body>
<div class="hero">
  <div class="hero-bg"></div>
  <div class="hero-content">
    <a href="../index.html" class="hero-back">
      <svg viewBox="0 0 16 16" fill="none"><path d="M13 8H3M7 4L3 8l4 4" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
      Back to Wiki Index
    </a>
    <div class="hero-badge">Source</div>
    <h1>{title}<span>.</span></h1>
    <p class="hero-sub">{author} · {source_type} · {source_date}</p>
    <div class="hero-tags">{tags_html}</div>
    <p class="hero-meta">Ingested: {ingested}</p>
  </div>
</div>
<section>
  <div class="content-area">
{body_html}
  </div>
</section>
{connections_section}
<footer>
  <p>Part of the <a href="../index.html">LLM Wiki</a> · Based on <a href="https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f" target="_blank">Karpathy's LLM Wiki</a> pattern</p>
  <p style="margin-top:0.5rem;font-size:0.78rem;">All markdown. Zero lock-in.</p>
</footer>
<script>
  if (window.matchMedia('(prefers-color-scheme: light)').matches) {{
    document.documentElement.style.setProperty('--bg', '#f8f9fb');
    document.documentElement.style.setProperty('--surface', '#ffffff');
    document.documentElement.style.setProperty('--surface-2', '#f0f1f5');
    document.documentElement.style.setProperty('--border', '#e2e4ec');
    document.documentElement.style.setProperty('--text', '#1a1d27');
    document.documentElement.style.setProperty('--text-dim', '#6b7089');
  }}
</script>
</body>
</html>'''

def build_connections_section(connections, base_path=""):
    """Build the connections section HTML."""
    if not connections:
        return ""

    # Parse connection lines
    conn_items = []
    for line in connections:
        line = line.strip()
        if not line:
            continue
        # Extract relationship type and target
        m = re.match(r'^(Core to|Foundation for|Extends|Complements|Used by|Related to|Contrasts with|Informs|Drives|Enforced by|Supported by|Protects|Prevents|Managed by|Reduced by|Relies on|Requires|Depends on|Operationalizes|Enforced|Supports)\s+\[\[([^\]]+)\]\](.*)', line)
        if m:
            rel_type = m.group(1)
            target = m.group(2).strip()
            desc = m.group(3).strip().lstrip('—').strip()
            conn_items.append({"type": rel_type, "target": target, "desc": desc})
        else:
            # Simple link
            m2 = re.match(r'\[\[([^\]]+)\]\](.*)', line)
            if m2:
                target = m2.group(1).strip()
                desc = m2.group(2).strip().lstrip('—').strip()
                conn_items.append({"type": "Related", "target": target, "desc": desc})

    if not conn_items:
        return ""

    cards_html = ""
    for c in conn_items:
        target = c["target"]
        # Resolve the target to an HTML file
        if target.startswith("concepts/"):
            slug = target.replace("concepts/", "")
            href = f"{slug}.html"
        elif target.startswith("sources/"):
            slug = target.replace("sources/", "")
            href = f"../sources/{slug}.html"
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

        cards_html += f'''
    <a class="connection-card" href="{href}">
      <span class="connection-type {type_class}">{c["type"]}</span>
      <h4>{title}</h4>
      <p>{c["desc"]}</p>
    </a>'''

    return f'''
<section>
  <div class="section-label">Knowledge Graph</div>
  <h2 class="section-title">Connections</h2>
  <div class="connections-grid">{cards_html}
  </div>
</section>'''

def convert_file(md_path, output_dir, template, is_source=False):
    """Convert a single MD file to HTML."""
    content = md_path.read_text()

    # Extract frontmatter
    m = re.match(r'^---\n(.*?)\n---\n(.*)', content, re.DOTALL)
    if not m:
        print(f"  Skipping {md_path.name} (no frontmatter)")
        return
    fm = yaml.safe_load(m.group(1))
    body_md = m.group(2).strip()

    title = fm.get("title", md_path.stem)
    tags = fm.get("tags", [])
    updated = fm.get("updated", "2026-05-23")
    sources = fm.get("sources", [])
    concepts = fm.get("concepts", [])

    # Tags HTML
    tags_html = "".join(f'<span class="tag">{t}</span>' for t in tags)

    # Source name
    source_name = ", ".join(sources) if sources else "Unknown"

    # Convert body
    body_html = md_to_html(body_md)

    # Connections
    connections = []
    for line in body_md.split('\n'):
        line = line.strip()
        if line.startswith('- ') and ('[[' in line):
            connections.append(line[2:])

    connections_html = build_connections_section(connections)

    # Format template
    if is_source:
        author = fm.get("author", "Unknown")
        source_type = fm.get("source_type", "article")
        source_date = fm.get("source_date", "Unknown")
        ingested = fm.get("ingested", "Unknown")
        html_content = template.format(
            title=html.escape(str(title)),
            author=html.escape(str(author)),
            source_type=html.escape(str(source_type)),
            source_date=html.escape(str(source_date)),
            ingested=html.escape(str(ingested)),
            tags_html=tags_html,
            body_html=body_html,
            connections_section=connections_html,
        )
    else:
        html_content = template.format(
            title=html.escape(str(title)),
            tags_html=tags_html,
            source_name=html.escape(str(source_name)),
            updated=html.escape(str(updated)),
            body_html=body_html,
            connections_section=connections_html,
        )

    # Write output
    output_path = output_dir / f"{md_path.stem}.html"
    output_path.write_text(html_content)
    print(f"  → {output_path.name}")

def main():
    load_slug_map()
    print("Converting concept pages...")
    for md_file in sorted(CONCEPTS_DIR.glob("*.md")):
        convert_file(md_file, CONCEPTS_DIR, CONCEPT_TEMPLATE, is_source=False)

    print("\nConverting source pages...")
    for md_file in sorted(SOURCES_DIR.glob("*.md")):
        convert_file(md_file, SOURCES_DIR, SOURCE_TEMPLATE, is_source=True)

    print("\nDone!")

if __name__ == "__main__":
    main()
