from logging.handlers import DatagramHandler
from pandas import DataFrame


def clean_data():
    """Realice la limpieza y transformación de los archivos CSV.

    Usando los archivos data_lake/raw/*.csv, cree el archivo data_lake/cleansed/precios-horarios.csv.
    Las columnas de este archivo son:

    * fecha: fecha en formato YYYY-MM-DD
    * hora: hora en formato HH
    * precio: precio de la electricidad en la bolsa nacional

    Este archivo contiene toda la información del 1997 a 2021.


    """
    import pandas as pd
    import os
    import glob

    #Se coloca la ruta en la que se encuentran los archivos
    files_joined = os.path.join('data_lake/raw/', "*.csv")

    #Se genera una lista con todos los archivos
    list_files = glob.glob(files_joined)

    #Se combinan los archivos
    df = pd.concat(map(pd.read_csv, list_files), ignore_index=True)
    # Se ajusta el formato de la fecha
    df["Fecha"] = pd.to_datetime(df["Fecha"], format="%Y/%m/%d")
    # Se elimina el pivote de la Fecha
    dataframe2 = pd.melt(df, id_vars=["Fecha"], value_vars = df.columns[1:], var_name= "hora", value_name= "precio")
    # Se elimina la letra H en la columna hora
    dataframe2["hora"] = dataframe2["hora"].replace({'H':''}, regex=True)
    # Se ajusta el formato de la columna hora
    dataframe2["hora"] = pd.to_numeric(dataframe2["hora"])
    # Se convierte la tabla en formato csv y se guarda en la carpeta cleansed del datalake
    dataframe2.to_csv('data_lake/cleansed/precios-horarios4.csv',index=False)
    
    #raise NotImplementedError("Implementar esta función")
    return dataframe2

if __name__ == "__main__":
    import doctest

    doctest.testmod()
    clean_data()

