# -*- encoding:utf-8 -*-
# Name: SUN RUI    ID: 18083229g

import numpy as np
import heapq
from decimal import Decimal
import copy
from collections import Counter

def knn(k, target_sample, sex_train, avg_trans_train, avg_payment_train, avg_silver_train):
    # ############# find max and min  ###############
    max_avg_trans = max(avg_trans_train)
    min_avg_trans = min(avg_trans_train)
    max_avg_payment = max(avg_payment_train)
    min_avg_payment = min(avg_payment_train)
    max_avg_silver = max(avg_silver_train)
    min_avg_silver = min(avg_silver_train)

    round_fun = lambda x: float('{:.4f}'.format(Decimal(x)))
    # ############# normalize training data ###############
    normalization_fun = lambda input_ls, max_val, min_val: [round_fun((each_data - min_val)/(max_val - min_val)) for each_data in input_ls]
    normal_avg_trans = normalization_fun(avg_trans_train, max_avg_trans, min_avg_trans)
    normal_avg_payment = normalization_fun(avg_payment_train, max_avg_payment, min_avg_payment)
    normal_avg_silver = normalization_fun(avg_silver_train, max_avg_silver, min_avg_silver)
    print("normalization avg_trans: {0}".format(normal_avg_trans))
    print("normalization avg_payment: {0}".format(normal_avg_payment))
    print("normalization avg_silver: {0}".format(normal_avg_silver))
    print("..................................................................")

    # ############# normalize target sample ###############
    sample_normal_avg_trans = round_fun((target_sample["avg_trans"] - min_avg_trans)/(max_avg_trans - min_avg_trans))
    sample_normal_avg_payment = round_fun((target_sample["avg_payment"] - min_avg_payment)/(max_avg_payment - min_avg_payment))
    sample_normal_avg_silver = round_fun((target_sample["avg_silver"] - min_avg_silver)/(max_avg_silver - min_avg_silver))
    sample_sex = target_sample["sex"]
    print("sample attributes normalization: avg_trans({0}), avg_payment({1}), avg_silver({2}), "
          "sex({3})".format(sample_normal_avg_trans,sample_normal_avg_payment, sample_normal_avg_silver, sample_sex))
    print("..................................................................")

    # ############# calculate euclidean distance ###############
    # euclidean distance power 2 in every attribute:
    distance_fun = lambda normal_ls, sample_data: [round_fun(np.square(sample_data - each_data, dtype=np.float64)) for each_data in normal_ls]
    distance_in_avg_trans = distance_fun(normal_avg_trans, sample_normal_avg_trans)
    distance_in_avg_payment = distance_fun(normal_avg_payment, sample_normal_avg_payment)
    distance_in_avg_silver = distance_fun(normal_avg_silver, sample_normal_avg_silver)
    distance_in_sex = distance_fun(sex_train, sample_sex)

    # final euclidean distance:
    overall_distance = []
    for i in range(len(distance_in_avg_trans)):
        overall_distance.append(round_fun(np.sqrt(distance_in_avg_trans[i] + distance_in_avg_payment[i] + distance_in_avg_silver[i] + distance_in_sex[i], dtype=np.float64)))
    print("every euclidean distance: {0}".format(overall_distance))
    print("..................................................................")

    # ############# find min k samples ###############
    min_k_ls = heapq.nsmallest(k, overall_distance)
    index_smallest_distance = [overall_distance.index(each_distance) for each_distance in min_k_ls]
    print("smallest K distances: {0}".format(min_k_ls))
    print("smallest K index (first 0): {0}".format(index_smallest_distance))
    print("smallest K items:")
    final_des_ls = []
    for index in index_smallest_distance:
        final_des_ls.append(decision_dic[decision_ls[index]])
        print("\t" + decision_dic[decision_ls[index]])
    word_counts = Counter(final_des_ls)
    top_one = word_counts.most_common(1)
    return top_one[0][0]

# target_sample = {"sex": 0, "avg_trans": 9, "avg_payment": 410, "avg_silver": 5}

# ############# data ###############
sex = [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0]    # F: 1, M:0
avg_trans = [8, 18, 5, 3, 11, 3, 9, 10, 7, 20, 22, 14, 10, 15, 13]
avg_payment = [301, 448, 305, 309, 522, 650, 490, 300, 274, 575, 530, 363, 409, 479, 445]
avg_silver = [4, 8, 9, 6, 10, 13, 5, 7, 12, 15, 9, 6, 8, 7, 11]
decision_dic = {1: "Remain", 2: "Downgrade", 3: "Upgrade"}
decision_ls = [1, 2, 1, 2, 1, 2, 3, 3, 2, 3, 2, 3, 1, 1, 1]


def cal_accuracy_rate(k):
    count1 = 0
    for i in range(len(sex)):
        target_sample = {"sex": sex[i], "avg_trans": avg_trans[i], "avg_payment": avg_payment[i], "avg_silver": avg_silver[i]}
        sex_train = copy.deepcopy(sex)
        avg_trans_train = copy.deepcopy(avg_trans)
        avg_payment_train = copy.deepcopy(avg_payment)
        avg_silver_train = copy.deepcopy(avg_silver)
        sex_train.pop(i)
        avg_trans_train.pop(i)
        avg_payment_train.pop(i)
        avg_silver_train.pop(i)
        prediction = knn(k, target_sample, sex_train, avg_trans_train, avg_payment_train, avg_silver_train)
        real_value = decision_dic[decision_ls[i]]
        if real_value == prediction:
            count1 += 1
    round_fun = lambda x: float('{:.4f}'.format(Decimal(x)))
    # print(count1)
    accuracy_rate = round_fun(count1/(len(sex)-1)*100)
    return "{}%".format(accuracy_rate)

if __name__ == '__main__':
    k_ls = [1, 2, 3, 4, 5, 6]
    accuracy_dict = {}
    for k in k_ls:
        print("\n***************************************************************************")
        print("********************************** k = {0} **********************************".format(k))
        print("***************************************************************************")
        accuracy_rate = cal_accuracy_rate(k)
        accuracy_dict[k] = accuracy_rate
    for (k, v) in accuracy_dict.items():
        print("k = {0}, accuracy rate = {1}".format(k, v))
