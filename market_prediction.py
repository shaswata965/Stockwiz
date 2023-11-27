
from yahoo_fin.stock_info import *


def train_data(val, name, prediction):
    from datetime import datetime, timedelta
    currDate = datetime.now()

    endDate = currDate.date() - timedelta(days=1)
    startDate = currDate.date() - timedelta(days=365 * 5)

    # file_set = market_condition.file_name()
    # file_num = ''
    # for h in range(len(file_set)):
    #     if file_set[h][0] == name:
    #         file_num = file_set[h][1]
    # file_set.clear()

    pima = get_data(name, startDate, endDate).values

    num_data = pima.shape[0]
    if (num_data % 60) != 0:
        num_sets = int(((num_data - (num_data % 60)) / 60) + 1)
    else:
        num_sets = int((num_data / 60))

    set_list = []
    set_list2 = []
    set_list3 = []

    count = 0
    for i in range(num_sets):
        n_array = []
        n_array2 = []
        pred_array = []
        for j in range(60):
            if (count + 1) < num_data:
                temp_array = [pima[count][0], pima[count][1], pima[count][2], pima[count][3], pima[count][4],
                              pima[count][5]]
                temp_array2 = [pima[count + 1][prediction]]
                count += 1
                n_array.append(temp_array)
                n_array2.append(temp_array2)
            else:
                pred_array = [pima[count][0], pima[count][1], pima[count][2], pima[count][3], pima[count][4],
                              pima[count][5]]
                break

        set_list.append(n_array)
        set_list2.append(n_array2)
        if pred_array:
            set_list3.append(pred_array)

        n_array = []
        n_array2 = []

    v_count_start = 0
    v_count_end = 60
    s_count = 0
    indicator = 0
    base_value = set_list[0][0][0]

    for i in range(len(set_list)):

        if i == num_sets - 1:
            v_count_end = len(set_list[num_sets - 1])

        for j in range(v_count_start, v_count_end):

            if set_list[i][j][0] <= base_value and s_count <= 120:
                set_list[i][j].append(0)
                s_count += 1
                indicator = 0
            else:
                set_list[i][j].append(1)
                base_value = set_list[i][j][0]
                s_count = 0
                indicator = 1

    set_list3[0].append(indicator)

    return set_list[val], set_list2[val], num_sets, set_list3
