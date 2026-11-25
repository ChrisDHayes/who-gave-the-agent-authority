import base64,json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
data=json.loads((root/'data/evidence.json').read_text())
data['matrix']=json.loads((root/'data/matrix.json').read_text())
data['authority']=json.loads((root/'data/authority-comparison.json').read_text())
data['closeups']=json.loads((root/'data/closeups.json').read_text())
data['moments']=json.loads((root/'data/moments.json').read_text())
html=(root/'src/experience.html').read_text()
for marker,name in [('AUTHORITY_VIEW','authority'),('CASE_COMPARE','compare'),('CLOSEUPS','closeups'),('RESPONSES','responses')]:
    html=html.replace('/* '+marker+' */',(root/('src/'+name+'.html')).read_text())
css=(root/'src/style.css').read_text()+'\n'+(root/'src/explore.css').read_text()
js='\n'.join((root/('src/'+name+'.js')).read_text() for name in ['app','explore','links'])
payload=json.dumps(data,ensure_ascii=False,separators=(',',':')).replace('</','<\\/')
html=html.replace('/* STYLES */',css).replace('/* SCRIPT */',js.replace('/* DATA */',payload))
emblem=base64.b64encode((root/'assets/authority-aperture-v1.png').read_bytes()).decode('ascii')
html=html.replace('/* AUTHORITY_EMBLEM */','data:image/png;base64,'+emblem)
(root/'dist').mkdir(exist_ok=True)
(root/'dist/index.html').write_text(html)
(root/'index.html').write_text(html)
print(f'Built {len(html.encode()):,} bytes and {len(data["cases"])} disclosures.')
