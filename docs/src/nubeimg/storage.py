"""Capa de almacenamiento de NubeImg.

La app NO sabe dónde se guardan las imágenes: solo habla con esta clase.
Hoy guarda en una carpeta del servidor (simula la "nube").
Mañana se puede crear otra clase con los mismos métodos (por ejemplo S3Storage
o DriveStorage) sin tocar el resto del programa.
"""
import re
import uuid
from datetime import datetime
from pathlib import Path

# Nombre generado por nosotros: 32 caracteres hexadecimales + extensión.
NOMBRE_VALIDO = re.compile(r"^[0-9a-f]{32}\.(png|jpg|gif|webp)$")


class LocalStorage:
    def __init__(self, carpeta):
        self.carpeta = Path(carpeta)
        self.carpeta.mkdir(parents=True, exist_ok=True)

    def guardar(self, archivo, extension):
        """Guarda el archivo con un nombre único y devuelve ese nombre."""
        nombre = f"{uuid.uuid4().hex}.{extension}"
        archivo.save(self.carpeta / nombre)
        return nombre

    def listar(self):
        """Devuelve las imágenes, de la más nueva a la más vieja."""
        items = []
        for ruta in self.carpeta.iterdir():
            if NOMBRE_VALIDO.match(ruta.name):
                info = ruta.stat()
                items.append({
                    "nombre": ruta.name,
                    "kb": round(info.st_size / 1024, 1),
                    "fecha": datetime.fromtimestamp(info.st_mtime).strftime("%d/%m/%Y %H:%M"),
                    "_t": info.st_mtime,
                })
        items.sort(key=lambda i: i["_t"], reverse=True)
        for i in items:
            del i["_t"]
        return items

    def ruta(self, nombre):
        """Ruta real del archivo, o None si el nombre no es válido o no existe."""
        if not NOMBRE_VALIDO.match(nombre):
            return None
        ruta = self.carpeta / nombre
        return ruta if ruta.is_file() else None

    def borrar(self, nombre):
        ruta = self.ruta(nombre)
        if ruta is None:
            return False
        ruta.unlink()
        return True
