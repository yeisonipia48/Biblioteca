# Biblioteca

Sistema de gestión de biblioteca desarrollado en Python que permite administrar un catálogo de libros mediante una interfaz de consola.

## Descripción

Este proyecto es una aplicación de gestión de biblioteca que permite:
- **Listar** todos los libros del catálogo
- **Agregar** nuevos libros (título y autor)
- **Actualizar** el título de un libro existente
- **Eliminar** libros del catálogo

Los datos se almacenan en un archivo CSV, utilizando la librería `pandas` para la manipulación de datos.

## Estructura del Proyecto

```
Biblioteca/
├── main.py                    # Punto de entrada de la aplicación
├── entidades/
│   └── libro.py               # Clase que representa un libro
├── servicios/
│   └── servicio_biblioteca.py # Lógica de negocio de la biblioteca
├── interfaz/
│   └── consola.py             # Interfaz de usuario por consola
├── data/
│   ├── libro1.csv             # Archivo de datos (CSV)
│   ├── libros.py              # Gestor de datos con context manager
│   └── manipulacion.py        # Clase para operaciones CRUD
└── requirements.txt           # Dependencias del proyecto
```

## Arquitectura

El proyecto sigue el patrón de arquitectura por capas:

1. **Entidades**: Define el modelo de datos [`Libro`](entidades/libro.py:1)
2. **Servicios**: Contiene la lógica de negocio en [`ServicioBiblioteca`](servicios/servicio_biblioteca.py:4)
3. **Datos**: Maneja el almacenamiento en [`Manipulacion`](data/manipulacion.py:4)
4. **Interfaz**: Comunicación con el usuario en [`InterfazConsola`](interfaz/consola.py:3)

### Flujo de funcionamiento

1. El usuario ejecuta `main.py`
2. [`InterfazConsola`](interfaz/consola.py:3) muestra el menú y captura las opciones
3. Las opciones delegan a [`ServicioBiblioteca`](servicios/servicio_biblioteca.py:4)
4. [`Manipulacion`](data/manipulacion.py:4) realiza las operaciones CRUD sobre el CSV

## Requisitos

- Python 3.8+
- Las libreríaslisted en `requirements.txt`

## Instalación

### 1. Clonar o descargar el proyecto

```bash
git clone <repositorio>
cd Biblioteca
```

### 2. Crear un entorno virtual (opcional pero recomendado)

```bash
python -m venv venv
source venv/bin/activate    # En Linux/Mac
venv\Scripts\activate       # En Windows
```

### 3. Instalar las dependencias

Instala todas las librerías del archivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

Las librerías incluidas son:
- `pandas==3.0.1` - Manipulación y análisis de datos
- `numpy==2.4.3` - Computación numérica (dependencia de pandas)
- `openpyxl==3.1.5` - Lectura/escritura de archivos Excel
- `et_xmlfile==2.0.0` - Soporte para archivos Excel XML
- `python-dateutil==2.9.0.post0` - Extensiones de fecha/hora
- `six==1.17.0` - Compatibilidad entre Python 2 y 3

## Uso

Para ejecutar la aplicación:

```bash
python main.py
```

### Opciones del menú

1. **Listar libros**: Muestra todos los libros del catálogo
2. **Agregar libro**: Solicita título y autor para crear un nuevo libro
3. **Actualizar título**: Solicita ID del libro y nuevo título
4. **Eliminar libro**: Solicita ID del libro a eliminar
5. **Salir**: Cierra la aplicación

## Tests

El proyecto incluye tests unitarios en el directorio `test/`. Para ejecutarlos:

```bash
pytest test/
```

## Notas

- El archivo de datos se encuentra en [`data/libro1.csv`](data/libro1.csv)
- Si el archivo CSV está abierto en Excel, la aplicación mostrará un error de permisos
