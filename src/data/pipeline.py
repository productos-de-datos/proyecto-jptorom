"""
Construya un pipeline de Luigi que:

* Importe los datos xls
* Transforme los datos xls a csv
* Cree la tabla unica de precios horarios.
* Calcule los precios promedios diarios
* Calcule los precios promedios mensuales

En luigi llame las funciones que ya creo.


"""

import os
from luigi import Task, LocalTarget
import luigi
from create_data_lake import create_data_lake
from ingest_data import ingest_data
from transform_data import transform_data
from clean_data import clean_data
from compute_monthly_prices import compute_monthly_prices
from compute_daily_prices import compute_daily_prices
import pandas as pd

if __name__ == "__main__":
    class CargueDatos(Task):
      
        def output(self):
            return luigi.LocalTarget('data_lake/landing/arc.csv')

        def run(self):
            with self.output().open("w") as outfile:
                ingest_data()

    class TransformaciónDatos(Task):

        def requires(self):
            return CargueDatos()
   
        def output(self):
            return luigi.LocalTarget('data_lake/raw/arc.txt')

        def run(self):
            with self.output().open("w") as outfile:
                transform_data()

    class TablaPrecioDia(Task):
        def requires(self):
            return TransformaciónDatos()

        def output(self):
            return luigi.LocalTarget('data_lake/cleansed/arc.txt')

        def run(self):
            with self.output().open("w") as outfile:
                clean_data()

    class PrecioAvgDiario(Task):
        def requires(self):
            return TablaPrecioDia()

        def output(self):
            return luigi.LocalTarget('data_lake/business/arc.txt')

        def run(self):
            with self.output().open("w") as outfile:
                compute_daily_prices()

    class PrecioAvgMensual(Task):

        def output(self):
            return luigi.LocalTarget('data_lake/business/arc.txt')

        def run(self):
            with self.output().open("w") as outfile:
                compute_monthly_prices()
    
    #raise NotImplementedError("Implementar esta función")

if __name__ == "__main__":
    import doctest
    luigi.run(["PrecioAvgMensual", "--local-scheduler"])
    doctest.testmod()
