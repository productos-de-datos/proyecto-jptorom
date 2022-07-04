from pandas import read_csv
import pickle

def train_daily_model():
    """Entrena el modelo de pronóstico de precios diarios.

    Con las features entrene el modelo de proóstico de precios diarios y
    salvelo en models/precios-diarios.pkl


    """
    #raise NotImplementedError("Implementar esta función")
    import pandas as pd
    from sklearn.model_selection import train_test_split
    import numpy as np
    from sklearn.preprocessing import MinMaxScaler
    from sklearn.neural_network import MLPRegressor
    from sklearn.model_selection import train_test_split
    


    datos = pd.read_csv("data_lake/business/features/precios-diarios.csv", header= 0)
    datos['Fecha'] = pd.to_datetime(datos['Fecha'], format='%Y-%m-%d')
    datos['weekday'] = pd.to_numeric(datos["Fecha"].dt.weekday)
    x_values= datos["weekday"]
    y_values = datos["precio"]
    x_values= np.array(x_values).reshape(-1, 1)
    
    # Se asignan a valores a los ejes
    X_values= datos["Fecha"]
    X_values = np.array(X_values).reshape(-1,1)
    y_values = datos["precio"]

    np.random.seed =(123456)
    H = 2 #Se escoge arbitrariamente

    mlp = MLPRegressor(
        hidden_layer_sizes=(H,),
        activation="logistic",
        learning_rate="adaptive",
        momentum=0.0,
        learning_rate_init=0.1, #Forma en la que aprendemos
        max_iter=10000, #Realizar diez mil iteraciones
        )

# Se parten los datos en dos conjuntos de datos: train y test. Se utiliza el 20% de los datos paras testing.
    X_train, X_test, y_train , y_test = train_test_split(
        x_values,
        y_values,
        train_size = 0.8,
        test_size= 0.2,
        random_state = 12345
        )

    mlp.fit(X_train,y_train)

    with open("src/models/precios-diarios.pkl", "wb") as f:
        pickle.dump(mlp, f)
    


if __name__ == "__main__":
    import doctest
    train_daily_model()
    doctest.testmod()
