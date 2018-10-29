# -*- encoding:utf-8 -*-
# Name: SUN RUI    ID: 18083229g

import pandas as pd
from sklearn import tree
from sklearn.externals.six import StringIO
from IPython.display import Image
from sklearn.tree import export_graphviz
import pydotplus


df_train = pd.read_csv("training_data_set.csv")
df_train.columns = ["Tear Production Rate", "Sex", "Age", "Spectacle Prescription", "Astigmatism", "Recommendation"]
train_X = df_train.values[:, 0:5]
train_Y = df_train.values[:, 5]

df_test = pd.read_csv("test_data_set.csv")
df_test.columns = ["Tear Production Rate", "Sex", "Age", "Spectacle Prescription", "Astigmatism", "Recommendation"]
test_X = df_test.values[:, 0:5]
test_Y = df_test.values[:, 5]

dtree = tree.DecisionTreeClassifier(criterion="entropy")
dtree.fit(train_X, train_Y)

Y_pred = dtree.predict(test_X)
print("testing Y data: {0}".format(test_Y))
print("prediction Y data: {0}".format(Y_pred))
print("accuracy rate: {0}%".format(dtree.score(test_X, test_Y)*100))

dot_data = StringIO()
export_graphviz(dtree, out_file=dot_data, filled=True, rounded=True, special_characters=True)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_pdf("decision_tree.pdf")
