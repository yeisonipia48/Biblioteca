class User:
    def __init__(self,id_usuario,nombre_usuario):
        self.id_usuario=id_usuario
        self.nombre_usuario=nombre_usuario
        self.libros_prestados=[]

    def __str__(self):
        return f"User: [{self.id_usuario}] {self.id_usuario}"
        