import io
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from nubeimg import create_app  # noqa: E402

PNG = b"\x89PNG\r\n\x1a\n" + b"\x00" * 50


class PruebasNubeImg(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.app = create_app({"TESTING": True, "CARPETA_NUBE": self.tmp.name})
        self.cliente = self.app.test_client()

    def tearDown(self):
        self.tmp.cleanup()

    def subir(self, contenido, nombre):
        return self.cliente.post(
            "/subir", data={"imagen": (io.BytesIO(contenido), nombre)},
            content_type="multipart/form-data")

    def test_galeria_vacia(self):
        self.assertEqual(self.cliente.get("/").status_code, 200)
        self.assertEqual(self.cliente.get("/api/imagenes").json, [])

    def test_subir_png_valido(self):
        self.subir(PNG, "foto.png")
        lista = self.cliente.get("/api/imagenes").json
        self.assertEqual(len(lista), 1)
        self.assertEqual(self.cliente.get(f"/archivos/{lista[0]['nombre']}").status_code, 200)

    def test_rechaza_archivo_falso(self):
        self.subir(b"esto no es una imagen", "virus.png")
        self.assertEqual(self.cliente.get("/api/imagenes").json, [])

    def test_rechaza_extension_no_permitida(self):
        self.subir(PNG, "documento.pdf")
        self.assertEqual(self.cliente.get("/api/imagenes").json, [])

    def test_rechaza_archivo_muy_grande(self):
        self.subir(PNG + b"\x00" * (6 * 1024 * 1024), "grande.png")
        self.assertEqual(self.cliente.get("/api/imagenes").json, [])

    def test_borrar_imagen(self):
        self.subir(PNG, "foto.png")
        nombre = self.cliente.get("/api/imagenes").json[0]["nombre"]
        self.cliente.post(f"/borrar/{nombre}")
        self.assertEqual(self.cliente.get("/api/imagenes").json, [])

    def test_no_permite_leer_fuera_de_la_carpeta(self):
        self.assertEqual(self.cliente.get("/archivos/..%2Frun.py").status_code, 404)
        self.assertEqual(self.cliente.get("/archivos/secreto.txt").status_code, 404)


if __name__ == "__main__":
    unittest.main()
