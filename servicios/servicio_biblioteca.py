from data.manipulacion import Manipulacion
from entidades.libro import Libro

class ServicioBiblioteca:
    def __init__(self):
        self.repo = Manipulacion()

    def listar_libros(self):
        datos_crudos = self.repo.read()
        return [Libro(f[0], f[1], f[2]) for f in datos_crudos]

    def crear_libro(self, titulo, autor):
        libros = self.repo.read()
        nuevo_id = str(len(libros) + 1)
        nueva_fila = [nuevo_id, titulo, autor]
        self.repo.create(nueva_fila)
        return nuevo_id

    def actualizar_libro(self, id_libro, nuevo_titulo):
        libros = self.repo.read()
        for i, fila in enumerate(libros):
            if str(fila[0]) == str(id_libro):
                nueva_fila = [fila[0], nuevo_titulo, fila[2]]
                self.repo.update(i, nueva_fila)
                return True
        return False

    def eliminar_libro(self, id_libro):
        libros = self.repo.read()
        for i, fila in enumerate(libros):
            if str(fila[0]) == str(id_libro):
                self.repo.delete(i)
                return True
        return False