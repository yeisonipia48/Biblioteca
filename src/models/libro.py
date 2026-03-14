class Libro:
    def __init__(self,id_libro,titulo,autor,usuario_prestamo=None):
        self.id = id_libro
        self.titulo = titulo
        self.autor = autor
        self.prestado=False
        self.usuario_prestamo=usuario_prestamo
    
    def __str__(self):
            estado = f"| Prestado a: {self.usuario_prestamo}" if self.usuario_prestamo else "| Disponible"
            return f"ID: {self.id} | Título: {self.titulo} | Autor: {self.autor} {estado}"