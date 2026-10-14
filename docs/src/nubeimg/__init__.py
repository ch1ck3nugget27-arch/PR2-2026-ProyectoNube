"""NubeImg: pequeño sistema para subir imágenes a una "nube"."""
from pathlib import Path

from flask import (Flask, flash, jsonify, redirect, render_template,
                   request, send_from_directory, url_for)

from .storage import LocalStorage

# Tipo de imagen -> firma real del archivo (primeros bytes).
# Revisamos esto para no confiar solo en el nombre que trae el archivo.
FIRMAS = {
    "png": (b"\x89PNG\r\n\x1a\n",),
    "jpg": (b"\xff\xd8\xff",),
    "gif": (b"GIF87a", b"GIF89a"),
}
EXTENSIONES_PERMITIDAS = {"png", "jpg", "jpeg", "gif", "webp"}


def detectar_tipo(archivo):
    """Mira los primeros bytes y devuelve 'png', 'jpg', 'gif', 'webp' o None."""
    cabecera = archivo.read(12)
    archivo.seek(0)
    for tipo, firmas in FIRMAS.items():
        if any(cabecera.startswith(f) for f in firmas):
            return tipo
    if cabecera[:4] == b"RIFF" and cabecera[8:12] == b"WEBP":
        return "webp"
    return None


def create_app(config=None):
    app = Flask(__name__)
    app.config.update(
        SECRET_KEY="cambiar-en-produccion",
        MAX_CONTENT_LENGTH=5 * 1024 * 1024,  # 5 MB
        CARPETA_NUBE=str(Path(__file__).resolve().parents[1] / "uploads"),
    )
    if config:
        app.config.update(config)

    nube = LocalStorage(app.config["CARPETA_NUBE"])

    @app.get("/")
    def galeria():
        return render_template("index.html", imagenes=nube.listar())

    @app.post("/subir")
    def subir():
        archivo = request.files.get("imagen")
        if archivo is None or archivo.filename == "":
            flash("Elige una imagen antes de subir.", "error")
            return redirect(url_for("galeria"))

        extension = archivo.filename.rsplit(".", 1)[-1].lower() if "." in archivo.filename else ""
        tipo = detectar_tipo(archivo)
        if extension not in EXTENSIONES_PERMITIDAS or tipo is None:
            flash("Formato no permitido. Usa PNG, JPG, GIF o WEBP.", "error")
            return redirect(url_for("galeria"))

        nube.guardar(archivo, tipo)
        flash("Imagen subida correctamente.", "ok")
        return redirect(url_for("galeria"))

    @app.get("/archivos/<nombre>")
    def archivo(nombre):
        ruta = nube.ruta(nombre)
        if ruta is None:
            return ("Imagen no encontrada", 404)
        return send_from_directory(ruta.parent, ruta.name)

    @app.post("/borrar/<nombre>")
    def borrar(nombre):
        if nube.borrar(nombre):
            flash("Imagen eliminada.", "ok")
        else:
            flash("No se encontró la imagen.", "error")
        return redirect(url_for("galeria"))

    @app.get("/api/imagenes")
    def api_imagenes():
        return jsonify(nube.listar())

    @app.errorhandler(413)
    def demasiado_grande(_):
        flash("La imagen supera el máximo de 5 MB.", "error")
        return redirect(url_for("galeria"))

    return app
