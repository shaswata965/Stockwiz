import pandas as pd
import os

data_list = []
close_list = []
file_set = []
def condition(q):
    dir_path = "data"
    files = os.listdir(dir_path)
    arr = []
    data_set = []
    stock_set = []
    stock_list = []
    cond = []
    for i in range(len(files)):
        pima = pd.read_csv(dir_path + "/" + files[i]).values
        num_data = pima.shape[0]
        file_data = []
        file_data.append(pima[0][7])
        file_data.append(files[i])
        file_set.append(file_data)
        if(num_data%q != 0):
            num_sets = int((num_data - (num_data % q)) / q) + 1
        else:
            num_sets = int(num_data / q)
        temp = []
        avg = []
        temp_data = []
        count = 0
        for z in range(num_data):
            temp.append(pima[z][5])
        close_list.append(temp)
        temp = []
        for j in range(num_sets):
            for k in range(q):
                if count < num_data:
                    temp.append(pima[count][5])
                    temp_data.append(
                        [pima[count][1], pima[count][2], pima[count][3], pima[count][4], pima[count][6], pima[count][7]])
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

    lens = []

    for i in range(len(arr)):
        lens.append(len(arr[i]))

    length = max(lens)

    for m in range(len(arr)):
        temp = []
        l = len(arr[m])
        if l != length:
            for n in range(length - l):
                temp.append(n)

        for k in temp:
            arr[m].insert(k, 0)

    sets = [[] for i in range(length)]

    for i in arr:
        for j in range(len(i)):
            sets[j].append(i[j])

    indi = []
    for i in sets:
        avg = sum(i) / len(i)
        indi.append(avg)

    base = indi[0]

    for i in range(len(indi)):
        if indi[i] > base:
            cond.append(1)
            base = indi[i]
        elif indi[i] < base:
            cond.append(0)
        else:
            cond.append(1)


    for i in range(len(stock_set)):
        for j in range(len(stock_set[i])):
            for k in range(len(stock_set[i][j])):
                stock_set[i][j][k].append(cond[j])



    for i in stock_set:
        temp_list = []
        for j in i:
            for k in j:
                temp_list.append(k)

        stock_list.append(temp_list)

    for i in range(len(stock_list)):
        for j in range(len(stock_list[i])):
            stock_list[i][j].append(close_list[i][j])

    return stock_list,file_set

def file_name():
    file_set = condition(90)[1]
    return file_set

