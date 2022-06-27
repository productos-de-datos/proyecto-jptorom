"""
Módulo de ingestión de datos.
-------------------------------------------------------------------------------

"""


def ingest_data():
    """Ingeste los datos externos a la capa landing del data lake.

    Del repositorio jdvelasq/datalabs/precio_bolsa_nacional/xls/ descarge los
    archivos de precios de bolsa nacional en formato xls a la capa landing. La
    descarga debe realizarse usando únicamente funciones de Python.

    """

def ingest_data():
    """Ingeste los datos externos a la capa landing del data lake.

    Del repositorio jdvelasq/datalabs/precio_bolsa_nacional/xls/ descarge los
    archivos de precios de bolsa nacional en formato xls a la capa landing. La
    descarga debe realizarse usando únicamente funciones de Python.

    """
import pandas as pd
import wget
import os

link = "https://github.com/jdvelasq/datalabs/blob/master/datasets/precio_bolsa_nacional/xls"
os.chdir('data_lake/landing')
for yearnum in range (1995,2021):
    wdir = link + "/" + format(yearnum) + ".xlsx"
    pd.read_excel(wget.download(wdir))
os.chdir('../../')

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    ingest_data()
