class Libro:
    def __init__(self, id_libro, titulo, autor):
        self.id = id_libro
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"ID: {self.id} | Título: {self.titulo} | Autor: {self.autor}"