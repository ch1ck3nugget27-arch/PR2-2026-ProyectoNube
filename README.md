# PR2-2026-ProyectoNube — NubeImg

> Sistema web sencillo para subir, ver y eliminar imágenes en un almacenamiento "en la nube".

## Problema
Las personas guardan fotos en el celular, en correos y en chats, sin un lugar propio y ordenado donde subirlas y consultarlas desde cualquier dispositivo.

## Propósito y objetivo
Construir un servicio web mínimo que permita **subir imágenes a un almacenamiento centralizado** y consultarlas en una galería, aplicando conceptos de sistemas operativos (archivos, permisos, procesos del servidor y manejo de recursos).

## Usuarios
Estudiantes y personas en general que necesitan guardar imágenes de forma simple.

## Descripción general
Aplicación web hecha con Python y Flask. El usuario elige una imagen, el servidor la valida (tipo real, tamaño máximo 5 MB), le asigna un nombre único y la guarda. La galería muestra las imágenes subidas y permite eliminarlas.

## Funcionalidades del MVP
- Subir imagen (PNG, JPG, GIF, WEBP, máx. 5 MB)
- Ver galería
- Abrir una imagen
- Eliminar una imagen
- Listado en JSON (`/api/imagenes`)

Fuera del alcance por ahora: cuentas de usuario, carpetas, compartir enlaces, nube real (S3/Drive). Ver [`docs/requisitos`](docs/requisitos/requisitos.md).

## Cómo ejecutarlo
```bash
cd PR2-2026-ProyectoNube
python -m venv .venv
source .venv/bin/activate        # En Windows: .venv\Scripts\activate
pip install -r requirements.txt
python src/run.py
```
Abre http://127.0.0.1:5000

Pruebas automáticas:
```bash
python -m unittest discover -s tests -v
```

## Estructura del repositorio
```
├── README.md
├── requirements.txt
├── docs/
│   ├── proyecto/        descripción del proyecto
│   ├── requisitos/      requisitos y alcance (MVP)
│   ├── planificacion/   cronograma (Gantt) e Issues propuestas
│   ├── presentaciones/  presentación del proyecto
│   └── auditoria/       cuestionario de madurez y tabla de acciones
├── equipo/              un .txt por integrante
├── src/                 código fuente (nubeimg/ = la aplicación)
└── tests/               pruebas automáticas
```

## Equipo
Ver carpeta [`equipo/`](equipo/).

| Integrante | Rol |
|---|---|
| Nombre Apellido | (completar) |
| Nombre Apellido | (completar) |

## Estado actual
🟡 MVP funcional de base creado. Pendiente: auditoría de madurez y checkpoint del docente.
