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
import os
import requests

for yearnum in range (1995,2022):
    if yearnum == 2016 or yearnum == 2017:
        link_descarga = 'https://github.com/jdvelasq/datalabs/blob/master/datasets/precio_bolsa_nacional/xls/{}.xls?raw=true'.format(yearnum)
        descarga = requests.get(link_descarga, allow_redirects= True)
        open ('data_lake/landing/{}.xls'.format(yearnum), 'wb').write(descarga.content)

    else:
        link_descarga = 'https://github.com/jdvelasq/datalabs/blob/master/datasets/precio_bolsa_nacional/xls/{}.xlsx?raw=true'.format(yearnum)
        descarga = requests.get(link_descarga, allow_redirects= True)
        open ('data_lake/landing/{}.xlsx'.format(yearnum), 'wb').write(descarga.content)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    ingest_data()
