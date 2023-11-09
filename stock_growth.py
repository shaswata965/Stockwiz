import market_condition


def growth():
    arr = []
    stock_set = []
    stock_list = []
    length = []
    data = market_condition.condition(90)
    for i in data:
        if (len(i) % 365) != 0:
            num_sets = int((len(i) - (len(i) % 365)) / 365) + 1
        else:
            num_sets = int(len(i) / 365)
        num_data = len(i)
        length.append(num_sets)
        temp = []
        avg = []
        temp_data = []
        data_set = []
        count = 0
        for j in range(num_sets):
            for k in range(365):
                if count < num_data:
                    temp.append(i[count][7])
                    temp_data.append(
                        [i[count][0], i[count][1], i[count][2], i[count][3], i[count][4], i[count][5], i[count][6],
                         i[count][7]])
                    count += 1
                else:
                    break
            data_set.append(temp_data)
            temp_data = []
            avg.append((sum(temp) / len(temp)))
            temp = []
        arr.append(avg)
        stock_set.append(data_set)
        data_set = []

    growth_set = []
    for i in arr:
        temp_set = []

        for j in range(len(i) - 1):
            temp_set.append(((i[j + 1] - i[j]) / i[j]) * 100)
        growth_set.append(temp_set)

    growth_index = []

    for i in growth_set:
        temp_set = [0]
        for j in i:
            if j >= 6.5:
                temp_set.append(1)
            elif j < 6.5:
                temp_set.append(0)

        growth_index.append(temp_set)

    for i in range(len(stock_set)):
        for j in range(len(stock_set[i])):
            for k in stock_set[i][j]:
                k.append(growth_index[i][j])

    for i in stock_set:
        temp_list = []
        for j in i:
            for k in j:
                temp_list.append(k)

        stock_list.append(temp_list)

    return stock_list


growth()
