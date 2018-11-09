# -*- encoding:utf-8 -*-

# Name: SUN RUI    ID:18083229g

import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.cluster import KMeans


def load_data(file_path):
    df_data = pd.read_csv(file_path)
    df_data.columns = ["Age", "Sex", "MonthlyIncome", "MaritalStatus",	"ServicePlan", "ExtraUsage"]
    scaled_data = preprocessing.scale(df_data)
    return scaled_data


def do_k_means(data):
    centers = np.vstack((data[0], data[7], data[14]))
    k_means = KMeans(n_clusters=3, init=centers, n_init=1, max_iter=1000)
    return k_means.fit_predict(data), k_means.fit(data).cluster_centers_

def print_clusters(cluster_index):
    cluster_dict = {0:[],1:[],2:[]}
    for i in range(len(cluster_index)):
        cluster_dict[cluster_index[i]].append(i+1)
    print("cluster result: {}".format(cluster_dict))

if __name__ == '__main__':
    df_scaled_data = load_data("data.csv")
    cluster_index, cluster_center = do_k_means(df_scaled_data)
    print("cluster index: {}".format(cluster_index))
    print_clusters(cluster_index)
    print("cluster centers:\n{}".format(cluster_center))

# print(cluster_index)
# print(scaled_data[:, 0])
# df_data["Age"] = scaled_data[:, 0]
# df_data["Sex"] = scaled_data[:, 1]
# df_data["MonthlyIncome"] = scaled_data[:, 2]
# df_data["MaritalStatus"] = scaled_data[:, 3]
# df_data["ServicePlan"] = scaled_data[:, 4]
# df_data["ExtraUsage"] = scaled_data[:, 5]
# df_data["cluster"] = cluster_index
# df_data.to_csv("data_2.csv")
