class Pila:
    """
    Implementación de una estructura de datos lineal tipo Pila (LIFO - Last In, First Out).
    Se utiliza para gestionar la creación de nuevos libros en el sistema.
    """
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, item):
        """Agrega un elemento a la cima de la pila (Push)."""
        self.items.append(item)

    def desapilar(self):
        """Elimina y devuelve el elemento en la cima de la pila (Pop)."""
        if not self.esta_vacia():
            return self.items.pop()
        return None

    def ver_cima(self):
        """Devuelve el elemento en la cima sin eliminarlo (Peek)."""
        if not self.esta_vacia():
            return self.items[-1]
        return None

    def tamano(self):
        return len(self.items)

    def obtener_todos(self):
        """Devuelve todos los elementos de la pila como una lista (para visualización)."""
        return self.items.copy()
