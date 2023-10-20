import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression

pima = pd.read_csv("TD.csv").values

num_data = pima.shape[0]

num_sets = int(((num_data - (num_data % 60)) / 60) + 1)

set_list = []

count = 0
for i in range(num_sets):
    n_array = []
    for j in range(60):
        if count < num_data:
            temp_array = [pima[count][5], pima[count][6]]
            count += 1
            n_array.append(temp_array)
        else:
            break

    set_list.append(n_array)

    n_array = []

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

for i in set_list:
    for j in i:
        print(j)
