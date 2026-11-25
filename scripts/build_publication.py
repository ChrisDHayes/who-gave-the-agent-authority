"""Build portable reading pages and Markdown. Python standard library only.

Set public_experience_url in publishing/publication.json after public hosting is
verified. Until then HTML/Markdown use relative links and no Substack export is
labelled ready to publish. DOCX review copies may use the existing private Site.
"""
import html, json, re, shutil
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
CONFIG = json.loads((ROOT/'publishing/publication.json').read_text())
REFS = json.loads((ROOT/'publishing/references.json').read_text())
BASE = 'https://openai.com/safety-alignment/misalignment-reports/'
for ref in REFS:
    ref['url'] = BASE + ref['slug'] + '/'

def reference(ref):
    return f"OpenAI. ({ref['citation']}, {ref['date']}). *{ref['title']}*. [{ref['url']}]({ref['url']})"

def render_markdown(name, experience):
    value = (ROOT/f'publishing/source/{name}.md').read_text()
    replacements = {r['id']:r['url'] for r in REFS}
    replacements.update(experience=experience,
        references='\n\n'.join(reference(r) for r in REFS),
        substack_references='\n\n'.join(reference(r) for r in REFS if r['substack']))
    for key, text in replacements.items():
        value = value.replace('{{'+key+'}}', text)
    assert '{{' not in value, 'Unresolved publication token'
    return value

# Small deliberate renderer for this project's authored Markdown subset.
INLINE = re.compile(r'\[([^\]]+)\]\(([^)]+)\)|\*\*(.+?)\*\*|\*([^*]+)\*')
def inline(text):
    out=[]; end=0
    for match in INLINE.finditer(text):
        out.append(html.escape(text[end:match.start()]))
        if match.group(1) is not None:
            out.append(f'<a href="{html.escape(match.group(2),quote=True)}">{inline(match.group(1))}</a>')
        elif match.group(3) is not None:
            out.append('<strong>'+inline(match.group(3))+'</strong>')
        else:
            out.append('<em>'+html.escape(match.group(4))+'</em>')
        end=match.end()
    return ''.join(out)+html.escape(text[end:])

def blocks(text):
    for chunk in re.split(r'\n\s*\n',text.strip()):
        if chunk.startswith('|'):
            rows=[[c.strip() for c in line.strip().strip('|').split('|')] for line in chunk.splitlines()]
            yield ('table', [rows[0]]+rows[2:])
        elif re.match(r'^#{1,6} ',chunk):
            marker,value=chunk.split(' ',1)
            yield (f'h{len(marker)}',value)
        else:
            yield ('p',chunk.replace('\n',' '))

def render_html(name, text):
    out=[]
    for kind,value in blocks(text):
        if kind=='table':
            header='<tr>'+''.join('<th scope="col">'+inline(v)+'</th>' for v in value[0])+'</tr>'
            body=''.join('<tr>'+''.join('<td>'+inline(v)+'</td>' for v in row)+'</tr>' for row in value[1:])
            out.append('<div class="table-wrap" tabindex="0" role="region" aria-label="Delegation specification"><table><thead>'+header+'</thead><tbody>'+body+'</tbody></table></div>')
        else:
            out.append(f'<{kind}>{inline(value)}</{kind}>')
    other='substack' if name=='essay' else 'essay'
    label='Companion article' if name=='essay' else 'Research essay'
    return '''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>'''+html.escape(CONFIG['title'])+(' · Essay' if name=='essay' else ' · Article')+'''</title>
<style>
:root{color-scheme:light dark;--bg:#fafbf9;--ink:#173038;--muted:#46616a;--line:#cbd8d9;--link:#086477}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:19px/1.72 Georgia,serif}main{max-width:800px;margin:auto;padding:52px 28px 80px}nav{font:15px/1.5 system-ui;display:flex;flex-wrap:wrap;gap:12px 24px;margin:0 0 58px}a{color:var(--link);text-underline-offset:4px;overflow-wrap:anywhere}a:hover{text-decoration-thickness:2px}a:focus-visible{outline:3px solid var(--link);outline-offset:5px}h1{font-size:clamp(34px,5vw,49px);line-height:1.1;letter-spacing:-.025em;margin:0 0 18px}h2{font:22px/1.4 system-ui;margin:0 0 24px;color:var(--muted)}h3{font:700 25px/1.3 system-ui;margin:44px 0 16px}p{margin:0 0 22px}h2+p{font:15px/1.5 system-ui;margin-bottom:35px}p:has(>strong:only-child){font:600 17px/1.6 system-ui;margin:28px 0}.table-wrap{overflow:auto;margin:25px 0}table{border-collapse:collapse;font:15px/1.55 system-ui;min-width:620px}th,td{padding:14px 13px;text-align:left;vertical-align:top;border-bottom:1px solid var(--line)}th{background:#e6edef}footer{border-top:1px solid var(--line);margin-top:48px;padding-top:20px;font:14px/1.6 system-ui;color:var(--muted)}
@media(prefers-color-scheme:dark){:root{--bg:#13252c;--ink:#edf2ef;--muted:#beced0;--line:#486169;--link:#9edce6}th{background:#233b44}}
@media(max-width:550px){body{font-size:18px}main{padding:30px 22px 60px}nav{margin-bottom:38px}h3{font-size:23px}}
@media print{nav{display:none}main{padding:0;max-width:none}body{color:#111;background:white;font-size:11pt}a{color:#111}h3{break-after:avoid}tr{break-inside:avoid}}
</style></head><body><main><nav aria-label="Publication"><a href="../index.html">Explore the experience</a><a href="'''+other+'''.html">'''+label+'''</a></nav><article>'''+''.join(out)+'''</article><footer>Christopher Hayes · November 2026 · Evidence snapshot and analytical limits are described in the source notes.</footer></main></body></html>'''

def main():
    public=CONFIG.get('public_experience_url')
    if public:
        parsed=urlparse(public)
        assert parsed.scheme=='https' and parsed.netloc and not parsed.query and not parsed.fragment
    destination=public or '../index.html'
    for name in ['essay','substack']:
        text=render_markdown(name,destination)
        (ROOT/f'publishing/{name}.md').write_text(text)
        # Reading pages deliberately remain portable across hosts and folders.
        (ROOT/f'publishing/{name}.html').write_text(render_html(name,render_markdown(name,'../index.html')))
        print(name, len(re.findall(r'\b[\w\u2019-]+\b',text.split('### References')[0].split('### Sources')[0])), 'words before references')
    target=ROOT/'publishing/substack-ready-to-publish.md'
    if public:
        target.write_text(render_markdown('substack',public))
    elif target.exists():
        target.unlink()
    (ROOT/'dist/publishing').mkdir(parents=True,exist_ok=True)
    for name in ['essay.html','substack.html']:
        shutil.copy2(ROOT/'publishing'/name,ROOT/'dist/publishing'/name)
    print('Public Substack export:', 'ready' if public else 'pending verified public URL')

if __name__=='__main__': main()
