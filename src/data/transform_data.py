def transform_data():
    """Transforme los archivos xls a csv.

    Transforme los archivos data_lake/landing/*.xls a data_lake/raw/*.csv. Hay
    un archivo CSV por cada archivo XLS en la capa landing. Cada archivo CSV
    tiene como columnas la fecha en formato YYYY-MM-DD y las horas H00, ...,
    H23.

    """
    raise NotImplementedError("Implementar esta función")
    
from openpyxl import Workbook
from email import header
import pandas as pd

for yearnum in range (1995,2022):
    if yearnum == 2016 or yearnum == 2017:
        read_file = pd.read_excel('data_lake/landing/{}.xls'.format(yearnum),header = None)
        # Mantenga solo las filas con al menos 20 valores que no sean NA
        df = read_file.dropna(axis =0, thresh= 20)
        # Omitir la primera fila
        df = df.iloc[1:]
        # Establecer la primer columna como formato fecha
        df[0] = pd.to_datetime(df[0], format="%Y/%m/%d")
        df.to_csv('data_lake/raw/{}.csv'.format(yearnum), index= False, header = True)
    else:
        read_file = pd.read_excel('data_lake/landing/{}.xlsx'.format(yearnum),header = None)
        # Mantenga solo las filas con al menos 20 valores que no sean NA
        df = read_file.dropna(axis =0, thresh= 20)
        # Omitir la primera fila
        df = df.iloc[1:]
        # Establecer la primer columna como formato fecha
        df[0] = pd.to_datetime(df[0], format="%Y/%m/%d")
        df.to_csv('data_lake/raw/{}.csv'.format(yearnum), index= False, header = True)     

if __name__ == "__main__":
    import doctest

    doctest.testmod()
    transform_data()
