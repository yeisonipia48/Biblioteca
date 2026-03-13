from src.services.gestion_libros import GestionLibros

def menu():
    gestion = GestionLibros()
    
    while True:
        print("\n--- SISTEMA DE BIBLIOTECA (DELETE TEST) ---")
        print("1. Listar Libros")
        print("2. Eliminar Libro por ID")
        print("3. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            print("\nListado actual en memoria:")
            gestion.mostrar_libros()
            
        elif opcion == "2":
            id_borrar = input("Ingresa el ID del libro a eliminar: ")
            if gestion.eliminar_libro(id_borrar):
                print("¡Éxito! El libro fue eliminado de la lista y del CSV.")
            else:
                print("Error: No se encontró un libro con ese ID.")
                
        elif opcion == "3":
            break

if __name__ == "__main__":
    menu()