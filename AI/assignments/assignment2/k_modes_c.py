# -*- encoding:utf-8 -*-

# Name: SUN RUI    ID:18083229g

import pandas as pd
import numpy as np
from kmodes.kmodes import KModes
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from mpl_toolkits.mplot3d import Axes3D

def load_data(file_path):
    df_data = pd.read_csv(file_path)
    df_data.columns = ["Age", "Sex", "MonthlyIncome", "MaritalStatus",	"ServicePlan", "ExtraUsage"]
    one_hot_data = np.array(pd.get_dummies(df_data))
    return one_hot_data

def do_k_modes(data):
    centroids = np.vstack((data[0], data[7], data[14]))
    k_modes = KModes(n_clusters=3, init=centroids, n_init=1, max_iter=10000)
    return k_modes.fit_predict(data), k_modes.cluster_centroids_

def plot_distribution_2D(cluster_index, data, cluster_center2):
    cluster0 = []
    cluster1 = []
    cluster2 = []
    for i in range(len(cluster_index)):
        if cluster_index[i] == 0:
            cluster0.append(data[i])
        if cluster_index[i] == 1:
            cluster1.append(data[i])
        if cluster_index[i] == 2:
            cluster2.append(data[i])
    color_ls = ["red", "green", "blue"]
    all_clusters = [cluster0, cluster1, cluster2]
    for each_cluster, color in zip(all_clusters, color_ls):
        for each_item in each_cluster:
            X = each_item[0]
            Y = each_item[1]
            plt.scatter(X, Y, s=200, c=color, alpha=.5)
    for each_center,color in zip(cluster_center2, color_ls):
        plt.scatter(each_center[0], each_center[1], s=200, c=color, alpha=.5, marker="*")
    plt.xlim(-3, 3)
    plt.ylim(-3, 3)
    plt.show()

def plot_distribution_3D(cluster_index, data, cluster_center3):
    cluster0 = []
    cluster1 = []
    cluster2 = []
    for i in range(len(cluster_index)):
        if cluster_index[i] == 0:
            cluster0.append(data[i])
        if cluster_index[i] == 1:
            cluster1.append(data[i])
        if cluster_index[i] == 2:
            cluster2.append(data[i])
    color_ls = ["red", "green", "blue"]
    all_clusters = [cluster0, cluster1, cluster2]
    fig = plt.figure()
    ax = Axes3D(fig)
    for each_cluster, color in zip(all_clusters, color_ls):
        for each_item in each_cluster:
            X = each_item[0]
            Y = each_item[1]
            Z = each_item[2]
            ax.scatter(X, Y, Z, s=200, c=color, alpha=.5)
    for each_center,color in zip(cluster_center3, color_ls):
        plt.scatter(each_center[0], each_center[1], s=200, c=color, alpha=.5, marker="*")
    ax.set_zlabel('Z')
    ax.set_ylabel('Y')
    ax.set_xlabel('X')
    plt.show()

def print_clusters(cluster_index):
    cluster_dict = {0: [], 1: [], 2: []}
    for i in range(len(cluster_index)):
        cluster_dict[cluster_index[i]].append(i+1)
    print("cluster result: {}".format(cluster_dict))

if __name__ == '__main__':
    data = load_data("data_depth.csv")    # data_width.csv
    cluster_index1, cluster_center1 = do_k_modes(data)
    print_clusters(cluster_index1)

    pca2 = PCA(2)
    reduce_data2 = pca2.fit_transform(data)
    cluster_index2, cluster_center2 = do_k_modes(reduce_data2)
    print_clusters(cluster_index2)
    plot_distribution_2D(cluster_index2, reduce_data2, cluster_center2)

    pca3 = PCA(3)
    reduce_data3 = pca3.fit_transform(data)
    cluster_index3, cluster_center3 = do_k_modes(reduce_data3)
    print_clusters(cluster_index3)
    plot_distribution_3D(cluster_index3, reduce_data3, cluster_center3)
