import pandas as pd
import market_condition

def train_data(val,name):
    file_set = market_condition.file_name()
    file_num = ''
    print(len(file_set))
    for h in range(len(file_set)):
        if file_set[h] == name:
            file_num = "File"+ str(h+1)+".csv"
    file_set.clear()
    pima = pd.read_csv("data/"+file_num).values

    num_data = pima.shape[0]
    if(num_data%60)!= 0:
        num_sets = int(((num_data - (num_data % 60)) / 60) + 1)
    else:
        num_sets = int((num_data / 60))

    set_list = []
    set_list2 = []

    count = 0
    for i in range(num_sets):
        n_array = []
        n_array2 = []
        for j in range(60):
            if count < num_data:
                temp_array = [pima[count][1], pima[count][2], pima[count][3], pima[count][4], pima[count][6]]
                temp_array2 = [pima[count][5]]
                count += 1
                n_array.append(temp_array)
                n_array2.append(temp_array2)
            else:
                break

        set_list.append(n_array)
        set_list2.append(n_array2)

        n_array = []
        n_array2 = []

    v_count_start = 0
    v_count_end = 60
    s_count = 0
    base_value = set_list[0][0][0]

    for i in range(len(set_list)):

        if i == num_sets-1:
            v_count_end = len(set_list[num_sets-1])

        for j in range(v_count_start, v_count_end):

            if set_list[i][j][0] <= base_value and s_count <= 120:
                set_list[i][j].append(0)
                s_count += 1
            else:
                set_list[i][j].append(1)
                base_value = set_list[i][j][0]
                s_count = 0

    return set_list[val], set_list2[val], num_sets