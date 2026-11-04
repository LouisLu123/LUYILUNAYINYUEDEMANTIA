from pathlib import Path
import re,json,base64,zipfile
P=Path(__file__).resolve().parent
# Bundle a single file: local HTML needs no server, network, fetch or CDN.
assets={f.name:'data:image/'+('jpeg' if f.suffix in ['.jpg','.jpeg'] else 'png')+';base64,'+base64.b64encode(f.read_bytes()).decode() for f in (P/'assets').iterdir() if f.is_file() and f.name!='brain-hero.png'}
app=(P/'app.js').read_text()
app=app.replace("(()=>{'use strict';","(()=>{'use strict';\nconst assetURL=name=>window.EMBEDDED_ASSETS?.[name]||'assets/'+name;")
app=app.replace("img.src='assets/'+sceneFiles[next]","img.src=assetURL(sceneFiles[next])").replace(".src='assets/'+name",".src=assetURL(name)").replace("img.src='assets/'+file","img.src=assetURL(file)")
s=(P/'index.html').read_text()
s=re.sub(r'<link rel="preload"[^>]+>', '',s)
s=s.replace('<link rel="stylesheet" href="styles.css">','<style>'+(P/'styles.css').read_text()+'</style>')
for name,uri in assets.items():s=s.replace('assets/'+name,uri)
s=s.replace('<script src="vendor/gsap.min.js"></script>','<script>'+(P/'vendor/gsap.min.js').read_text().replace('</script','<\\/script')+'</script>')
s=s.replace('<script src="motion-polish.js"></script>','<script>'+(P/'motion-polish.js').read_text().replace('</script','<\\/script')+'</script>')
s=s.replace('<script src="engine.js"></script>','<script>'+(P/'engine.js').read_text()+'</script>')
s=s.replace('<script src="app.js"></script>','<script>window.EMBEDDED_ASSETS='+json.dumps(assets)+';</script><script>'+app.replace('</script','<\\/script')+'</script>')
for filename in ['Dementia-Keynote.html','Dementia-Cinematic.html','Dementia-Keynote-Revised.html']:
 (P/filename).write_text(s)
print('Self-contained HTML:',len(s),'characters;',len(assets),'embedded source assets')
