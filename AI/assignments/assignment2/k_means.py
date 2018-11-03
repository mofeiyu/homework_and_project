# -*- encoding:utf-8 -*-

# Name: SUN RUI    ID:18083229g

import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from mpl_toolkits.mplot3d import Axes3D


def load_data(file_path):
    df_data = pd.read_csv(file_path)
    df_data.columns = ["Age", "Sex", "MonthlyIncome", "MaritalStatus",	"ServicePlan", "ExtraUsage"]
    # print(df_data)
    scaled_data = preprocessing.scale(df_data)
    return scaled_data


def do_k_means(data):
    centers = np.vstack((data[0], data[7], data[14]))
    k_means = KMeans(n_clusters=3, init=centers, n_init=1, max_iter=1000)
    return k_means.fit_predict(data), k_means.fit(data).cluster_centers_

def plot_distribution_2D(index, data):
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
    pca = PCA(2)
    color_ls = ["red", "green", "blue"]
    all_clusters = [cluster0, cluster1, cluster2]
    for i in range(len(all_clusters)):
        plot_columns = pca.fit_transform(all_clusters[i])
        X = plot_columns[:, 0]
        Y = plot_columns[:, 1]
        plt.scatter(X, Y, s=200, c=color_ls[i], alpha=.5)
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
    pca = PCA(3)
    color_ls = ["red", "green", "blue"]
    all_clusters = [cluster0, cluster1, cluster2]
    fig = plt.figure()
    ax = Axes3D(fig)
    for i in range(len(all_clusters)):
        plot_columns = pca.fit_transform(all_clusters[i])
        X = plot_columns[:, 0]
        Y = plot_columns[:, 1]
        Z = plot_columns[:, 2]
        ax.scatter(X, Y, Z, s=200, c=color_ls[i], alpha=.5)
    ax.set_zlabel('Z')
    ax.set_ylabel('Y')
    ax.set_xlabel('X')
    plt.show()

data = load_data("data.csv")
cluster_index, cluster_center = do_k_means(data)
plot_distribution_2D(cluster_index, data)
plot_distribution_3D(cluster_index, data)
print(cluster_index)
# print(cluster_center)


#
# cluster0 = []
# cluster1 = []
# cluster2 = []
# for i in range(len(cluster_index)):
#     if cluster_index[i] == 0:
#         cluster0.append(data[i])
#     if cluster_index[i] == 1:
#         cluster1.append(data[i])
#     if cluster_index[i] == 2:
#         cluster2.append(data[i])
# pca = PCA(3)
# plot_columns = pca.fit_transform(cluster0)
# fig = plt.figure()
# ax = Axes3D(fig)
# X = plot_columns[:, 0]
# Y = plot_columns[:, 1]
# Z = plot_columns[:, 2]
# ax.scatter(X, Y, Z, s=100)
#
# plt.show()