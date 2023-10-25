import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression


def train_data(val):
    pima = pd.read_csv("TD.csv").values

    num_data = pima.shape[0]

    num_sets = int(((num_data - (num_data % 60)) / 60) + 1)

    set_list = []
    set_list2 = []

    count = 0
    for i in range(num_sets):
        n_array = []
        n_array2 = []
        for j in range(60):
            if count < num_data:
                temp_array = [pima[count][2], pima[count][3], pima[count][4], pima[count][5], pima[count][6]]
                temp_array2 = [pima[count][1]]
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

        if i == 20:
            v_count_end = 57

        for j in range(v_count_start, v_count_end):

            if set_list[i][j][0] <= base_value and s_count <= 120:
                set_list[i][j].append(0)
                s_count += 1
            else:
                set_list[i][j].append(1)
                base_value = set_list[i][j][0]
                s_count = 0
    # print(set_list[20])
    return set_list[val], set_list2[val], num_sets

# train_data()
