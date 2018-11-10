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
    return df_data

def do_k_modes(df_data):
    one_hot_data = np.array(pd.get_dummies(df_data))
    centroids = np.vstack((one_hot_data[0], one_hot_data[7], one_hot_data[14]))
    k_modes = KModes(n_clusters=3, init=centroids, n_init=1)
    return k_modes.fit_predict(one_hot_data), one_hot_data

# def plot_distribution_2D(cluster_index, data):
#     cluster0 = []
#     cluster1 = []
#     cluster2 = []
#     for i in range(len(cluster_index)):
#         if cluster_index[i] == 0:
#             cluster0.append(data[i])
#         if cluster_index[i] == 1:
#             cluster1.append(data[i])
#         if cluster_index[i] == 2:
#             cluster2.append(data[i])
#     pca = PCA(2)
#     color_ls = ["red", "green", "blue"]
#     all_clusters = [cluster0, cluster1, cluster2]
#     for i in range(len(all_clusters)):
#         plot_columns = pca.fit_transform(all_clusters[i])
#         X = plot_columns[:, 0]
#         Y = plot_columns[:, 1]
#         plt.scatter(X, Y, s=200, c=color_ls[i], alpha=.5)
#     plt.xlim(-3, 3)
#     plt.ylim(-3, 3)
#     plt.show()
#
# def plot_distribution_3D(cluster_index, data):
#     cluster0 = []
#     cluster1 = []
#     cluster2 = []
#     for i in range(len(cluster_index)):
#         if cluster_index[i] == 0:
#             cluster0.append(data[i])
#         if cluster_index[i] == 1:
#             cluster1.append(data[i])
#         if cluster_index[i] == 2:
#             cluster2.append(data[i])
#     pca = PCA(3)
#     color_ls = ["red", "green", "blue"]
#     all_clusters = [cluster0, cluster1, cluster2]
#     fig = plt.figure()
#     ax = Axes3D(fig)
#     for i in range(len(all_clusters)):
#         plot_columns = pca.fit_transform(all_clusters[i])
#         X = plot_columns[:, 0]
#         Y = plot_columns[:, 1]
#         Z = plot_columns[:, 2]
#         ax.scatter(X, Y, Z, s=200, c=color_ls[i], alpha=.5)
#
#     plt.show()


df_data = load_data("data_width.csv")
cluster_index, one_hot_data = do_k_modes(df_data)
# plot_distribution_2D(cluster_index, one_hot_data)
# plot_distribution_3D(cluster_index, one_hot_data)
print(cluster_index)
