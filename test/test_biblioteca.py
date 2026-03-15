from servicios.servicio_biblioteca import ServicioBiblioteca

#Prueba para listar libros
def test_listar_libro():
    servicio =ServicioBiblioteca()
    lista= servicio.listar_libros()
    #Verificar que devuelva una lista
    assert isinstance(lista, list)

# Pruebas para crear un libro
def test_creacion_libro():
    # 1. Preparación (Setup)
    servicio = ServicioBiblioteca()
    titulo = "Libro de Prueba"
    autor = "Autor Test"
    
    # 2. Acción (Execution)
    # Suponiendo que tu servicio retorna el objeto creado
    libro = servicio.crear_libro(titulo, autor)
    
    # 3. Verificación (Assertion)
    assert libro.titulo == "Libro de Prueba"
    assert libro.autor == "Autor Test"


def test_actualizar_libro():
    # 1. Preparación (Setup)
    servicio = ServicioBiblioteca()
    id_libro = "1"
    nuevo_libro = "Gabriel Garcia Marquez"
    
    # 2. Acción (Execution)
    # Suponiendo que tu servicio retorna el objeto actualizando
    libro = servicio.actualizar_libro(id_libro, nuevo_libro)
    
   # 3. Verificación (Assertion)
    assert libro is True, "El servicio debería devolver True al actualizar"
    
    # 4. Verificación de Integridad (Opcional pero recomendado)
    # Vamos a buscar el libro para ver si de verdad cambió en la "base de datos"
    libros = servicio.listar_libros()
    libro_editado = next((l for l in libros if str(l.id) == id_libro), None)
    
    assert libro_editado is not None
    assert libro_editado.titulo == nuevo_libro

def test_eliminar_libro():
    servicio = ServicioBiblioteca()
    id_libro = "11"
    
    # 1. Intentamos borrarlo
    fue_borrado = servicio.eliminar_libro(id_libro)
    assert fue_borrado is True, "El servicio no confirmó la eliminación"
    
    # 2. Obtenemos la lista actualizada
    libros_actuales = servicio.listar_libros()
    
    # 3. Verificamos que NO exista ningún libro con ese ID en la lista
    # Usamos 'any' para buscar si el ID todavía ronda por ahí
    existe_todavia = any(str(l.id) == id_libro for l in libros_actuales)
    
    assert existe_todavia is False, f"El libro con ID {id_libro} sigue en la lista"