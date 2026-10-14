# Requisitos y alcance

## Requisitos funcionales (MVP)
| ID | Requisito | Estado |
|---|---|---|
| RF-01 | El usuario puede subir una imagen PNG, JPG, GIF o WEBP | ✅ |
| RF-02 | El sistema rechaza archivos que no son imágenes | ✅ |
| RF-03 | El sistema rechaza imágenes de más de 5 MB | ✅ |
| RF-04 | El usuario ve una galería con sus imágenes | ✅ |
| RF-05 | El usuario puede abrir una imagen | ✅ |
| RF-06 | El usuario puede eliminar una imagen | ✅ |
| RF-07 | Existe un listado en JSON de las imágenes | ✅ |

## Requisitos no funcionales
- Funciona en un navegador moderno, también en celular.
- Los nombres de archivo no pueden provocar acceso a otras carpetas.
- Se instala con un solo comando (`pip install -r requirements.txt`).

## Fuera del alcance (versión actual)
Cuentas de usuario, carpetas/álbumes, compartir enlaces, miniaturas, nube real (S3, Drive).

## Posibles mejoras (segunda etapa)
1. Inicio de sesión y galería por usuario.
2. `S3Storage` o similar usando la misma interfaz de `storage.py`.
3. Miniaturas y paginación.
