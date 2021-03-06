def compute_daily_prices():
    """Compute los precios promedios diarios.

    Usando el archivo data_lake/cleansed/precios-horarios.csv, compute el prcio
    promedio diario (sobre las 24 horas del dia) para cada uno de los dias. Las
    columnas del archivo data_lake/business/precios-diarios.csv son:

    * fecha: fecha en formato YYYY-MM-DD

    * precio: precio promedio diario de la electricidad en la bolsa nacional



    """
    #raise NotImplementedError("Implementar esta función")
    import pandas as pd
    
    datos = pd.read_csv('data_lake/cleansed/precios-horarios.csv',index_col = None, header= 0)
    datos["Fecha"] = pd.to_datetime(datos["Fecha"], format= '%Y/%m/%d')
    datos = datos[["Fecha","precio"]]
    datos = datos.groupby(["Fecha"])["precio"].mean()
    datos.to_csv('data_lake/business/precios-diarios.csv',index=True)

if __name__ == "__main__":
    import doctest

    doctest.testmod()
    compute_daily_prices()
