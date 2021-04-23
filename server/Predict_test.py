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
        train = df
        print(train)
        sc = MinMaxScaler()
        train_sc = sc.fit_transform(train)
        print(train_sc)
        train_sc_df = pd.DataFrame(train_sc, columns=['trade_price_idx_value'], index=train.index)
        print(train_sc_df)
        for s in range(1, 13):
            train_sc_df['shift_{}'.format(s)] = train_sc_df['trade_price_idx_value'].shift(s)
        print(train_sc_df)

        X_train = train_sc_df.dropna().drop('trade_price_idx_value', axis=1)
        y_train = train_sc_df.dropna()[['trade_price_idx_value']]

        X_train = X_train.values
        y_train = y_train.values

        X_train_t = X_train.reshape(X_train.shape[0], 12, 1)

        K.clear_session()
    
        model = Sequential() # Sequeatial Model 
        model.add(LSTM(20, input_shape=(12, 1))) # (timestep, feature) 
        model.add(Dense(1)) # output = 1 
        model.compile(loss='mean_squared_error', optimizer='adam') 
        model.summary()

        early_stop = EarlyStopping(monitor='loss', patience=1, verbose=1)

        model.fit(X_train_t, y_train, epochs=100,
        batch_size=30, verbose=1, callbacks=[early_stop])


        y_pred = model.predict(X_train_t[-2:], batch_size=32)
        print(X_train_t[-2:])
        print([X_train_t[-1]])
        # y_pred = model.predict(X_train_t[-12:], batch_size=32)
        y_pred_inversed = sc.inverse_transform(y_pred)
        print(y_pred_inversed)
        self.result = [v[0] for v in list(y_pred_inversed)]
