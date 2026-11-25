"""Validate evidence integrity and the portable HTML output, without fetching sources."""
import base64,collections,json,re,subprocess,tempfile
from datetime import date
from pathlib import Path

root=Path(__file__).resolve().parents[1]
data=json.loads((root/'data/evidence.json').read_text())
matrix=json.loads((root/'data/matrix.json').read_text())
cases=data['cases']; expected=[f'R{i:03}' for i in range(1,27)]+[f'N{i:03}' for i in range(1,4)]
assert [c['id'] for c in cases]==expected
assert collections.Counter(c['kind'] for c in cases)=={'report':26,'notice':3}
assert collections.Counter(c['boundary'] for c in cases)=={'Access and method':10,'Task and continuation':6,'Collaboration':4,'Evaluation and evidence':3,'Publication':3,'Oversight and stopping':2,'Unresolved':1}
for c in cases:
    assert all(c.get(k) for k in ['source','authority','task','observed','outcome','interpretation','limit'])
    assert c['source'].startswith('https://')
    for event in c['timeline']:
        assert event['disclosure_id']==c['id']
        for k in ['date_start','date_end']:
            if event[k]: date.fromisoformat(event[k])
        if event['date_start'] and event['date_end']: assert event['date_start']<=event['date_end']
        if event['date_precision']=='by': assert event['date_start'] is None and event['date_end']
    for response in c['responses']:
        assert response['disclosure_id']==c['id'] and response['source_url'].startswith('https://')
assert 4<=len(matrix['cases'])<=6
assert matrix['review_date']=='2026-11-21'
for case_id, row in matrix['cases'].items():
    assert case_id in expected
    assert all(len(row[key])==4 for key in ['states','short','events','text','sections'])
    assert all(state in matrix['definitions'] for state in row['states'])
    assert all(row[key] for key in ['source','takeaway','reading','action','note'])
    original=next(c['source'] for c in cases if c['id']==case_id)
    assert row['source'].rstrip('/').split('/')[-1]==original.rstrip('/').split('/')[-1]
assert 'Controlled experiment' in matrix['cases']['R011']['note']
assert 'non-misaligned' in matrix['cases']['R020']['note']
authority=json.loads((root/'data/authority-comparison.json').read_text())
closeups=json.loads((root/'data/closeups.json').read_text())
assert set(authority['cases'])==set(expected)
columns={x['id'] for x in authority['columns']}
assert columns=={'access','task','collaboration','evidence','publication','oversight'}
assert len(authority['columns'])==6
for c in cases:
    row=authority['cases'][c['id']]
    assert set(row['tags']).issubset(columns)
    assert set(row.get('unresolved',[])).issubset(columns)
    assert not set(row['tags']).intersection(row.get('unresolved',[]))
    assert all(isinstance(text,str) and text.strip() for text in row['tags'].values())
    assert row['source']==c['source'] and row['source_sections'] and row['followup']
    assert row['basis']==('report_reread' if c['kind']=='report' else 'collected_notice')
    if c['boundary']!='Unresolved':
        primary=next(x['id'] for x in authority['columns'] if x['theme']==c['boundary'])
        assert primary in row['tags']
assert not authority['cases']['N001']['tags']
assert authority['cases']['N001']['unresolved']==['publication']
assert 'non-misaligned' in authority['cases']['R020']['tags']['oversight']
assert 'simulated' in ' '.join(authority['cases']['R011']['tags'].values()).lower()
f=closeups['framing'];g=closeups['graders']
assert f['case_id']=='R006' and f['unit']=='percent' and f['approximate'] is True
assert [x['value'] for x in f['values']]==[10,16] and f['axis_max']==20
assert f['denominator'] is None
assert g['case_id']=='R010' and g['total']==len(g['items'])==3
assert g['accepted']==sum(x['accepted'] for x in g['items'])==2
for q in [f,g]:
    original=next(c['source'] for c in cases if c['id']==q['case_id'])
    assert q['source'].rstrip('/').split('/')[-1]==original.rstrip('/').split('/')[-1]
    assert q['qualification'] and q['section']
html=(root/'dist/index.html').read_text()
markup=re.sub(r'<script>[\s\S]*?</script>','',html)
ids=re.findall(r'\bid="([^"]+)"',markup)
assert len(ids)==len(set(ids)), 'Duplicate HTML IDs'
moments=json.loads((root/'data/moments.json').read_text())
assert len(moments)==8 and len({m['id'] for m in moments})==8
for m in moments:
    assert m['target'] in ids and m['case'] in expected
    if 'compare' in m: assert m['compare'] in expected and m['compare']!=m['case']
    if 'story' in m: assert m['story'] in range(4)
assert all(x in ids or x in {m['id'] for m in moments} for x in re.findall(r'href="#([^"]+)"',markup))
assert '/* DATA */' not in html and '/* SCRIPT */' not in html and '/* STYLES */' not in html
assert all('/* '+name+' */' not in html for name in ['AUTHORITY_EMBLEM','AUTHORITY_VIEW','CASE_COMPARE','CLOSEUPS','RESPONSES'])
embedded=re.search(r'class="emblem-art" src="data:image/png;base64,([A-Za-z0-9+/=]+)"',html)
assert embedded, 'Portable title image is missing'
assert base64.b64decode(embedded.group(1),validate=True)==(root/'assets/authority-aperture-v1.png').read_bytes()
assert not re.search(r'<script[^>]+src=|<link[^>]+rel="stylesheet"',html)
script=re.search(r'<script>([\s\S]*?)</script>',html).group(1)
with tempfile.NamedTemporaryFile(suffix='.js',mode='w') as js:
    js.write(script);js.flush();subprocess.run(['node','--check',js.name],check=True)
assert 'Five reviewed teaching examples' in html and 'remaining 24' in html
assert re.findall(r'<section[^>]+\bid="([^"]+)"',html)==['start','workaround','atlas','evidence','timing','limits','delegation','method'], 'Locked section order changed'
assert 'prefers-reduced-motion:reduce' in html
print('PASS: 29 disclosures, 29 source-mapped authority reviews, two quantitative close-ups, five checkpoint rows, category counts, date precision, locked sections, navigation, embedded image integrity, and built JavaScript syntax.')
