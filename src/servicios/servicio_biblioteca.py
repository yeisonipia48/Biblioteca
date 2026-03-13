import pandas as pd
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
        self.pil-nuevos_libros = Pila() # Pila para el 'Create'
        self.contador_libros_nuevos = 0 # Contador para IDs locales
        self.cargar_datos_api()

    def cargar_datos_api(self):
        """
        Carga datos iniciales desde la API de Open Library usando pandas.
        """
        try:
            print("Cargando libros desde Open Library...")
            df = pd.read_json(self.url_api, path="docs")
            df.to_csv("libros.csv", index=False)
            print("Archivo libros.csv generado/actualizado para verificación.")

            # Tomamos los primeros 10 libros como data inicial
            for index, row in df.head(10).iterrows():
                id_libro = row.get('key', f"api_{index}")
                titulo = row.get('title', 'Sin Título')
                autor = row.get('author_name', ['Anónimo'])[0] if isinstance(row.get('author_name'), list) else 'Anónimo'
                libro = Libro(id_libro, titulo, autor)
                self.libros_iniciales.append(libro)
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
        self.pil-nuevos_libros.apilar(nuevo_libro)
        return nuevo_libro
   
