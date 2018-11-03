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
    k_modes = KModes(n_clusters=3, init=centroids, n_init=1)
    return k_modes.fit_predict(data), data

def plot_distribution_2D(cluster_index, data):
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
    plt.xlim(-3, 3)
    plt.ylim(-3, 3)
    plt.show()

def plot_distribution_3D(cluster_index, data):
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
    ax.set_zlabel('Z')
    ax.set_ylabel('Y')
    ax.set_xlabel('X')
    plt.show()

data = load_data("data_depth.csv")
pca2 = PCA(2)
reduce_data2 = pca2.fit_transform(data)
print(reduce_data2)
cluster_index2, cluster_center2 = do_k_modes(reduce_data2)
print(cluster_index2)
plot_distribution_2D(cluster_index2, reduce_data2)

pca3 = PCA(3)
reduce_data3 = pca3.fit_transform(data)
cluster_index3, cluster_center3 = do_k_modes(reduce_data3)
plot_distribution_3D(cluster_index3, reduce_data3)
