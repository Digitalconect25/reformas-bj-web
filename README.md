# Reformas BJ

Web estática de Reformas BJ para Alicante y alrededores, preparada para GitHub y Vercel.

## Contenido

- Inicio y galería de Obras con cinco proyectos y 31 fotografías.
- Ocho páginas de servicios, con imágenes ilustrativas, contenido específico y enlaces de consulta.
- Teléfono y WhatsApp: +34 613 130 991.
- Dirección: Rigoberto Ferrer 22, Bajo. Alicante.
- Enlaces legales, imágenes WebP adaptables y navegación para móvil.

## Despliegue en Vercel

Importar este repositorio y utilizar:

| Ajuste | Valor |
| --- | --- |
| Rama | main |
| Framework | Other |
| Root Directory | raíz del repositorio |
| Build Command | vacío |
| Output Directory | dist |

El archivo `vercel.json` configura la carpeta pública `dist`. No se necesitan dependencias ni variables de entorno para mostrar la web. El formulario abre WhatsApp con un mensaje preparado; no envía datos a un servidor propio.

## Contacto y perfiles

Editar `dist/config.js`. Los iconos de Google, Instagram, Facebook y correo se activan al introducir sus enlaces HTTPS y el correo real. No hay cuentas inventadas ni enlaces a perfiles ajenos.

## Dominio y buscadores

Cuando exista dominio definitivo, ejecutar antes de subir la actualización:

```bash
python3 configurar_dominio.py https://DOMINIO-REAL
```

Esto actualiza las direcciones canonical, los datos estructurados, `robots.txt`, `llms.txt` y el sitemap de las diez páginas. Verificar después el dominio en Google Search Console y enviar `/sitemap.xml`.

La web incluye datos estructurados de negocio y servicios. No se garantiza indexación, posicionamiento ni recomendaciones de sistemas de IA.

## Datos por completar

Nombre fiscal o razón social del titular, NIF, correo electrónico, datos registrales si corresponden y detalles del alojamiento definitivo. Revisar los textos legales con esos datos antes de la publicación final.

## Comprobaciones realizadas

Enlaces internos y retorno a Servicios, existencia de imágenes y tamaños adaptables, títulos únicos, sintaxis JavaScript y generación aislada del sitemap de diez páginas. Queda pendiente la comprobación visual en el alojamiento definitivo.

La vista descargable `ABRIR_REFORMAS_BJ.html` está excluida del repositorio: Vercel sirve directamente las páginas independientes de `dist`.
