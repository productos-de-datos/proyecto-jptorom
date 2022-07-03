
from pandas import to_datetime


def make_monthly_prices_plot():
    """Crea un grafico de lines que representa los precios promedios diarios.

    Usando el archivo data_lake/business/precios-diarios.csv, crea un grafico de
    lines que representa los precios promedios diarios.

    El archivo se debe salvar en formato PNG en data_lake/business/reports/figures/daily_prices.png.

    """
    #raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest
    import pandas as pd
    import matplotlib.pyplot as plt
    import numpy as np

    # Se obtienen los datos
    datos = pd.read_csv("data_lake/business/precios-mensuales.csv", header= 0)
    #Se ajusta el formato del campo Fecha
    datos['Fecha'] = pd.to_datetime(datos['Fecha'], format='%Y-%m-%d')
    # Se asignan a valores a los ejes
    x_values= datos["Fecha"]
    y_values = datos["precio"]

    plt.figure(figsize=(14, 4)) 
    plt.plot(x_values,y_values,"g")
    plt.ylabel("Precio")
    plt.xlabel("Fecha")
    plt.title("Precio Promedio Mensual de Energía")
    plt.savefig("data_lake/business/reports/figures/monthly_prices.png")

    #doctest.testmod()
if __name__ == "__main__":
    import doctest

    doctest.testmod()
    make_monthly_prices_plot()
