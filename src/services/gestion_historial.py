

class Gestion_historial:
    def __init__(self,gestion_libros):
        self.gestion = gestion_libros
    # --- NUEVAS ESTRUCTURAS INTEGRADAS ---
        self.pila_historial=[] # PILA: Últimas acciones (LIFO)
        self.cola_reservas=[] # COLA: Usuarios esperando libros (FIFO)
    # --- MODULO HISTORIAL ---
    def registrar_accion(self,mensaje):
        """Agrega una acción a la pila"""
        self.pila_historial.append(mensaje)

    def ver_ultimo_movimiento(self):
        """Muestra el tope de la pila sin eliminarlo"""
        return self.pila_historial[-1] if self.pila_historial else "Sin historial."
    
    # --- MÓDULO: RESERVAS (COLA) ---
    def encolar_reserva(self,nombre_usuario):
        self.cola_reservas.append(nombre_usuario)
        self.registrar_accion(f"Reserva: {nombre_usuario} entro a la cola")
    
    def atender_siguiente_reserva(self):
        if self.cola_reservas:
            usuario= self.cola_reservas.pop(0)
            self.registrar_accion(f"Reserva atendida, se presta el libro a:{usuario}")
            return usuario
        return None
    # --- MÓDULO: RESERVAS (COLA) ---

    def prestar_libro_usuario(self, id_libro, nombre_usuario):
        actual = self.gestion.cabeza
        while actual:
            if str(actual.libro.id) == str(id_libro):
                # Si tu modelo Libro tuviera un atributo 'usuario', aquí validarías
                # Por ahora, simulamos el préstamo registrando la acción
                self.registrar_accion(f"Préstamo: Libro ID {id_libro} a {nombre_usuario}")
                return f"Éxito: Libro '{actual.libro.titulo}' asignado a {nombre_usuario}."
            actual = actual.siguiente
        
        # Si no se encuentra, lo mandamos a la cola de espera (Innovación)
        self.encolar_reserva(nombre_usuario)
        return f"Libro no encontrado. {nombre_usuario} ha sido agregado a la COLA de espera."
