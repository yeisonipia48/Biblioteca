from src.services.gestion_libros import GestionLibros
from src.models.libro import Libro
def menu():
    gestion = GestionLibros()
    
    while True:
        print("\n--- SISTEMA DE BIBLIOTECA (DELETE TEST) ---")
        print("1. Listar Libros")
        print("2. Agregar libro")
        print("3. Actualizar")
        print("4. Eliminar Libro por ID")
        print("5. Prestar libro")
        print("6. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            print("\nListado actual en memoria:")
            gestion.mostrar_libros()
        elif opcion == "2":
            print("\n--- AGREGAR NUEVO LIBRO ---")
            # 1. El sistema genera el ID automáticamente
            nuevo_id=gestion.generar_nuevo_id()
            print(f"ID asignado automáticamente: {nuevo_id}")
            # 2. Agregar nuevo nombre
            nombre_libro=input("Ingresa el nombre del nuevo libro:")
            nombre_autor=input("Ingresa el nombre del autor:")
            # 23 Creamos el objeto con ese ID automático
            libro=Libro(nuevo_id,nombre_libro,nombre_autor)
            gestion.insertar_al_final(libro)
            print("¡Libro guardado con éxito!")
        elif opcion == "4":
            id_borrar = input("Ingresa el ID del libro a eliminar: ")
            if gestion.eliminar_libro(id_borrar):
                print("¡Éxito! El libro fue eliminado de la lista y del CSV.")
            else:
                print("Error: No se encontró un libro con ese ID.")
        elif opcion == "5":
            pass
        elif opcion == "6":
            break

if __name__ == "__main__":
    menu()