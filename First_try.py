import numpy
import pandas as pd
from sklearn import linear_model
import numpy as np

data = pd.read_csv("TD.csv").values

X_init = []
Y_train = []

val = 0
for i in data:
    count = 0
    for j in i:
        count += 1
        val += 1
        if count == 1:
            X_init.append(val)
        elif count == 6:
            Y_train.append(j)

X_train = np.reshape(X_init, (-1, 1))

lm = linear_model.LinearRegression()

lm.fit(X_train, Y_train)

y_pred = lm.predict(X_train)

print(y_pred)

print(Y_train)
