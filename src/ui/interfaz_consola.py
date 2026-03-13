from ..servicios.servicio_biblioteca import ServicioBiblioteca

class InterfazConsola:
    def __init__(self):
        self.servicio = ServicioBiblioteca()

    def mostrar_menu(self):
        while True:
            print("\n--- SISTEMA DE GESTIÓN DE BIBLIOTECA ---")
            print("1. Listar libros (Read)")
            print("2. Agregar nuevo libro (Create con Pila)")
            print("3. Actualizar libro (Update - Ejemplo)")
            print("4. Eliminar libro (Delete - Ejemplo)")
            print("5. Salir")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                self.listar_libros()
            elif opcion == "2":
                self.agregar_libro()
            elif opcion == "3":
                self.actualizar_libro()
            elif opcion == "4":
                self.eliminar_libro()
            elif opcion == "5":
                print("Saliendo del sistema...")
                break
            else:
                print("Opción no válida.")

    def listar_libros(self):
        libros = self.servicio.listar_libros()
        print("\n--- LISTADO DE LIBROS ---")
        for libro in libros:
            print(libro)

    def agregar_libro(self):
        print("\n--- AGREGAR NUEVO LIBRO ---")
        titulo = input("Título: ")
        autor = input("Autor: ")
        libro_creado = self.servicio.crear_libro(titulo, autor)
        print(f"Libro agregado a la Pila con ID: {libro_creado.id}")

    def actualizar_libro(self):
        print("\n--- ACTUALIZAR LIBRO ---")
        id_libro = input("Ingrese el ID del libro a actualizar: ")
        nuevo_titulo = input("Ingrese el nuevo título: ")
        if self.servicio.actualizar_libro(id_libro, nuevo_titulo):
            print("Libro actualizado.")
        else:
            print("Libro no encontrado.")

    def eliminar_libro(self):
        print("\n--- ELIMINAR LIBRO ---")
        id_libro = input("Ingrese el ID del libro a eliminar: ")
        libro_eliminado = self.servicio.eliminar_libro(id_libro)
        if libro_eliminado:
            print(f"Libro eliminado: {libro_eliminado}")
        else:
            print("Libro no encontrado.")
