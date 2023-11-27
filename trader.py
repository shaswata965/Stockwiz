import linear_prediction
import yfinance as yf


def trade(trader_set):
    for i in trader_set:
        stock_bought = i[4]
        high = linear_prediction.prediction(1, i[0])
        high_high = high[0]
        high_low = high[1]

        low = linear_prediction.prediction(2, i[0])
        low_high = low[0]
        low_low = low[1]

        ticker = yf.Ticker(i[0])

        # data = ticker.history(period='1d')
        #
        # open_price = data['Close'].iloc[0]
        current_price = ticker.info['currentPrice']

        stock_number = int(i[3] / current_price)
        remaining = i[3] - (stock_number * current_price)
        print(high_low)
        print(current_price)
        print(low_low)
        print(low_high)

        if current_price <= low_low and current_price < high_low:
            print("Buy " + i[0])
            i[6] = current_price
            stock_bought, i[4] = stock_number
            i[3] = remaining
        elif low_high >= current_price >= low_low and current_price < high_low:
            print("Buy " + i[0])
            i[6] = current_price
            stock_bought, i[4] = stock_number
            i[3] = remaining
        elif current_price >= high_low and current_price >= i[6] and i[4] != 0:
            print("Sell " + i[0])
            stock_sold = i[4]
            profit = stock_sold * current_price - stock_sold * i[6]
            i[4] = 0
            i[5] = profit
            i[3] = stock_sold * i[6]

            print("No action for " + i[0])

    return trader_set
