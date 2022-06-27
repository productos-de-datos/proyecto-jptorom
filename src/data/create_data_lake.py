from matplotlib.ft2font import LOAD_NO_HINTING


def create_data_lake():
    """Cree el data lake con sus capas.

    Esta función debe crear la carpeta `data_lake` en la raiz del proyecto. El data lake contiene
    las siguientes subcarpetas:

    ```
    .
    |
    \___ data_lake/
         |___ landing/
         |___ raw/
         |___ cleansed/
         \___ business/
              |___ reports/
              |    |___ figures/
              |___ features/
              |___ forecasts/

    ```


    """
    # Se establecen las direcciones absolutas de los directorios a crear
    dir= ['data_lake',
        'data_lake/landing',
        'data_lake/raw',
        'data_lake/cleansed',
        'data_lake/business/',
        'data_lake/business/reports/',
        'data_lake/business/reports/figures',
        'data_lake/business/features',
        'data_lake/business/forecasts'
    ]
    
    import os
    import sys
    import shutil

    #En caso de existir un directorio llamado data_lake al correr, lo elimina.
    if os.path.exists('data_lake') is True:
        shutil.rmtree('data_lake')

    # Se crean los directorios
    for ruta in dir:
        os.mkdir(ruta)
    
    #raise NotImplementedError("Implementar esta función")

if __name__ == "__main__":
    import doctest

    doctest.testmod()
    create_data_lake()
