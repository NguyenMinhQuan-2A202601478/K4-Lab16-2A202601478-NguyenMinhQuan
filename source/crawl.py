import os
import re
import json
import urllib.request
from bs4 import BeautifulSoup

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RAW_DIR = os.path.join(BASE_DIR, 'Raw')
CLEAN_DIR = os.path.join(BASE_DIR, 'Clean')
SOURCE_LINK_FILE = os.path.join(RAW_DIR, 'source_link.md')

os.makedirs(RAW_DIR, exist_ok=True)
os.makedirs(CLEAN_DIR, exist_ok=True)

def get_links():
    links = []
    if os.path.exists(SOURCE_LINK_FILE):
        with open(SOURCE_LINK_FILE, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line.startswith('http://') or line.startswith('https://'):
                    links.append(line)
    return links

def fetch_url(url):
    print(f"Fetching URL: {url}")
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode('utf-8', errors='ignore')

def process_wikipedia(url):
    html_path = os.path.join(RAW_DIR, 'wikipedia_adobe_photoshop.html')
    if not os.path.exists(html_path) or os.path.getsize(html_path) < 1000:
        try:
            html = fetch_url(url)
            with open(html_path, 'w', encoding='utf-8') as f:
                f.write(html)
            print(f"Downloaded raw Wikipedia HTML ({len(html)} bytes)")
        except Exception as e:
            print(f"Error fetching Wikipedia URL: {e}")
            return
    else:
        with open(html_path, 'r', encoding='utf-8') as f:
            html = f.read()
        print(f"Loaded existing Wikipedia HTML ({len(html)} bytes)")

    soup = BeautifulSoup(html, 'html.parser')
    body = soup.find(id='bodyContent') or soup

    in_vh = False
    vh_items = []

    # Parse headings and elements inside Version history
    for elem in body.find_all(['div', 'p', 'ul', 'ol', 'table']):
        classes = elem.get('class', [])
        classes_str = ' '.join(classes) if classes else ''

        if 'mw-heading' in classes_str:
            heading_text = elem.get_text(strip=True)
            if 'Version history' in heading_text:
                in_vh = True
                vh_items.append({'type': 'h2', 'text': heading_text})
            elif 'mw-heading2' in classes_str and in_vh:
                in_vh = False
                break
            elif in_vh:
                vh_items.append({'type': 'h3', 'text': heading_text})
        elif in_vh:
            if elem.name == 'p':
                t = elem.get_text(strip=True)
                if t:
                    vh_items.append({'type': 'p', 'text': t})
            elif elem.name in ['ul', 'ol']:
                items = [li.get_text(strip=True) for li in elem.find_all('li', recursive=False)]
                if items:
                    vh_items.append({'type': 'list', 'items': items})
            elif elem.name == 'table' and 'infobox' not in classes_str:
                rows = []
                for tr in elem.find_all('tr'):
                    cols = [td.get_text(strip=True) for td in tr.find_all(['td', 'th'])]
                    if cols:
                        rows.append(cols)
                if rows:
                    vh_items.append({'type': 'table', 'rows': rows})

    # Save to JSON
    json_path = os.path.join(RAW_DIR, 'wikipedia_version_history.json')
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump({
            'source_url': url,
            'items': vh_items
        }, f, ensure_ascii=False, indent=2)

    # Save to Markdown
    md_path = os.path.join(RAW_DIR, 'wikipedia_version_history.md')
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write('# Wikipedia - Adobe Photoshop Version History\n\n')
        f.write(f'Source: {url}\n\n')
        for item in vh_items:
            if item['type'] == 'h2':
                f.write(f"## {item['text']}\n\n")
            elif item['type'] == 'h3':
                f.write(f"### {item['text']}\n\n")
            elif item['type'] == 'p':
                f.write(f"{item['text']}\n\n")
            elif item['type'] == 'list':
                for li in item['items']:
                    f.write(f"- {li}\n")
                f.write('\n')
            elif item['type'] == 'table':
                for r in item['rows']:
                    f.write('| ' + ' | '.join(r) + ' |\n')
                f.write('\n')

    print(f"Extracted {len(vh_items)} Version History blocks from Wikipedia into wikipedia_version_history.md and .json")

def process_adobe_release_notes(url):
    html_path = os.path.join(RAW_DIR, 'adobe_photoshop_release_notes.html')
    md_path = os.path.join(RAW_DIR, 'adobe_release_notes.md')

    if not os.path.exists(html_path) or os.path.getsize(html_path) < 1000:
        try:
            html = fetch_url(url)
            with open(html_path, 'w', encoding='utf-8') as f:
                f.write(html)
            print(f"Downloaded raw Adobe release notes HTML ({len(html)} bytes)")
        except Exception as e:
            print(f"Error fetching Adobe release notes: {e}")

    # Ensure adobe_release_notes.md exists
    if os.path.exists(md_path):
        with open(md_path, 'r', encoding='utf-8') as f:
            md_content = f.read()
        print(f"Loaded existing Adobe release notes MD ({len(md_content)} bytes)")
    else:
        md_content = f"Source: {url}\n"

    # Also generate structured JSON
    json_path = os.path.join(RAW_DIR, 'adobe_release_notes.json')
    
    # Parse version blocks from md_content or html
    version_blocks = []
    current_version = None
    lines = md_content.splitlines()
    for line in lines:
        line_s = line.strip()
        if re.search(r'Photoshop|version|\b202[0-6]\b|\b25\.\d+|\b26\.\d+', line_s, re.IGNORECASE) and (line_s.startswith('#') or line_s.startswith('**')):
            current_version = line_s
            version_blocks.append({'version_header': current_version, 'content': []})
        elif current_version and line_s:
            if version_blocks:
                version_blocks[-1]['content'].append(line_s)

    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump({
            'source_url': url,
            'total_lines': len(lines),
            'version_blocks_count': len(version_blocks),
            'sample_blocks': version_blocks[:20]
        }, f, ensure_ascii=False, indent=2)

    print(f"Saved Adobe release notes JSON structure to {json_path}")

def generate_clean_summary():
    # Combine key timeline events into source/Clean/photoshop_version_timeline.json and .md
    wiki_json_path = os.path.join(RAW_DIR, 'wikipedia_version_history.json')
    clean_timeline_path = os.path.join(CLEAN_DIR, 'photoshop_version_timeline.md')
    
    milestones = []
    if os.path.exists(wiki_json_path):
        with open(wiki_json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            items = data.get('items', [])
            
            curr_heading = ""
            for item in items:
                if item['type'] in ['h2', 'h3']:
                    curr_heading = item['text']
                elif item['type'] == 'p':
                    text = item['text']
                    date_match = re.search(r'\b(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{4}\b|\b\d{4}\b', text)
                    if date_match:
                        milestones.append({
                            'heading': curr_heading,
                            'text': text,
                            'date_approx': date_match.group(0)
                        })
                        
    with open(clean_timeline_path, 'w', encoding='utf-8') as f:
        f.write("# Cleaned Photoshop Version Timeline\n\n")
        f.write("| Version / Milestone | Approx Date | Highlights / Key Features |\n")
        f.write("| --- | --- | --- |\n")
        for m in milestones:
            heading = m['heading'].replace('|', '-')
            date = m['date_approx']
            snippet = m['text'][:150].replace('\n', ' ').replace('|', '-') + '...'
            f.write(f"| {heading} | {date} | {snippet} |\n")
            
    print(f"Generated clean timeline summary in {clean_timeline_path}")

def main():
    links = get_links()
    print(f"Target links from source_link.md: {links}")
    for link in links:
        if 'wikipedia.org' in link:
            process_wikipedia(link)
        elif 'adobe.com' in link:
            process_adobe_release_notes(link)
    
    generate_clean_summary()

if __name__ == '__main__':
    main()
