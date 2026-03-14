from src.services.gestion_libros import GestionLibros
from src.services.gestion_historial import Gestion_historial
from src.models.libro import Libro
from src.services.gestion_usuarios import Gestion_usuarios
def menu():
    gestion_libros = GestionLibros()
    gestion_historial = Gestion_historial(gestion_libros)
    gestion_usuarios= Gestion_usuarios()
    
    while True:
        print("\n--- SISTEMA DE BIBLIOTECA (DELETE TEST) ---")
        print("1. Listar Libros")
        print("2. Agregar libro")
        print("3. Actualizar")
        print("4. Eliminar Libro por ID")
        print("5. Prestar libro")
        print("6. Ver Historial de acciones (Pila - LIFO)")
        print("7. Ver siguiente en cola de reserva (Cola - FIFO)")
        print("8. GESTIÓN USUARIOS (Cola - FIFO)")
        print("9. Salir")
        
        #Sección para que el usuario elija un valor numerico, usamos int, para asegurar que es un entero
        opcion = int(input("Selecciona una opción: "))
        
        if opcion == 1:
            print("\nListado actual en memoria:")
            gestion_libros.mostrar_libros()
        elif opcion == 2:
            print("\n--- AGREGAR NUEVO LIBRO ---")
            # 1. El sistema genera el ID automáticamente
            nuevo_id=gestion_libros.generar_nuevo_id()
            print(f"ID asignado automáticamente: {nuevo_id}")
            # 2. Agregar nuevo nombre
            nombre_libro=input("Ingresa el nombre del nuevo libro:")
            nombre_autor=input("Ingresa el nombre del autor:")
            # 3. Creamos el objeto con ese ID automático
            libro=Libro(nuevo_id,nombre_libro,nombre_autor)
            gestion_libros.insertar_al_final(libro)
            gestion_historial.registrar_accion(f"Libro agregado: {nombre_libro} (ID: {nuevo_id})")
            print("¡Libro guardado con éxito!")
        elif opcion == 3:
            pass
        elif opcion == 4:
            id_borrar = input("Ingresa el ID del libro a eliminar: ")
            if gestion_libros.eliminar_libro(id_borrar):
                print("¡Éxito! El libro fue eliminado de la lista y del CSV.")
                gestion_historial.registrar_accion(f"Libro eliminado: ID {id_borrar}")
            else:
                print("Error: No se encontró un libro con ese ID.")
        elif opcion == 5:
            print("\n--- PRESTAR LIBRO ---")
            id_libro = input("Ingresa el ID del libro: ")
            nombre_usuario = input("Ingresa el nombre del usuario: ")
            resultado = gestion_historial.prestar_libro_usuario(id_libro, nombre_usuario)
            print(resultado)
        elif opcion == 6:
            print("\n--- HISTORIAL DE ACCIONES (PILA) ---")
            # Mostramos el último movimiento usando la lógica de Pila
            ultimo = gestion_historial.ver_ultimo_movimiento()
            print(f"Última acción realizada: {ultimo}")
            
            # Opcional: Podrías hacer un bucle para mostrar toda la pila si quisieras
            print(f"Total de acciones en pila: {len(gestion_historial.pila_historial)}")
        elif opcion == 7:
            print("\n--- GESTIÓN DE RESERVAS (COLA) ---")
            if not gestion_historial.cola_reservas:
                print("No hay nadie en la cola de espera.")
            else:
                print(f"Usuarios esperando: {gestion_historial.cola_reservas}")
                confirmar = input("¿Deseas atender al siguiente usuario? (s/n): ")
                if confirmar.lower() == 's':
                    atendido = gestion_historial.atender_siguiente_reserva()
                    print(f"Atendiendo a: {atendido}. Ahora puede solicitar su libro.")
        elif opcion == 8:
            print("\n--- BIENVENIDO A LA GESTIÓN DE  USUARIOS (COLA) ---")
            print("\nELIJA QUE ES LO QUE QUIERE HACER HOY: \n 1. VER USUARIO,\n 2. AGREGAR USUARIO,\n 3. ACTUALIZAR USUARIO,\n 4. ELIMINAR USUARIO \n 5. SALIR")
            continuar_usuarios=True
            while continuar_usuarios:
                #opcion para que el usuario elija ver, agregar, borrar 
                opcion_gestion_usuario=int(input("Selecciona una opción: "))
                if opcion_gestion_usuario ==1:
                    print("\nListado actual en memoria:")
                    gestion_usuarios.mostrar_usuarios()
                elif opcion_gestion_usuario==2:

                    nombre_usuario=input("Escribe por favor el nombre del usuario:")
                    gestion_usuarios.resgistar_usuario(nombre_usuario)
                elif opcion_gestion_usuario==5:
                    continuar_usuarios = False
        elif opcion == 9:
            break

if __name__ == "__main__":
    menu()