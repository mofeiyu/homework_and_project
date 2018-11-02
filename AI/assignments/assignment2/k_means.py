# -*- encoding:utf-8 -*-

# Name: SUN RUI    ID:18083229g

import pandas as pd
from sklearn import preprocessing
from sklearn.cluster import KMeans


def load_data(file_path):
    df_data = pd.read_csv(file_path)
    df_data.columns = ["Age", "Sex", "MonthlyIncome", "MaritalStatus",	"ServicePlan", "ExtraUsage"]
    # print(df_data)
    scaled_data = preprocessing.scale(df_data)
    return scaled_data


def do_k_means(data):
    k_means = KMeans(n_clusters=3, random_state=0)
    print(k_means.fit_predict(data))
    print(k_means.fit(data).cluster_centers_)


data = load_data("data.csv")
do_k_means(data)


