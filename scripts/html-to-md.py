#!/usr/bin/env python3
"""One-time migration: extract markdown from existing hand-crafted HTML pages."""

import re
import html as html_mod
from pathlib import Path
from datetime import date

WIKI_ROOT = Path(__file__).parent.parent
CONCEPTS_DIR = WIKI_ROOT / "concepts"
SOURCES_DIR = WIKI_ROOT / "sources"
SYNTHESES_DIR = WIKI_ROOT / "syntheses"

TODAY = date.today().isoformat()


def extract_hero_info(html_content: str, page_type: str) -> dict:
    """Extract frontmatter info from hero section."""
    info = {"title": "", "tags": [], "type": page_type}

    # Title from h1
    m = re.search(r'<h1>(.*?)<span>\.</span></h1>', html_content)
    if m:
        info["title"] = html_mod.unescape(m.group(1).strip())

    # Tags
    info["tags"] = re.findall(r'<span class="tag">([^<]+)</span>', html_content)

    if page_type == "concept":
        # Hero-meta: Source: ... · Updated: YYYY-MM-DD
        m = re.search(r'Updated:\s*(\d{4}-\d{2}-\d{2})', html_content)
        if m:
            info["updated"] = m.group(1)
        else:
            info["updated"] = TODAY
        m = re.search(r'Source:\s*([^·]+)', html_content)
        if m:
            info["sources"] = [m.group(1).strip()]
    elif page_type == "source":
        # Hero-sub: Author · type · date
        m = re.search(r'<p class="hero-sub">([^<]+)</p>', html_content)
        if m:
            parts = [p.strip() for p in m.group(1).split("·")]
            if len(parts) >= 1:
                info["author"] = parts[0]
            if len(parts) >= 2:
                info["source_type"] = parts[1]
            if len(parts) >= 3:
                info["source_date"] = parts[2]
        # Ingested date
        m = re.search(r'Ingested:\s*(\d{4}-\d{2}-\d{2})', html_content)
        if m:
            info["ingested"] = m.group(1)
        # Concepts (from body connections list)
        raw_concepts = re.findall(
            r'<a href="../concepts/([^"]+)" class="wiki-link">[^<]+</a>',
            html_content,
        )
        info["concepts"] = [c.replace(".html", "") for c in raw_concepts]

    return info


def strip_hero_and_footer(html_content: str) -> str:
    """Extract just the .content-area block."""
    m = re.search(
        r'<div class="content-area">\s*(.*?)\s*</div>\s*</section>',
        html_content,
        re.DOTALL,
    )
    return m.group(1) if m else ""


def html_wikilink_to_md(text: str) -> str:
    """Convert <a class="wiki-link"> to [[wikilink|display]]."""
    def _replace(m):
        href = m.group(1)
        display = html_mod.unescape(m.group(2).strip())
        # Strip .html extension and path prefix
        target = re.sub(r'\.html$', '', href)
        target = re.sub(r'^(\.\./)?(concepts/|sources/)', '', target)
        if target == display:
            return f"[[{target}]]"
        return f"[[{target}|{display}]]"
    return re.sub(
        r'<a href="([^"]+)" class="wiki-link">([^<]+)</a>',
        _replace,
        text,
    )


def html_ext_link_to_md(text: str) -> str:
    """Convert external <a target="_blank"> to [text](url)."""
    def _replace(m):
        href = m.group(1)
        display = html_mod.unescape(m.group(2).strip())
        return f"[{display}]({href})"
    return re.sub(
        r'<a href="([^"]+)" target="_blank"[^>]*>([^<]+)</a>',
        _replace,
        text,
    )


def html_body_to_markdown(body_html: str) -> str:
    """Convert content-area HTML to markdown."""
    text = body_html

    # Remove HTML comments
    text = re.sub(r'<!--.*?-->', '', text, flags=re.DOTALL)

    # Code blocks
    text = re.sub(
        r'<pre><code(?: class="language-\w+")?>(.*?)</code></pre>',
        lambda m: f"```\n{html_mod.unescape(m.group(1))}\n```",
        text,
        flags=re.DOTALL,
    )

    # Headings
    text = re.sub(r'<h2>(.*?)</h2>', lambda m: f'## {html_wikilink_to_md(html_mod.unescape(m.group(1)))}\n', text)
    text = re.sub(r'<h3>(.*?)</h3>', lambda m: f'### {html_wikilink_to_md(html_mod.unescape(m.group(1)))}\n', text)

    # Blockquotes
    text = re.sub(
        r'<blockquote>(.*?)</blockquote>',
        lambda m: "> " + html_wikilink_to_md(html_mod.unescape(m.group(1))).strip() + "\n",
        text,
        flags=re.DOTALL,
    )

    # Unordered lists
    text = re.sub(
        r'<ul>\s*(.*?)\s*</ul>',
        lambda m: _process_list_items(m.group(1), "- "),
        text,
        flags=re.DOTALL,
    )

    # Ordered lists
    text = re.sub(
        r'<ol>\s*(.*?)\s*</ol>',
        lambda m: _process_ordered_list(m.group(1)),
        text,
        flags=re.DOTALL,
    )

    text = re.sub(
        r'<table>(.*?)</table>',
        lambda m: _process_table(m.group(0)),
        text,
        flags=re.DOTALL,
    )

    # Inline formatting
    text = re.sub(r'<strong>(.*?)</strong>', r'**\1**', text)
    text = re.sub(r'<em>(.*?)</em>', r'*\1*', text)
    text = re.sub(r'<code>(.*?)</code>', r'`\1`', text)

    # Links (wikilinks first, then external)
    text = html_wikilink_to_md(text)
    text = html_ext_link_to_md(text)

    # Paragraphs: wrap remaining bare text
    text = re.sub(
        r'<p>(.*?)</p>',
        lambda m: html_wikilink_to_md(html_mod.unescape(m.group(1))) + "\n",
        text,
        flags=re.DOTALL,
    )

    # Clean up excessive whitespace
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = text.strip()

    return text


def _process_list_items(list_html: str, prefix: str) -> str:
    """Convert <li> items to markdown list."""
    items = re.findall(r'<li>(.*?)</li>', list_html, re.DOTALL)
    lines = []
    for item in items:
        text = html_mod.unescape(item.strip())
        text = re.sub(r'<strong>(.*?)</strong>', r'**\1**', text)
        text = re.sub(r'<em>(.*?)</em>', r'*\1*', text)
        text = re.sub(r'<code>(.*?)</code>', r'`\1`', text)
        text = html_wikilink_to_md(text)
        text = html_ext_link_to_md(text)
        lines.append(f"{prefix}{text}")
    return "\n".join(lines) + "\n"


def _process_ordered_list(list_html: str) -> str:
    """Convert <li> items to numbered markdown list."""
    items = re.findall(r'<li>(.*?)</li>', list_html, re.DOTALL)
    lines = []
    for i, item in enumerate(items, 1):
        text = html_mod.unescape(item.strip())
        text = re.sub(r'<strong>(.*?)</strong>', r'**\1**', text)
        text = re.sub(r'<em>(.*?)</em>', r'*\1*', text)
        text = re.sub(r'<code>(.*?)</code>', r'`\1`', text)
        text = html_wikilink_to_md(text)
        text = html_ext_link_to_md(text)
        lines.append(f"{i}. {text}")
    return "\n".join(lines) + "\n"


def _process_table(table_html: str) -> str:
    """Convert HTML table to markdown table."""
    # Extract all rows (thead + tbody)
    rows = []

    # Header row
    header_match = re.search(r'<thead>.*?<tr>(.*?)</tr>.*?</thead>', table_html, re.DOTALL)
    if header_match:
        headers = re.findall(r'<th>(.*?)</th>', header_match.group(1))
        rows.append([html_mod.unescape(h.strip()) for h in headers])

    # Body rows (only from <tbody> to avoid matching header row)
    body_matches = re.findall(r'<tbody>(.*?)</tbody>', table_html, re.DOTALL)
    body_rows = []
    for tbody in body_matches:
        body_rows.extend(re.findall(r'<tr>(.*?)</tr>', tbody, re.DOTALL))
    for row_html in body_rows:
        cells = re.findall(r'<t[dh]>(.*?)</t[dh]>', row_html, re.DOTALL)
        row = []
        for cell in cells:
            text = html_mod.unescape(cell.strip())
            text = re.sub(r'<strong>(.*?)</strong>', r'**\1**', text)
            text = re.sub(r'<em>(.*?)</em>', r'*\1*', text)
            text = re.sub(r'<code>(.*?)</code>', r'`\1`', text)
            text = html_wikilink_to_md(text)
            text = html_ext_link_to_md(text)
            row.append(text)
        if row:
            rows.append(row)

    if not rows:
        return ""

    # Build markdown table
    lines = []
    lines.append("| " + " | ".join(rows[0]) + " |")
    lines.append("| " + " | ".join("---" for _ in rows[0]) + " |")
    for row in rows[1:]:
        lines.append("| " + " | ".join(row) + " |")

    return "\n".join(lines) + "\n"


def extract_connection_cards(html_content: str, page_type: str) -> list:
    """Extract connection cards as (type, slug, description) tuples."""
    cards = []
    pattern = (
        r'<a class="connection-card" href="([^"]+)">\s*'
        r'<span class="connection-type[^"]*">([^<]+)</span>\s*'
        r'<h4>([^<]+)</h4>\s*'
        r'<p>([^<]*)</p>'
    )
    for m in re.finditer(pattern, html_content, re.DOTALL):
        href = m.group(1)
        rel_type = m.group(2).strip()
        desc = html_mod.unescape(m.group(4).strip())

        # Extract slug from href
        slug = re.sub(r'\.html$', '', href)
        slug = re.sub(r'^(\.\./)?(concepts/|sources/)', '', slug)

        cards.append((rel_type, slug, desc))
    return cards


def build_frontmatter(info: dict) -> str:
    """Build YAML frontmatter string."""
    lines = ["---"]
    if info.get("title"):
        lines.append(f'title: "{info["title"]}"')
    if info.get("type"):
        lines.append(f"type: {info['type']}")
    if info.get("tags"):
        lines.append(f"tags: [{', '.join(info['tags'])}]")
    if info.get("created"):
        lines.append(f"created: {info['created']}")
    if info.get("updated"):
        lines.append(f"updated: {info['updated']}")
    if info.get("sources"):
        lines.append(f"sources: [{', '.join(info['sources'])}]")
    if info.get("aliases"):
        lines.append(f"aliases: [{', '.join(info['aliases'])}]")

    # Source-specific
    if info.get("author"):
        lines.append(f'author: "{info["author"]}"')
    if info.get("source_type"):
        lines.append(f"source_type: {info['source_type']}")
    if info.get("source_date"):
        lines.append(f"source_date: {info['source_date']}")
    if info.get("ingested"):
        lines.append(f"ingested: {info['ingested']}")
    if info.get("concepts"):
        lines.append(f"concepts: [{', '.join(info['concepts'])}]")
    if info.get("url"):
        lines.append(f'url: "{info["url"]}"')

    lines.append("---")
    return "\n".join(lines)


def build_connections_md(cards: list) -> str:
    """Build the --- connections section for markdown."""
    if not cards:
        return ""
    lines = ["---"]
    for rel_type, slug, desc in cards:
        # Map non-standard relationship labels to script-recognized ones
        mapped_type = _map_relationship(rel_type)
        lines.append(f"- {mapped_type} [[{slug}]] — {desc}")
    return "\n".join(lines)


RELATIONSHIP_MAP = {
    "Alternative to": "Contrasts with",
    "Enables": "Supports",
    "Applied to": "Related to",
    "Applies to": "Related to",
    "Source": "Related to",
    "Core concept": "Core to",
    "Mechanism": "Foundation for",
    "Foundation": "Foundation for",
    "Related": "Related to",
    "Canonical example": "Core to",
    "Architecture": "Foundation for",
    "Built on": "Extends",
    "Built on top": "Foundation for",
    "Powered by": "Relies on",
}


def _map_relationship(label: str) -> str:
    """Map hand-crafted relationship labels to script-recognized ones."""
    return RELATIONSHIP_MAP.get(label, label)


def convert_html_to_md(html_path: Path, page_type: str) -> str:
    """Convert a single HTML page to markdown with frontmatter."""
    html_content = html_path.read_text()

    # Extract metadata
    info = extract_hero_info(html_content, page_type)
    info["created"] = info.get("updated", TODAY)

    # Extract and convert body
    body_html = strip_hero_and_footer(html_content)
    body_md = html_body_to_markdown(body_html)

    # Extract connection cards
    cards = extract_connection_cards(html_content, page_type)
    connections_md = build_connections_md(cards)

    # Assemble
    parts = [build_frontmatter(info), "", body_md]
    if connections_md:
        parts.append(connections_md)

    return "\n".join(parts) + "\n"


def main():
    print("Converting concept pages...")
    concept_files = sorted(CONCEPTS_DIR.glob("*.html"))
    for html_file in concept_files:
        slug = html_file.stem
        # Skip backup files
        if slug.endswith(".bak"):
            continue
        md_path = CONCEPTS_DIR / f"{slug}.md"
        if md_path.exists():
            print(f"  Skipping {slug}.md (already exists)")
            continue
        md_content = convert_html_to_md(html_file, "concept")
        md_path.write_text(md_content)
        print(f"  → {slug}.md")

    print("\nConverting source pages...")
    source_files = sorted(SOURCES_DIR.glob("*.html"))
    for html_file in source_files:
        slug = html_file.stem
        md_path = SOURCES_DIR / f"{slug}.md"
        if md_path.exists():
            print(f"  Skipping {slug}.md (already exists)")
            continue
        md_content = convert_html_to_md(html_file, "source")
        md_path.write_text(md_content)
        print(f"  → {slug}.md")

    print("\nDone! Run convert-to-html.py to regenerate .html files.")


if __name__ == "__main__":
    main()
