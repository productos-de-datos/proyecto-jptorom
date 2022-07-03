def make_monthly_prices_plot(): 
    """Crea un grafico de lines que representa los precios promedios mensuales. 
 
    Usando el archivo data_lake/business/precios-mesuales.csv, crea un grafico de 
    lines que representa los precios promedios mensuales. 
 
    El archivo se debe salvar en formato PNG en data_lake/business/reports/figures/daily_prices.png. 
 
    """ 
    import pandas as pd
    import matplotlib.pyplot as plt

    precios_mensuales = pd.read_csv('data_lake/business/precios-mensuales.csv')
    precios_mensuales['Fecha'] = pd.to_datetime(precios_mensuales["Fecha"])

    x = precios_mensuales['Fecha']
    y = precios_mensuales['precio']

    plt.figure(figsize=(10, 4)) 
    plt.plot(x, y, label='Promedio Mensual') 
    plt.title('Precio Promedio Mensual') 
    plt.xlabel('Fecha') 
    plt.ylabel('Precio') 
    plt.savefig("data_lake/business/reports/figures/monthly_prices.png") 
    
 
if __name__ == "__main__": 
    import doctest 
    
    doctest.testmod() 
    make_monthly_prices_plot()
