import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import json

from keras.layers import LSTM 
from keras.models import Sequential 
from keras.layers import Dense 
import keras.backend as K 
from keras.callbacks import EarlyStopping

class Predict:
    def __init__(self):
        self.result = []

    def action(self, injectedDatas):
        df = pd.DataFrame(injectedDatas)

        forForecast = df.iloc[-12:]
        train = df

        sc = MinMaxScaler()

        forForecast_sc = sc.fit_transform(forForecast)
        train_sc = sc.fit_transform(train)

        print(forForecast_sc)
        print(train_sc)

        # forForecast_sc_df = pd.DataFrame([forForecast_sc], columns=['trade_price_idx_value'], index=train.index)
        train_sc_df = pd.DataFrame(train_sc, columns=['trade_price_idx_value'], index=train.index)

        for s in range(1, 13):
            # forForecast_sc_df['shift_{}'.format(s)] = train_sc_df['trade_price_idx_value'].shift(s)
            train_sc_df['shift_{}'.format(s)] = train_sc_df['trade_price_idx_value'].shift(s)

        X_train = train_sc_df.dropna().drop('trade_price_idx_value', axis=1)
        y_train = train_sc_df.dropna()[['trade_price_idx_value']]

        # X_forecast = forForecast_sc_df.dropna().drop('trade_price_idx_value', axis=1)
        # y_forecast = forForecast_sc_df.dropna()[['trade_price_idx_value']]

        X_train = X_train.values
        y_train = y_train.values

        # X_forecast = X_forecast.values
        # y_forecast = y_forecast.values

        X_train_t = X_train.reshape(X_train.shape[0], 12, 1)

        # X_forecast_t = X_forecast.reshape(X_forecast.shape[0],12,1)

        K.clear_session()
    
        model = Sequential() # Sequeatial Model 
        model.add(LSTM(20, input_shape=(12, 1))) # (timestep, feature) 
        model.add(Dense(1)) # output = 1 
        model.compile(loss='mean_squared_error', optimizer='adam') 
        model.summary()

        early_stop = EarlyStopping(monitor='loss', patience=1, verbose=1)

        model.fit(X_train_t, y_train, epochs=100,
        batch_size=30, verbose=1, callbacks=[early_stop])

        maxChange = max(injectedDatas)

        # y_pred = np.ndarray([])
        print(X_train)
        y_pred = model.predict(X_train_t[-12:], batch_size=32)
        # test_pred = model.predict(X_forecast_t, batch_size=32)

        # print(test_pred)

        # print(sc.inverse_transform([v[0] for v in list(y_pred * maxChange)]))
        self.result = [v[0] for v in list(y_pred * maxChange)]

        # x_input = np.ndarray(injectedDatas[-12:], dtype=np.float64)
        # x_input = x_input.reshape((1, 12, 1))
        # yhat = model.predict(x_input, verbose=0)
        # print(yhat)
