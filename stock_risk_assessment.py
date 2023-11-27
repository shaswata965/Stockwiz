import tensorflow as tf
import numpy as np
from yahoo_fin.stock_info import *

Sequential = tf.keras.models.Sequential
Dense = tf.keras.layers.Dense

import stock_growth


def risk_assess():

    from datetime import datetime, timedelta

    data_set, label = stock_growth.growth()

    files = ['RY.TO', 'TD.TO', 'SHOP.TO', 'CNQ.TO', 'CNR.TO', 'ENB.TO', 'TRI.TO', 'BMO.TO',
             'BN.TO', 'ATD.TO', 'CSU.TO', 'NVEI.TO', 'DOO.TO', 'GSY.TO', 'ATZ.TO', 'BHC.TO',
             'LSPD.TO', 'T.TO', 'WEED.TO', 'SOY.TO']

    predict_set = []


    for i in files:
        currDate = datetime.now()
        endDate = currDate.date() - timedelta(days=1)
        startDate = currDate.date() - timedelta(days=365 * 5)

        pima = get_data(i, startDate, endDate).values

        temp_array = []
        temp_array.append(pima[0][6])

        def get_info(name):
            x = []
            y = []
            for u in data_set:
                for j in u:
                    if j[6] == name:
                        j = [x for x in j if x != name]
                        x.append(j)

            for u in label:
                a = len(u) - 1
                if u[a] == name:
                    y = [x for x in u if x != name]

            return x, y

        X, y = get_info(pima[0][6])

        tf.random.set_seed(42)
        np.random.seed(42)

        split_point = int(len(X) * .995)

        Xtr = X[:split_point]
        Xte = X[split_point:]

        X_training = np.array(Xtr)
        X_test = np.array(Xte)

        ytr = y[:split_point]

        y_training = np.array(ytr)

        model = Sequential([
            Dense(5, activation='sigmoid', input_shape=[8]),
            Dense(2, activation='relu'),
            Dense(1, activation='linear')
        ])

        model.compile(
            optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
            loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
        )

        model.fit(
            X_training, y_training,
            epochs=100,
            shuffle=True,
            verbose=0
        )

        prediction = model.predict(X_test)
        rating = 0

        temp_array.append(prediction[0][0])

        if 0.0 <= prediction[0] < 0.2:
            rating = 5
        elif 0.2 <= prediction[0] < 0.4:
            rating = 6
        elif 0.4 <= prediction[0] < 0.6:
            rating = 7
        elif 0.6 <= prediction[0] < 0.8:
            rating = 8
        elif 0.8 <= prediction[0] < 1.0:
            rating = 9
        elif prediction[0] >= 1.0:
            rating = 10
        elif -1.0 <= prediction[0] < 0:
            rating = 4
        elif -5.0 < prediction[0] < -1.0:
            rating = 3
        elif prediction[0] <= -5.0:
            rating = 0

        temp_array.append(rating)

        predict_set.append(temp_array)


    final_set = sorted(predict_set, key=lambda x: x[1], reverse=True)

    return (final_set)
