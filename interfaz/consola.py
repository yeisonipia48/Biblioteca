from servicios.servicio_biblioteca import ServicioBiblioteca

class InterfazConsola:
    def __init__(self):
        self.servicio = ServicioBiblioteca()

    def mostrar_menu(self):
        while True:
            print("\n")
            print('*'*22)
            print("*     BIBLIOTECA     *")
            print('*'*22)
            print("\n1. Listar libros")
            print("2. Agregar libro")
            print("3. Actualizar título")
            print("4. Eliminar libro")
            print("5. Salir")
            opcion = input("\nOpción: ")
            print("\n")

            if opcion == "1":
                libros = self.servicio.listar_libros()
                for l in libros: print(l)
            elif opcion == "2":
                t = input("Título: "); a = input("Autor: ")
                self.servicio.crear_libro(t, a)
            elif opcion == "3":
                id_l = input("ID: "); nt = input("Nuevo título: ")
                self.servicio.actualizar_libro(id_l, nt)
            elif opcion == "4":
                id_l = input("ID a eliminar: ")
                self.servicio.eliminar_libro(id_l)
            elif opcion == "5": break