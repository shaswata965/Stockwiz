import numpy
import pandas as pd
from matplotlib import pyplot as plt
from sklearn import linear_model
import numpy as np

data = pd.read_csv("TD.csv").values

X_init = []
Y_train = []

val = 0
last_val = 0
last_val_arr = []
for i in data:
    count = 0
    for j in i:
        count += 1
        val += 1
        if count == 1:
            X_init.append(val)
            last_val = val
        elif count == 6:
            Y_train.append(j)

for i in range(0, 10):
    last_val += 1
    last_val_arr.append(last_val)

X_Test = np.reshape(last_val_arr, (-1, 1))

X_train = np.reshape(X_init, (-1, 1))

lm = linear_model.LinearRegression()

lm.fit(X_train, Y_train)

y_pred = lm.predict(X_Test)

temp_f_wb = lm.intercept_ + lm.coef_*X_train

plt.plot(X_train, temp_f_wb, c='b', label='Our Prediction')
plt.scatter(X_train, Y_train, marker='x', c='r', label='Actual Values')
plt.title('Housing Prices')
plt.xlabel('Size(in 1000 sqft)')
plt.ylabel('Price(in 1000 dollar)')
plt.legend()
plt.show()

print(y_pred)

print(Y_train)