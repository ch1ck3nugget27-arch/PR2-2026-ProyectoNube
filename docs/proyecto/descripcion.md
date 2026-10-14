# Descripción del proyecto: NubeImg

## 1. Problema
No existe un lugar simple y propio donde subir imágenes y volver a verlas desde cualquier equipo.

## 2. Objetivo general
Desarrollar durante el semestre un sistema web que permita subir, consultar y eliminar imágenes en un almacenamiento centralizado.

## 3. Objetivos específicos
1. Implementar la subida de imágenes con validación de tipo y tamaño.
2. Mostrar una galería con las imágenes almacenadas.
3. Permitir eliminar imágenes.
4. Separar el almacenamiento en una capa propia para poder cambiar la "nube" (carpeta local → servicio real) sin reescribir la app.
5. Probar el sistema con pruebas automáticas.
6. Documentar la instalación y el uso.

## 4. Relación con Sistemas Operativos
- **Sistema de archivos:** el servidor guarda, lista y borra archivos en disco.
- **Permisos y seguridad:** nombres de archivo generados por el sistema para evitar acceder a rutas ajenas.
- **Procesos y recursos:** el servidor web es un proceso que atiende peticiones; se limita el tamaño de subida para proteger memoria y disco.
- *(El equipo puede ampliar este punto con lo visto en clase.)*

## 5. Tecnologías
Python 3, Flask, HTML/CSS, GitHub (repositorio, Issues y Projects).

## 6. Riesgos
| Riesgo | Mitigación |
|---|---|
| Subir archivos que no son imágenes | Se revisa el contenido real del archivo, no solo la extensión |
| Llenar el disco | Límite de 5 MB por imagen (futuro: cuota por usuario) |
| Integrante sin experiencia en GitHub | Tareas pequeñas y revisión entre compañeros |
