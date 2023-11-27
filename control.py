from datetime import datetime
import time
import sys

import linear_prediction
import stock_risk_assessment
import trader

num = 0

setter = 0

while setter == 0:
    val = int(input("What would you like to do Today?"+"\n"+"Press 1: For Getting Today's Stock Forecast"+"\n"+
                    "Press 2: For Auto trading"))

    if val == 1:
        opt = int(input("\n"+"Press 0: For predicted High Price"+"\n"+
                        "Press 1: For predicted Low Price"+"\n"+
                        "Press 2: For predicted Closing Price"+"\n"+
                        "Press 3: For predicted Adjusted Closing Price"+"\n"+
                        "Press 4: To return to First Menu"))
        if opt == 0:
            print("x")
            setter = 1
        else:
            print("y")
            setter = 1

    else:
        budget = int(input('Enter Budget: '))
        stock_set = stock_risk_assessment.risk_assess()
        trader_set = []

        for i in range(len(stock_set)):
            if stock_set[i][1] >= 6:
                num = i
                break
        total_div = 0
        for j in range(num, num + 5):
            trader_set.append(stock_set[j])
            total_div += stock_set[j][2]

        for i in trader_set:
            bud_each = (budget / total_div) * i[2]
            i.append(bud_each)
            i.append(0)
            i.append(0)
            i.append(0)

        start_time = datetime.strptime("16:00", "%H:%M")
        cur = datetime.now().strftime("%H:%M")
        cur_time = datetime.strptime(cur, "%H:%M")

        if cur_time < start_time:
            dif = start_time - cur_time
        else:
            print("The time to trade is up, please try again tomorrow")
            sys.exit()

        iterations = int(dif.total_seconds() // 600)


        def start_trading(trader_set, iterations):
            cur_set = trader_set

            for k in range(iterations):
                cur_set = trader.trade(cur_set)
                time.sleep(600)
            return cur_set


        final_set = start_trading(trader_set, iterations)

        setter = 1
