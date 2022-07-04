import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.neural_network import MLPRegressor
import pickle
def train_daily_model():
    """Entrena el modelo de pronóstico de precios diarios.
    Con las features entrene el modelo de proóstico de precios diarios y
    salvelo en models/precios-diarios.pkl
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

    #Preparación de los datos
    P=13 # Cantidad de retardos que miramos hacía atrás
    X=[] #lista vacia en la cual se agrega comprenhension. Dataframe que usamos para entrenamiento y validación
    for t in range(P-1,9409-1):  # Se recorre el indice de los datos
        X.append([data_scaled[t-n]for n in range(P)])
    observed_scaled = data_scaled[P:]

    # Tenemos 9396 patrones para entrenamiento
    np.random.seed =(123456)
    H = 1 #Se escoge arbitrariamente, número de neuronas en la capa oculta.

    mlp = MLPRegressor(
        hidden_layer_sizes=(H,),
        activation="logistic",
        learning_rate="adaptive",
        momentum=0.0,
        learning_rate_init=0.1, #Forma en la que aprendemos
        max_iter=10000, #Realizar diez mil iteraciones
        )

    mlp.fit(X[0:7057],observed_scaled[0:7057]) #9409-2352=7057

    pickle.dump(mlp, open('src/models/precios-diarios.pkl', 'wb'))

if __name__ == "__main__":
    import doctest
    train_daily_model()
    doctest.testmod()
