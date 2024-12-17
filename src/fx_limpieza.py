import pandas as pd

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
