from pathlib import Path
from urllib.parse import urlparse,urljoin
from xml.sax.saxutils import escape
import re,sys,json
root=Path(__file__).parent/'dist'
if len(sys.argv)!=2:raise SystemExit('Uso: python3 configurar_dominio.py https://tudominio.es')
domain=sys.argv[1].rstrip('/');parsed=urlparse(domain)
if parsed.scheme!='https' or not parsed.netloc or parsed.path or parsed.query or parsed.fragment:raise SystemExit('Introduce el dominio HTTPS, sin rutas.')
urls=[]
def absolute(value):
 if isinstance(value,dict):
  return {k:(urljoin(domain+'/',v) if k in ['@id','url','image','item'] and isinstance(v,str) and not v.startswith(('https:','http:')) else absolute(v)) for k,v in value.items()}
 if isinstance(value,list):return [absolute(v) for v in value]
 return value
for p in sorted(root.glob('*.html')):
 url=domain+('/' if p.name=='index.html' else '/'+p.name);urls.append(url);s=p.read_text()
 s=re.sub(r'<link rel="canonical"[^>]*>','',s);s=re.sub(r'<meta property="og:url"[^>]*>','',s)
 s=s.replace('</head>',f'<link rel="canonical" href="{escape(url)}"><meta property="og:url" content="{escape(url)}"></head>')
 def structured(m):
  obj=absolute(json.loads(m.group(1)));nodes=obj.get('@graph',[obj])
  for node in nodes:
   if node.get('@type')=='HomeAndConstructionBusiness':node.update({'url':domain+'/','image':domain+'/img/logo-reformas-bj.webp'})
   if node.get('@type')=='Service':node['url']=url
  return '<script type="application/ld+json">'+json.dumps(obj,ensure_ascii=False)+'</script>'
 s=re.sub(r'<script type="application/ld\+json">(.*?)</script>',structured,s,flags=re.S);p.write_text(s)
(root/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join('<url><loc>'+escape(url)+'</loc></url>' for url in urls)+'</urlset>')
(root/'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: '+domain+'/sitemap.xml\n')
p=root/'llms.txt';s=p.read_text();s=re.sub(r'\]\(\./([^)]*)\)',lambda m:']('+domain+'/'+m.group(1)+')',s);p.write_text(s)
print('Dominio configurado. Sitemap con',len(urls),'páginas y direcciones canonical completas.')
