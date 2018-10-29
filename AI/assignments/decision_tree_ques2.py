# -*- encoding:utf-8 -*-
# Name: SUN RUI    ID: 18083229g

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn import metrics

file_name = "nor_data1.csv"    # "normalization_data_static.csv"
df_train = pd.read_csv(file_name)
df_train.columns = ["bhr", "basebp", "basedp", "pkhr", "sbp", "dp", "dose", "maxhr", "%mphr(b)", "mbp", "dpmaxdo",
                    "dobdose", "age", "gender", "baseEF", "dobEF", "chestpain", "posECG", "equivecg", "restwma",
                    "posSE", "newMI", "newPTCA", "newCABG", "hxofHT", "hxofdm", "hxofcig", "hxofMI",
                    "hxofPTCA", "hxofCABG", "death"]
X = df_train.values[:, 0:-1]
Y = df_train.values[:, -1]

accuracy_ls = []
test_y_ls = []
pre_y_ls = []

times = 100000
for i in range(times):
    print("finish {0}%\r".format(int(i / times * 100)), end='')
    trainX, testX, trainY, testY = train_test_split(X, Y, test_size=0.3)
    test_y_ls.append(testY)
    dtree = tree.DecisionTreeClassifier(criterion="entropy")
    dtree.fit(trainX, trainY)
    Y_pred = dtree.predict(testX)
    pre_y_ls.append(Y_pred)
    accuracy_ls.append(dtree.score(testX, testY))

print("mean accuracy: {0}".format(np.mean(accuracy_ls)))
print("RMSE error:{0}".format(np.sqrt(metrics.mean_squared_error(test_y_ls, pre_y_ls))))

