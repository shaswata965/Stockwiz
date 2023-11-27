from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np
import market_prediction


def prediction(predict, stock_name):
    cur_set = market_prediction.train_data(0, stock_name, predict)[2]

    X_train = market_prediction.train_data(cur_set - 2, stock_name, predict)[0]

    X_train = np.array(X_train)

    Y_train = market_prediction.train_data(cur_set - 2, stock_name, predict)[1]

    Y_train = np.array(Y_train)

    X_test = market_prediction.train_data(cur_set - 1, stock_name, predict)[0]

    Y_test = market_prediction.train_data(cur_set - 1, stock_name, predict)[1]

    lm = LinearRegression()

    lm.fit(X_train, Y_train)

    X_test = (np.array(X_test))
    Y_test = np.array(Y_test)

    Y_pred = lm.predict(X_test)

    margin = 1-lm.score(X_test, Y_test)

    X_plot = []

    for i in range(0, Y_test.shape[0]):
        X_plot.append(i)

    X_plot = np.array(X_plot)

    plt.plot(X_plot, Y_pred, c='b', label='Our Prediction')
    plt.scatter(X_plot, Y_test, marker='x', c='r', label='Actual Values')
    plt.title('Stock Prices')
    plt.xlabel('Data-Point(Date)')
    plt.ylabel('Price(opening)')
    plt.legend()
    plt.show()

    X_train = market_prediction.train_data(cur_set - 1, stock_name, predict)[0]

    X_train = np.array(X_train)

    Y_train = market_prediction.train_data(cur_set - 1, stock_name, predict)[1]

    Y_train = np.array(Y_train)

    X_test = market_prediction.train_data(cur_set - 1, stock_name, predict)[3]
    lm.fit(X_train, Y_train)
    X_test = (np.array(X_test))
    Y_pred = lm.predict(X_test)



    val = Y_pred[0][0]


    return (val)
