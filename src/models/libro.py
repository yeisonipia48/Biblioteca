class Libro:
    def __init__(self,id_libro,titulo,autor):
        self.id = id_libro
        self.titulo = titulo
        self.autor = autor
    
    def __str__(self):
        return f"[{self.id}] {self.titulo} - {self.autor}"