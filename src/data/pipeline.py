"""
Construya un pipeline de Luigi que:
* Importe los datos xls
* Transforme los datos xls a csv
* Cree la tabla unica de precios horarios.
* Calcule los precios promedios diarios
* Calcule los precios promedios mensuales
En luigi llame las funciones que ya creo.
"""
 
import luigi 
from luigi import Task, LocalTarget 
 
class IngresoDatos(Task): 
    def output(self): 
        return LocalTarget('data_lake/landing/arc.csv') 
 
    def run(self): 
        from ingest_data import ingest_data 
        with self.output().open('w') as archivos: 
            ingest_data() 
 
 
class TransformacionDatos(Task): 
    def requires(self): 
        return IngresoDatos() 
 
    def output(self): 
        return LocalTarget('data_lake/raw/arc.txt') 
 
    def run(self): 
        from transform_data import transform_data 
        with self.output().open('w') as archivos: 
            transform_data() 
 
 
class LimpiezaDatos(Task): 
    def requires(self): 
        return TransformacionDatos() 
 
    def output(self): 
        return LocalTarget('data_lake/cleansed/arc.txt') 
 
    def run(self): 
        from clean_data import clean_data 
        with self.output().open('w') as archivos: 
            clean_data() 
 
 
class PrecioAvgDiario(Task): 
    def requires(self): 
        return LimpiezaDatos() 
 
    def output(self): 
        return LocalTarget('data_lake/business/arc.txt') 
 
    def run(self): 
        from compute_daily_prices import compute_daily_prices 
        with self.output().open('w') as archivos: 
            compute_daily_prices() 
 
 
class PrecioAvgMensual(Task): 
    def requires(self): 
        return PrecioAvgDiario() 
 
    def output(self): 
        return LocalTarget('data_lake/business/arc.txt') 
 
    def run(self): 
        from compute_monthly_prices import compute_monthly_prices 
        with self.output().open('w') as archivos: 
            compute_monthly_prices() 
 
 
if __name__ == '__main__': 
    luigi.run(["PrecioAvgMensual", "--local-scheduler"]) 
 
if __name__ == "__main__": 
    import doctest 
    doctest.testmod()
