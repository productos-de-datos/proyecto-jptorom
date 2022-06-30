def transform_data():
    """Transforme los archivos xls a csv.

    Transforme los archivos data_lake/landing/*.xls a data_lake/raw/*.csv. Hay
    un archivo CSV por cada archivo XLS en la capa landing. Cada archivo CSV
    tiene como columnas la fecha en formato YYYY-MM-DD y las horas H00, ...,
    H23.

    """
import openpyxl
import pandas as pd

for yearnum in range (1995,2022):
    if yearnum == 2016  or yearnum == 2017:
        read_file = pd.read_excel('data_lake/landing/{}.xls'.format(yearnum),index_col=None, header = None)
        # Se eliminan columnas sobrantes
        df = read_file.iloc[:,:25]
        # Se eliminan filas que no tienen información
        df = df.dropna(how = "any")
        df.to_csv('data_lake/raw/{}.csv'.format(yearnum), index_label= False, index = False, header = None)  
    if yearnum in range (2018,2022):
        read_file = pd.read_excel('data_lake/landing/{}.xlsx'.format(yearnum),index_col=None, header = None)
        # Se eliminan columnas sobrantes
        df = read_file.iloc[:,:25]
        df.to_csv('data_lake/raw/{}.csv'.format(yearnum), index_label= False, index = False, header = None)  

    if yearnum in range (1995,2016):
        read_file = pd.read_excel('data_lake/landing/{}.xlsx'.format(yearnum),index_col=None)
        # Se eliminan columnas sobrantes
        df = read_file.iloc[:,:25]
        # Se eliminan filas que no tienen información
        df = df.dropna(how = "any")
        df.to_csv('data_lake/raw/{}.csv'.format(yearnum), index_label= False, index = False, header = None)     

if __name__ == "__main__":
    import doctest

    doctest.testmod()
    transform_data()
