# -*- encoding:utf-8 -*-
import numpy as np
import heapq

# ############# 需要使用的数据 ###############
sex = [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0]    # F: 1, M:0
avg_trans = [8, 18, 5, 3, 11, 3, 9, 10, 7, 20, 22, 14, 10, 15, 13]
avg_payment = [301, 448, 305, 309, 522, 650, 490, 300, 274, 575, 530, 363, 409, 479, 445]
avg_silver = [4, 8, 9, 6, 10, 13, 5, 7, 12, 15, 9, 6, 8, 7, 11]
decision_dic = {1: "Remain", 2: "Downgrade", 3: "Upgrade"}
decision_ls = [1, 2, 1, 2, 1, 2, 3, 3, 2, 3, 2, 3, 1, 1, 1]
# print(len(sex), len(avg_trans), len(avg_payment), len(avg_silver))

# ############# 求各组属性最大最小值 ###############
max_avg_trans = max(avg_trans)
min_avg_trans = min(avg_trans)
max_avg_payment = max(avg_payment)
min_avg_payment = min(avg_payment)
max_avg_silver = max(avg_silver)
min_avg_silver = min(avg_silver)

# ############# 正规化各组属性值 ###############
normalization_fun = lambda input_ls, max_val, min_val: [(each_data - min_val)/(max_val - min_val) for each_data in input_ls]
normal_avg_trans = normalization_fun(avg_trans, max_avg_trans, min_avg_trans)
normal_avg_payment = normalization_fun(avg_payment, max_avg_payment, min_avg_payment)
normal_avg_silver = normalization_fun(avg_silver, max_avg_silver, min_avg_silver)
print("normalization avg_trans: {0}".format(normal_avg_trans))
print("normalization avg_payment: {0}".format(normal_avg_payment))
print("normalization avg_silver: {0}".format(normal_avg_silver))
print("******************************************************************"*2+"\n")

# ############# 正规化待测数据各个属性 ###############
sample = {"sex": 0, "avg_trans": 9, "avg_payment": 410, "avg_silver": 5}
sample_normal_avg_trans = (sample["avg_trans"] - min_avg_trans)/(max_avg_trans - min_avg_trans)
sample_normal_avg_payment = (sample["avg_payment"] - min_avg_payment)/(max_avg_payment - min_avg_payment)
sample_normal_avg_silver = (sample["avg_silver"] - min_avg_silver)/(max_avg_silver - min_avg_silver)
sample_sex = sample["sex"]
print("sample attributes normalization: avg_trans({0}), avg_payment({1}), avg_silver({2}), "
      "sex({3})".format(sample_normal_avg_trans,sample_normal_avg_payment, sample_normal_avg_silver, sample_sex))
print("******************************************************************"*2+"\n")

# ############# 计算欧氏距离 ###############
# 计算各个属性上的距离的平方:
distance_fun = lambda normal_ls, sample_data: [np.square(sample_data - each_data) for each_data in normal_ls]
distance_in_avg_trans = distance_fun(normal_avg_trans, sample_normal_avg_trans)
distance_in_avg_payment = distance_fun(normal_avg_payment, sample_normal_avg_payment)
distance_in_avg_silver = distance_fun(normal_avg_silver, sample_normal_avg_silver)
distance_in_sex = distance_fun(sex, sample_sex)
# print(distance_in_avg_trans)
# print(distance_in_avg_payment)
# print(distance_in_avg_silver)
# print(distance_in_sex)
# 计算最后距离:
overall_distance = []
for i in range(len(distance_in_avg_trans)):
    overall_distance.append(np.sqrt(distance_in_avg_trans[i] + distance_in_avg_payment[i] + distance_in_avg_silver[i] + distance_in_sex[i]))
print("every euclidean distance: {0}".format(overall_distance))
print("******************************************************************"*2+"\n")

# ############# 找到最小的k个数据 ###############
k = 5
min_k_ls = heapq.nsmallest(k, overall_distance)
index_smallest_distance = [overall_distance.index(each_distance) for each_distance in min_k_ls]
print("smallest K distances: {0}".format(min_k_ls))
print("smallest K index (first 0): {0}".format(index_smallest_distance))
print("smallest K items:")
for index in index_smallest_distance:
    print("\t" + decision_dic[decision_ls[index]])
