import pandas as pd
import numpy as np

def valores_nulos(df):
    """
    Calcula el número y el porcentaje de valores nulos en un DataFrame.

    Args:
        df (pd.DataFrame): El DataFrame sobre el cual se calcularán los valores nulos.

    Returns:
        pd.DataFrame: Un DataFrame con dos columnas:
            - 'numero_nulos': Número de valores nulos por columna.
            - 'porcentaje_nulos': Porcentaje de valores nulos respecto al total de filas.
            - 'tipo_dato': Tipo de dato (dtype) de cada columna.
    """
    # Crear un DataFrame vacío
    df_nulos = pd.DataFrame()
    
    # Calcular número de nulos y porcentaje de nulos
    df_nulos["numero_nulos"] = df.isnull().sum()
    df_nulos["porcentaje_nulos"] = round((df.isnull().sum() / df.shape[0]) * 100, 2)
    df_nulos["tipo_dato"] = df.dtypes

    return df_nulos

################################
""" import os
import pandas as pd """
#####
""" def cargar_archivos_en_dataframe(directorio, extension,encoding="utf-8"): """
"""
    Busca archivos con la extensión dada en el directorio y carga todos los datos en un único DataFrame.
    
    Parámetros:
    - directorio: Ruta donde se buscarán los archivos.
    - extension: Extensión del archivo a buscar (como '.csv', '.xlsx', etc.)
    
    Retorna:
    - DataFrame con los datos combinados de todos los archivos encontrados.
   
    
    # Lista para almacenar los DataFrames
    dfs = []
    
    # Buscar archivos en el directorio con la extensión especificada
    for archivo in os.listdir(directorio):
        if archivo.endswith(extension):
            archivo_path = os.path.join(directorio, archivo)
            
            # Dependiendo de la extensión, se carga el archivo correspondiente
            if extension == '.csv':
                df = pd.read_csv(archivo_path)
            elif extension == '.xlsx':
                df = pd.read_excel(archivo_path)
            else:
                print(f"Formato de archivo {extension} no soportado.")
                return None
            
            # Añadir el DataFrame a la lista
            dfs.append(df)
            print(f"Archivo cargado: {archivo}")
    
    # Si se encontraron archivos y se cargaron, concatenar los DataFrames
    if dfs:
        df_final = pd.concat(dfs, ignore_index=True)
        print(f"Se han cargado {len(dfs)} archivos en un único DataFrame.")
        return df_final
    else:
        print(f"No se encontraron archivos con la extensión {extension} en el directorio.")
        return None

# Ejemplo de uso
directorio = '../datos/raw_data/'  # Especifica tu directorio
extension = input("Ingresa la extensión de los archivos a buscar (ejemplo: '.csv', '.xlsx'): ")
encoding="utf-8"

df_resultado = cargar_archivos_en_dataframe(directorio, extension)

if df_resultado is not None:
    print(df_resultado.head())  # Muestra las primeras filas del DataFrame resultante
 """