# -*- encoding:utf-8 -*-

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn import metrics

file_name = "normalization_data.csv"    # "cardiac_delet.csv"
df_train = pd.read_csv(file_name)
df_train.columns = ["bhr", "basebp", "basedp", "pkhr", "sbp", "dp", "dose", "maxhr", "%mphr(b)", "mbp", "dpmaxdo",
                    "dobdose", "age", "gender", "baseEF", "dobEF", "chestpain", "equivecg", "restwma",
                    "posSE", "newMI", "hxofHT", "hxofdm",  "hxofMI",
                    "hxofCABG", "death"]

X = df_train.values[:, 2:-1]
Y = df_train.values[:, -1]


accuracy_ls = []
test_y_ls = []
pre_y_ls = []
test_times = 10

for i in range(100000):
    trainX, testX, trainY, testY = train_test_split(X, Y, test_size=0.3)
    test_y_ls.append(testY)
    dtree = tree.DecisionTreeClassifier(criterion="gini")
    dtree.fit(trainX, trainY)
    Y_pred = dtree.predict(testX)
    pre_y_ls.append(Y_pred)
    accuracy_ls.append(dtree.score(testX, testY))

print("mean accuracy: {0}".format(np.mean(accuracy_ls)))
print("RMSE error:{0}".format(np.sqrt(metrics.mean_squared_error(test_y_ls, pre_y_ls))))
