"""Create the portable GitHub package from an explicit allowlist."""
import argparse,hashlib,json,zipfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',required=True);args=parser.parse_args()
    out=Path(args.output).resolve();out.parent.mkdir(parents=True,exist_ok=True)
    paths=[ROOT/name for name in ['index.html','.nojekyll','README.md','DECISIONS.md','VALIDATION.md','requirements-documents.txt']]
    for folder in ['src','data','assets','scripts','research','publishing']:
        paths.extend(p for p in (ROOT/folder).rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.pyc')
    paths=sorted(set(paths))
    manifest={'edition':'1.5','public_deployment':'Not configured','files':[]}
    with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        for p in paths:
            relative=p.relative_to(ROOT).as_posix();data=p.read_bytes()
            assert '.openai/' not in relative and '.git/' not in relative
            z.writestr(relative,data)
            manifest['files'].append({'path':relative,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
        z.writestr('PACKAGE_MANIFEST.json',json.dumps(manifest,indent=2)+'\n')
    with zipfile.ZipFile(out) as z:
        assert z.testzip() is None
        for item in manifest['files']:
            assert hashlib.sha256(z.read(item['path'])).hexdigest()==item['sha256']
    print(json.dumps({'path':str(out),'files':len(paths)+1,'bytes':out.stat().st_size,'sha256':hashlib.sha256(out.read_bytes()).hexdigest()}))
if __name__=='__main__':main()
