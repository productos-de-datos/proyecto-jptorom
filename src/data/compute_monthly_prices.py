def compute_monthly_prices():
    """Compute los precios promedios mensuales.

    Usando el archivo data_lake/cleansed/precios-horarios.csv, compute el prcio
    promedio mensual. Las
    columnas del archivo data_lake/business/precios-mensuales.csv son:

    * fecha: fecha en formato YYYY-MM-DD

    * precio: precio promedio mensual de la electricidad en la bolsa nacional



    """
    #raise NotImplementedError("Implementar esta función")

    import pandas as pd

    # Se carga la data
    readfile = pd.read_csv('data_lake/cleansed/precios-horarios.csv')
    # Se toman únicamente las columnas Fecha y precio
    readfile = readfile[["Fecha","precio"]]
    # Se convierte el formato del campo Fecha
    readfile["Fecha"] = pd.to_datetime(readfile["Fecha"], format="%Y/%m/%d")
    # Se cambia el día de cada fecha, colocando el primer día de cada mes
    readfile["Fecha"] = readfile["Fecha"].dt.to_period("M").dt.to_timestamp()
    # Se agrupa por fecha y se saca la media del precio
    df = readfile.groupby(["Fecha"]).mean().reset_index()
    # Se convierte el dataframe a formato csv y se guarda en la carpeta businees
    df.to_csv('data_lake/business/precios-mensuales.csv',index=False)
    return df


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    compute_monthly_prices()
