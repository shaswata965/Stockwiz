import os

import pandas as pd
import tensorflow as tf
import numpy as np

Sequential = tf.keras.models.Sequential
Dense = tf.keras.layers.Dense

import stock_growth

def risk_assess():
    data_set, label = stock_growth.growth()

    dir_path = "data"

    files = os.listdir(dir_path)

    predict_set = []
    sort_set = []

    for i in files:

        pima = pd.read_csv("data/" + i).values

        temp_array = []
        temp_array.append(pima[0][7])


        def get_data(name):
            x = []
            y = []
            for i in data_set:
                for j in i:
                    if j[5] == name:
                        j = [x for x in j if x != name]
                        x.append(j)

            for i in label:
                a = len(i) - 1
                if i[a] == name:
                    y = [x for x in i if x != name]

            return x, y


        X, y = get_data(pima[0][7])

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
        sort_set.append(prediction[0][0])

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

    sort_set = sorted(sort_set, key=lambda x: x, reverse=True)

    final_set = sorted(predict_set, key=lambda x: x[1], reverse=True)

    return(final_set)


