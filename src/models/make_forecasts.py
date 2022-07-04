import pandas as pd
import pickle
import numpy as np
from sklearn.preprocessing import MinMaxScaler
def make_forecasts():
    """Construya los pronosticos con el modelo entrenado final.

    Cree el archivo data_lake/business/forecasts/precios-diarios.csv. Este
    archivo contiene tres columnas:

    * La fecha.

    * El precio promedio real de la electricidad.

    * El pronóstico del precio promedio real.


    """
    #raise NotImplementedError("Implementar esta función")
    datos= pd.read_csv('data_lake/business/features/precios-diarios.csv',index_col = None, header= 0)
    
    # Se ajusta el formato de la columna fecha
    datos["Fecha"] = pd.to_datetime(datos["Fecha"], format= '%Y/%m/%d')
    
    # Se establece la columna fecha como indice para poder hacer uso de las funcionalidades de pandas
    datos = datos.set_index("Fecha")
    datos = datos.sort_index()

    #Serie escalada entre 0 y 1
    scaler = MinMaxScaler()
    data_scaled = scaler.fit_transform(np.array(datos).reshape(-1,1))
    data_scaled = [u[0] for u in data_scaled] #Lista de listas porque es lo que espera sklearn

    P=13 # Cantidad de retardos que miramos hacía atrás
    X=[] #lista vacia en la cual se agrega comprenhension. Dataframe que usamos para entrenamiento y validación
    for t in range(P-1,9409-1):  # Se recorre el indice de los datos
        X.append([data_scaled[t-n]for n in range(P)])
    observed_scaled = data_scaled[P:]

    mlp = pickle.load(open('src/models/precios-diarios.pkl', 'rb'))

    y_scaled_m1 = mlp.predict(X)
    y_m1= scaler.inverse_transform([[u] for u in y_scaled_m1])
    y_m1 =[u[0] for u in y_m1]
    data = datos[13:]
    data["pronóstico"]= y_m1
    data.to_csv('data_lake/business/forecasts/precios-diarios.csv', index=True)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    make_forecasts()
