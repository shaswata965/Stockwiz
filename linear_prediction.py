
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np
import market_prediction

cur_set = market_prediction.train_data(0,'TD')[2]

X_train = market_prediction.train_data(cur_set - 2,'TD')[0]

X_train = np.array(X_train)

Y_train = market_prediction.train_data(cur_set - 2,'TD')[1]

Y_train = np.array(Y_train)

X_test = market_prediction.train_data(cur_set - 1,'TD')[0]

X_test = np.array(X_test)

Y_test = market_prediction.train_data(cur_set - 1,'TD')[1]

Y_test = np.array(Y_test)

lm = LinearRegression()

lm.fit(X_train, Y_train)

Y_pred = lm.predict(X_test)

print(lm.score(X_test,Y_test))

X_plot = []

for i in range(0,Y_test.shape[0]):
    X_plot.append(i)


X_plot = np.array(X_plot)

plt.plot(X_plot, Y_pred, c='b', label='Our Prediction')
plt.scatter(X_plot, Y_test, marker='x', c='r', label='Actual Values')
plt.title('Stock Prices')
plt.xlabel('Data-Point(Date)')
plt.ylabel('Price(opening)')
plt.legend()
plt.show()