import pandas as pd
import os
from src.models.libro import Libro

class Nodo:
    def __init__(self,libro):
        self.libro = libro
        self.siguiente= None

class GestionLibros:
    def __init__(self):
        self.cabeza = None
        self.archivo_csv ="data/libros.csv"
        if not os.path.exists('data'):
            os.makedirs('data')
        self.cargar_datos_iniciales()

    def cargar_datos_iniciales(self):
        """Lee el CSV y crea los nodos en memoria"""
        if os.path.exists(self.archivo_csv):
            try:
                df=pd.read_csv(self.archivo_csv)
                for _, fila in df.iterrows():
                    # Por cada fila del CSV, creamos un objeto Libro y un Nodo
                    nuevo_libro = Libro(str(fila['id']), fila['titulo'], fila['autor'])
                    self.insertar_al_final(nuevo_libro)
            except Exception as e:
                print(f"Error al cargar el CSV: {e}")
    
    def insertar_al_final(self, libro):
        """Agrega un nodo al final de la estructura lineal"""
        
        nuevo_nodo = Nodo(libro)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            return
        
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nuevo_nodo
        # Realizamos una sincronización con el archivo csv
        self.sincronizar_csv() # Guardamos los cambios en el archivo físico
        return True
        

    # --- GENERAR NUEVO ID UNICO-AUTO_ICREMENT
    def generar_nuevo_id(self):
        if not self.cabeza:
            return 1
        actual =self.cabeza
        max_id=0

        while actual:
            try:
                id_actual=int(actual.libro.id)
                if id_actual > max_id:
                    max_id= id_actual
            except ValueError:
                pass # Por si hay algún ID que no sea número
            actual=actual.siguiente
        return max_id+1
    # -- INSERTAR LIBRO CSV 
    # --- LÓGICA DEL DELETE (Eliminación en Lista Enlazada) ---
    def eliminar_libro(self, id_objetivo):
        """
        Busca un libro por ID y lo elimina desconectando el nodo.
        """
        actual = self.cabeza
        anterior = None
        encontrado = False

        # Recorremos la estructura lineal (punteros)
        while actual is not None:
            if str(actual.libro.id) == str(id_objetivo):
                if anterior is None:
                    # Caso 1: El libro a borrar es la cabeza
                    self.cabeza = actual.siguiente
                else:
                    # Caso 2: El libro está en medio o al final
                    # "Saltamos" el nodo actual conectando el anterior con el siguiente
                    anterior.siguiente = actual.siguiente
                
                encontrado = True
                break
            
            # Mover los punteros al siguiente
            anterior = actual
            actual = actual.siguiente

        if encontrado:
            self.sincronizar_csv() # Guardamos los cambios en el archivo físico
            return True
        return False

    def sincronizar_csv(self):
        """Convierte la estructura de nodos de vuelta a CSV"""
        datos = []
        actual = self.cabeza
        while actual:
            datos.append({
                "id": actual.libro.id,
                "titulo": actual.libro.titulo,
                "autor": actual.libro.autor
            })
            actual = actual.siguiente
        
        df = pd.DataFrame(datos)
        df.to_csv(self.archivo_csv, index=False)

    def mostrar_libros(self):
        """Recorre la lista para mostrarla en consola"""
        actual = self.cabeza
        if not actual:
            print("La biblioteca está vacía.")
            return
        while actual:
            print(actual.libro)
            actual = actual.siguiente