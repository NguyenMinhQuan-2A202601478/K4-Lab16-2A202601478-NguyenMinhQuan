import os
import re
import requests
from bs4 import BeautifulSoup
import json

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

RAW_DIR = os.path.join(os.path.dirname(__file__), 'Raw')
CLEAN_DIR = os.path.join(os.path.dirname(__file__), 'Clean')
SOURCE_LINK_FILE = os.path.join(RAW_DIR, 'source_link.md')

os.makedirs(RAW_DIR, exist_ok=True)
os.makedirs(CLEAN_DIR, exist_ok=True)

def read_source_links():
    links = []
    if os.path.exists(SOURCE_LINK_FILE):
        with open(SOURCE_LINK_FILE, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line.startswith('http://') or line.startswith('https://'):
                    links.append(line)
    return links

def fetch_url(url):
    print(f"Fetching: {url}")
    response = requests.get(url, headers=HEADERS, timeout=30)
    response.raise_for_status()
    return response.text

def crawl_wikipedia(url):
    html = fetch_url(url)
    
    # Save raw HTML
    raw_html_path = os.path.join(RAW_DIR, 'wikipedia_adobe_photoshop.html')
    with open(raw_html_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Saved raw HTML to {raw_html_path}")

    soup = BeautifulSoup(html, 'html.parser')
    
    # Find Version history section and tables
    version_history_data = []
    
    tables = soup.find_all('table', class_='wikitable')
    print(f"Found {len(tables)} wikitables on Wikipedia page")
    
    # Parse wikitables for version history
    parsed_tables = []
    for idx, table in enumerate(tables):
        rows = table.find_all('tr')
        table_data = []
        headers = []
        for tr in rows:
            th_tags = tr.find_all(['th'])
            if th_tags and not headers:
                headers = [th.get_text(strip=True) for th_tags_item in th_tags for th in [th_tags_item]]
                continue
            
            td_tags = tr.find_all(['td', 'th'])
            if td_tags:
                row_vals = [td.get_text(strip=True) for td in td_tags]
                table_data.append(row_vals)
        
        parsed_tables.append({
            'table_index': idx + 1,
            'headers': headers,
            'rows': table_data
        })

    # Extract text under Version history header
    version_history_section = ""
    vh_header = soup.find(id=re.compile(r'Version_history|History', re.IGNORECASE))
    if vh_header:
        parent_h = vh_header.find_parent(['h2', 'h3'])
        if parent_h:
            curr = parent_h.find_next_sibling()
            while curr and curr.name not in ['h2']:
                version_history_section += curr.get_text() + "\n"
                curr = curr.find_next_sibling()

    # Save parsed data to JSON and Markdown in Raw folder
    wiki_json_path = os.path.join(RAW_DIR, 'wikipedia_version_history.json')
    with open(wiki_json_path, 'w', encoding='utf-8') as f:
        json.dump({
            'source_url': url,
            'version_history_text': version_history_section.strip(),
            'tables': parsed_tables
        }, f, ensure_ascii=False, indent=2)
    print(f"Saved Wikipedia parsed JSON to {wiki_json_path}")

    # Save Markdown formatted table in Raw
    wiki_md_path = os.path.join(RAW_DIR, 'wikipedia_version_history.md')
    with open(wiki_md_path, 'w', encoding='utf-8') as f:
        f.write(f"# Wikipedia - Adobe Photoshop Version History\n\n")
        f.write(f"Source: {url}\n\n")
        
        for t in parsed_tables:
            f.write(f"### Table {t['table_index']}\n\n")
            if t['headers']:
                f.write("| " + " | ".join(t['headers']) + " |\n")
                f.write("| " + " | ".join(["---"] * len(t['headers'])) + " |\n")
            for row in t['rows']:
                f.write("| " + " | ".join(row) + " |\n")
            f.write("\n")
            
    print(f"Saved Wikipedia parsed Markdown to {wiki_md_path}")
    return parsed_tables

def crawl_adobe_release_notes(url):
    html = fetch_url(url)
    
    # Save raw HTML
    raw_html_path = os.path.join(RAW_DIR, 'adobe_photoshop_release_notes.html')
    with open(raw_html_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Saved raw HTML to {raw_html_path}")

    soup = BeautifulSoup(html, 'html.parser')
    
    # Extract main content text and structure
    content_div = soup.find('div', class_=re.compile(r'main-content|content|root|page', re.IGNORECASE)) or soup.body
    
    # Extract sections, headers, tables, lists
    release_notes_text = content_div.get_text(separator='\n', strip=True) if content_div else ""
    
    # Extract headers and content blocks
    blocks = []
    headers_and_paragraphs = soup.find_all(['h1', 'h2', 'h3', 'h4', 'table', 'ul', 'ol', 'p'])
    for elem in headers_and_paragraphs:
        if elem.name in ['h1', 'h2', 'h3', 'h4']:
            blocks.append({'type': 'header', 'level': elem.name, 'text': elem.get_text(strip=True)})
        elif elem.name == 'table':
            rows = elem.find_all('tr')
            tbl = []
            for tr in rows:
                cols = [td.get_text(strip=True) for td in tr.find_all(['td', 'th'])]
                if cols:
                    tbl.append(cols)
            blocks.append({'type': 'table', 'data': tbl})
        elif elem.name in ['ul', 'ol']:
            items = [li.get_text(strip=True) for li in elem.find_all('li')]
            blocks.append({'type': 'list', 'items': items})
        elif elem.name == 'p':
            txt = elem.get_text(strip=True)
            if txt:
                blocks.append({'type': 'paragraph', 'text': txt})

    # Save to JSON
    adobe_json_path = os.path.join(RAW_DIR, 'adobe_release_notes.json')
    with open(adobe_json_path, 'w', encoding='utf-8') as f:
        json.dump({
            'source_url': url,
            'blocks': blocks
        }, f, ensure_ascii=False, indent=2)
    print(f"Saved Adobe release notes JSON to {adobe_json_path}")

    # Save to Markdown
    adobe_md_path = os.path.join(RAW_DIR, 'adobe_release_notes.md')
    with open(adobe_md_path, 'w', encoding='utf-8') as f:
        f.write(f"# Adobe Photoshop Desktop Release Notes\n\n")
        f.write(f"Source: {url}\n\n")
        
        for b in blocks:
            if b['type'] == 'header':
                level_prefix = '#' * int(b['level'][1])
                f.write(f"\n{level_prefix} {b['text']}\n\n")
            elif b['type'] == 'paragraph':
                f.write(f"{b['text']}\n\n")
            elif b['type'] == 'list':
                for item in b['items']:
                    f.write(f"- {item}\n")
                f.write("\n")
            elif b['type'] == 'table':
                for r in b['data']:
                    f.write("| " + " | ".join(r) + " |\n")
                f.write("\n")

    print(f"Saved Adobe release notes Markdown to {adobe_md_path}")
    return blocks

def main():
    links = read_source_links()
    print(f"Found links in source_link.md: {links}")
    
    for link in links:
        if 'wikipedia.org' in link:
            crawl_wikipedia(link)
        elif 'adobe.com' in link:
            crawl_adobe_release_notes(link)
        else:
            print(f"Unknown link pattern: {link}")

if __name__ == '__main__':
    main()
