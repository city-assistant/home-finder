import pandas as pd
import numpy as np
import json

from keras.layers import LSTM 
from keras.models import Sequential 
from keras.layers import Dense 
import keras.backend as K 
from keras.callbacks import EarlyStopping

import pandas as pd
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dropout, Dense, Activation
from pandas.io.parsers import read_csv

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

        mid_price = list(dataDfDict['서울특별시 강서구 공항동'][0])

        day_divided = 50
        day_length = day_divided + 1
        day_result = []

        for i in range(len(mid_price) - day_length):
            day_result.append(mid_price[i: i + day_length])

        norm_result = []
        for section in day_result:
            norm_section = [((float(p) / float(section[0])) - 1) for p in section]
            norm_result.append(norm_section)
        day_result = np.array(norm_result)

        train_data_rate = 0.7
        boundary = round(day_result.shape[0] * train_data_rate)
        train_data = day_result[:boundary, :]
        test_data = day_result[boundary:, :]

        x_train = train_data[:, :-1]
        x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
        y_train = train_data[:, -1]

        x_test = test_data[:, :-1]
        x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
        y_test = test_data[:, -1]

        model = Sequential()
        model.add(LSTM(50, return_sequences=True, input_shape=(50, 1)))
        model.add(LSTM(64, return_sequences=False))
        model.add(Dense(1, activation='relu'))
        model.compile(loss='mse', optimizer='sgd')

        model.fit(x_train, y_train,
            validation_data=(x_test, y_test),
            batch_size=10,
            epochs=20
            )
        pred = model.predict(x_test)
        self.result = [list(y_train) + list(y_test), list(y_train) + list(pred)]