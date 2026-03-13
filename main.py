from src.ui.interfaz_consola import InterfazConsola

def main():
    """
    Punto de entrada principal de la aplicación.
    Inicializa la interfaz de usuario de la consola.
    """
    interfaz = InterfazConsola()
    interfaz.mostrar_menu()

if __name__ == "__main__":
    main()
