class Libro:
    def __init__(self, id, titulo, autor):
        self.id = id
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"ID: {self.id} | Título: '{self.titulo}' por {self.autor}"
