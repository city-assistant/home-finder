import pandas as pd
import numpy as np
from numpy import array
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
        self.test = []

    def action(self, injectedDatas):
        print(injectedDatas)
        x,y = [], []
        for i in range(len(injectedDatas)-12):
            x.append(injectedDatas[i:i+12])
            y.append(injectedDatas[i+12])

        x, y = array(x), array(y)

        x_train = x
        y_train = y

        x_train = x_train.reshape((x_train.shape[0], x_train.shape[1], 1))
        x = x.reshape((x.shape[0], x_train.shape[1], 1))

        model = Sequential()
        model.add(LSTM(20, activation = 'relu', input_shape=(12,1)))
        model.add(Dense(1))
        model.compile(optimizer='adam', loss='mean_squared_error')
        model.summary()

        early_stop = EarlyStopping(monitor='loss', patience=1, verbose=1)

        model.fit(x_train, y_train, epochs=100, batch_size=1, callbacks=[early_stop])
        
        testList = []

        nextArray = x[-13:-12].copy()
        for i in range(12):
            ytest = model.predict(nextArray)
            nextArray = np.append(np.delete(nextArray[0], 0), ytest).reshape(1,12,1)
            testList.append(nextArray[0][-1][0])


        answerList = []

        nextArray = x[-1:].copy()
        for i in range(12):
            ytest = model.predict(nextArray)
            nextArray = np.append(np.delete(nextArray[0], 0), ytest).reshape(1,12,1)
            answerList.append(nextArray[0][-1][0])

        self.test = testList
        self.result = answerList
