from ..models.users import User

class NodoUsuario:
    def __init__(self, usuario):
        self.usuario = usuario
        self.siguiente = None

class Gestion_usuarios:
    def __init__(self):
        self.cabeza=None
        self.usuarios=[]


    #creacion de id autoincrementable
    def generar_nuevo_id_usuario(self):
        """Genera un nuevo ID basado en el último id en la lista"""
        if not self.cabeza:
            return 1
        max_id=0
        actual=self.cabeza
        while actual:
            if int(actual.usuario.id)>max_id:
                max_id=int(actual.usuario.id)
            actual=actual.siguiente
            return max_id+1
        
    # --- MODULO REGISTRO---
    def resgistar_usuario(self,nombre):
        id_usuario = self.generar_nuevo_id_usuario()
        nuevo_usuario = User(id_usuario, nombre)
        nuevo_nodo = NodoUsuario(nuevo_usuario)

        # Lógica de inserción en Lista Enlazada
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente: # Buscamos el último nodo
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo # Conectamos el nuevo

        print(f"Usuario registrado: {nombre} (ID: {id_usuario})")
    
    def mostrar_usuarios(self):
        """Recorre la lista para mostrarla en consola"""
        actual = self.cabeza
        if not actual:
            print("No hay usuarios registrados.")
            return
        
        print("\n--- LISTADO DE USUARIOS (Estructura Lineal) ---")
        
        while actual:
            # Asegúrate de que el modelo User tenga un método __str__ para que se vea bien
    
            print(f"Nombre usuario: {actual.usuario.nombre_usuario} ID:{actual.usuario.id_usuario}")
            actual = actual.siguiente