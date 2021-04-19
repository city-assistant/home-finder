import numpy
import matplotlib.pyplot as plt
import pandas
import math
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error

class Predict:
    def __init__(self):
        self.result = []

    def action(self):
        dataDfDict ={}
        with open('C:\ITStudy\home-finder\RealEstateTransactionKorea-master\cityTranslatedData.json', 'r', encoding='utf-8') as f:
            json_data = json.load(f)
        for key in json_data.keys():
            for i in range(len(json_data[key]['datas'])):
                if json_data[key]['datas'][i] == "":
                    json_data[key]['datas'][i] = json_data[key]['datas'][i-1]
            dataDfDict[key] = pd.DataFrame(json_data[key]['datas'], json_data[key]['labels'])

        df = dataDfDict['서울특별시 마포구 상수동']

        # forForecast = df
        train = df

        sc = MinMaxScaler()

        train_sc = sc.fit_transform(train)

        train_sc_df = pd.DataFrame(train_sc, columns=['trade_price_idx_value'], index=train.index)

        for s in range(1, 13):
            # forForecast_sc_df['shift_{}'.format(s)] = train_sc_df['trade_price_idx_value'].shift(s)
            train_sc_df['shift_{}'.format(s)] = train_sc_df['trade_price_idx_value'].shift(s)

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

        # early_stop = EarlyStopping(monitor='loss', patience=1, verbose=1)

        model.fit(X_train_t, y_train, epochs=100,
        batch_size=30, verbose=1)
        # batch_size=30, verbose=1, callbacks=[early_stop])

        maxChange = max(train[0])

        y_pred = model.predict(X_test_t, batch_size=32)

        self.result = [list(y_train * maxChange) + list(y_pred * maxChange)]