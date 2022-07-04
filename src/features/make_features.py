def make_features():
    import pandas as pd
    import numpy as np
    
    df_daily = pd.read_csv('data_lake/business/precios-diarios.csv')
    df_daily['log_precio'] = np.log(df_daily_prices['precio'])
    df_daily['precio_log_12'] = df_daily_prices.precio.shift(12)
    df_daily['log_precio_log_12'] = np.log(df_daily_prices['precio_lag_12'])
    df_daily.to_csv('data_lake/business/features/precios-diarios.csv', index=False)

import pytest
def test_make_features():
    import pandas as pd

    make_features()

    df_to_test = pd.read_csv('data_lake/business/features/precios-diarios.csv')

    assert df_to_test.empty is False


if __name__ == "__main__":
    import doctest
    make_features()
    doctest.testmod()
