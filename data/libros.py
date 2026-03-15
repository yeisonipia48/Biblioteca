import pandas as pd
from contextlib import contextmanager
import os

@contextmanager
def data(ruta=r'data/libro1.csv'):
    datos = []
    try:
        if os.path.exists(ruta):
            df = pd.read_csv(ruta)
            datos = df.values.tolist() # Convertir a estructura lineal (lista de listas)
        yield datos
    except Exception as e:
        print(f"Error al leer: {e}")
        yield []