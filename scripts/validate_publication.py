"""Check publication links, citations and portable page destinations."""
import json,re
from pathlib import Path
from urllib.parse import urlparse
from zipfile import ZipFile
from xml.etree import ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
moments=json.loads((ROOT/'data/moments.json').read_text())
aliases={m['id'] for m in moments}
refs=json.loads((ROOT/'publishing/references.json').read_text())
citations={r['citation'] for r in refs}
assert citations=={f'2026{x}' for x in 'abcdefghi'}
for name in ['essay','substack']:
    text=(ROOT/f'publishing/{name}.md').read_text()
    assert '{{' not in text and '}}' not in text
    assert set(re.findall(r'2026[a-z]',text))<=citations
    urls=re.findall(r'\]\(([^)]+)\)',text)
    links=[u for u in urls if urlparse(u).fragment in aliases]
    assert len(links)==(8 if name=='essay' else 6),(name,len(links))
    page=(ROOT/f'publishing/{name}.html').read_text()
    for path in re.findall(r'href="([^"]+)"',page):
        parsed=urlparse(path)
        if parsed.scheme:continue
        assert (ROOT/'publishing'/parsed.path).resolve().is_file(),path
        if parsed.fragment:assert parsed.fragment in aliases
    docpath=ROOT/'publishing'/f'Who_Gave_the_Agent_That_Authority_{name.title()}_Christopher_Hayes.docx'
    if docpath.exists():
        with ZipFile(docpath) as z:
            rels=ET.fromstring(z.read('word/_rels/document.xml.rels'))
            targets=[x.get('Target') for x in rels if x.get('Type','').endswith('/hyperlink')]
            assert sum(urlparse(t).fragment in aliases for t in targets)==len(links)
            assert b'pBdr' not in z.read('word/styles.xml')
assert (ROOT/'index.html').read_bytes()==(ROOT/'dist/index.html').read_bytes()
config=json.loads((ROOT/'publishing/publication.json').read_text())
ready=ROOT/'publishing/substack-ready-to-publish.md'
assert ready.exists()==bool(config.get('public_experience_url'))
print('PASS: essay and article citations, eight essay moments, six article moments, portable destinations, Word hyperlinks, clean title styles, and publication readiness state.')
