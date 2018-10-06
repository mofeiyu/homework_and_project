# -*- encoding:utf-8 -*-

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import tree

df_train = pd.read_csv("training_data_set.csv")
df_train.columns = ["Tear Production Rate", "Sex", "Age", "Spectacle Prescription", "Astigmatism", "Recommendation"]
train_X = df_train.values[:, 0:5]
train_Y = df_train.values[:, 5]

df_test = pd.read_csv("test_data_set.csv")
df_test.columns = ["Tear Production Rate", "Sex", "Age", "Spectacle Prescription", "Astigmatism", "Recommendation"]
test_X = df_test.values[:, 0:5]
test_Y = df_test.values[:, 5]

dtree = tree.DecisionTreeClassifier(criterion="gini")
dtree.fit(train_X, train_Y)

Y_pred = dtree.predict(test_X)
print(Y_pred)
print("Accuracy: \n", dtree.score(test_X, test_Y))
