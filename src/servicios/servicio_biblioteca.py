import pandas as pd
import json
import urllib.request
from ..modelos.libro import Libro
from ..estructuras.estructuras_lineales import Pila

class ServicioBiblioteca:
    """
    Servicio que gestiona la lógica de la biblioteca:
    - Consume la API de Open Library.
    - Implementa CRUD (Create con Pila) usando un ID único.
    """
    def __init__(self):
        self.url_api = "https://openlibrary.org/search.json?q=python"
        self.libros_iniciales = [] # Lista base cargada de la API
        self.pila_nuevos_libros = Pila() # Pila para el 'Create'
        self.contador_libros_nuevos = 0 # Contador para IDs locales
        self.cargar_datos_api()

    def cargar_datos_api(self):
        """
        Carga datos iniciales desde la API de Open Library.
        """
        try:
            print("Cargando libros desde Open Library...")
            request = urllib.request.Request(
                self.url_api,
                headers={"User-Agent": "Biblioteca/1.0 (https://openlibrary.org)"},
            )
            with urllib.request.urlopen(request, timeout=15) as response:
                payload = response.read().decode("utf-8")

            data = json.loads(payload)
            docs = data.get("docs", [])

            df = pd.DataFrame(docs)
            df.to_csv("libros.csv", index=False, encoding="utf-8")
            print("Archivo libros.csv generado/actualizado para verificación.")

            self.libros_iniciales = []

            # Tomamos los primeros 10 libros como data inicial
            for index, doc in enumerate(docs[:10]):
                id_libro = doc.get("key") or f"api_{index}"
                titulo = doc.get("title") or "Sin Título"

                author_name = doc.get("author_name")
                if isinstance(author_name, list) and len(author_name) > 0:
                    autor = author_name[0]
                elif isinstance(author_name, str) and author_name.strip():
                    autor = author_name
                else:
                    autor = "Anónimo"

                self.libros_iniciales.append(Libro(id_libro, titulo, autor))
            print(f"Se cargaron {len(self.libros_iniciales)} libros iniciales.")
        except Exception as e:
            print(f"Error al cargar datos de la API: {e}")

    # --- CRUD: CREATE (Uso de Pila) ---
    def crear_libro(self, titulo, autor):
        """
        CREATE: Agrega un nuevo libro utilizando una Pila y un ID local.
        """
        self.contador_libros_nuevos += 1
        id_local = f"nuevo_{self.contador_libros_nuevos}"
        nuevo_libro = Libro(id_local, titulo, autor)
        self.pila_nuevos_libros.apilar(nuevo_libro)
        return nuevo_libro
   
    def listar_libros(self):
        """
        READ: Devuelve una lista combinada de libros iniciales y nuevos.
        """
        return self.libros_iniciales + self.pila_nuevos_libros.obtener_todos()

    def actualizar_libro(self, id_libro, nuevo_titulo, autor):
        for libro in self.pila_nuevos_libros.items:
            if libro.id == id_libro:
                libro.titulo = nuevo_titulo
                libro.autor = autor
                return True

        for libro in self.libros_iniciales:
            if libro.id == id_libro:
                libro.titulo = nuevo_titulo
                libro.autor = autor
                return True

        return False

    def eliminar_libro(self, id_libro):
        for index, libro in enumerate(self.pila_nuevos_libros.items):
            if libro.id == id_libro:
                return self.pila_nuevos_libros.items.pop(index)

        for index, libro in enumerate(self.libros_iniciales):
            if libro.id == id_libro:
                return self.libros_iniciales.pop(index)

        return None
