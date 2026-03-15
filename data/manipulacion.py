import pandas as pd
from data.libros import data

class Manipulacion:
    ruta = r'data/libro1.csv'
    columnas = ['Id', 'Titulo', 'Autor']

    @classmethod
    def _guardar(cls, lista):
        try:
            df = pd.DataFrame(lista, columns=cls.columnas)
            df.to_csv(cls.ruta, index=False)
        except PermissionError:
            print("\n[!] ERROR: Cierra el archivo Excel 'Libro1.xlsx' y presiona Enter.")

    @classmethod
    def create(cls, nueva_fila):
        with data() as datos:
            datos.append(nueva_fila)
            cls._guardar(datos)

    @classmethod
    def read(cls):
        with data() as datos:
            return datos

    @classmethod
    def update(cls, indice, nueva_fila):
        with data() as datos:
            if 0 <= indice < len(datos):
                datos[indice] = nueva_fila
                cls._guardar(datos)

    @classmethod
    def delete(cls, indice):
        with data() as datos:
            if 0 <= indice < len(datos):
                datos.pop(indice)
                cls._guardar(datos)