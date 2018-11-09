#encoding=utf-8

from __future__ import division
from __future__ import print_function
import numpy as np
import pandas as pd
from data import DataFactory
from sklearn import metrics
from sklearn import linear_model, svm
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import AdaBoostRegressor
from sklearn.ensemble import ExtraTreesRegressor

class Model:
    def __init__(self):
        self.dataset = DataFactory()
        self.clfs = {        
            'svm':svm.SVR(), 
            'RandomForestRegressor': RandomForestRegressor(n_estimators=100),
            'BayesianRidge':linear_model.BayesianRidge(),
            'GradientBoostingRegressor':GradientBoostingRegressor(),
            'AdaBoostRegressor':AdaBoostRegressor(),
            'ExtraTreesRegressor':ExtraTreesRegressor()          
        }
        self.train_X, self.train_Y = self.dataset.get_train_data()
        self.dev_X, self.dev_Y = self.dataset.get_dev_data()
        self.test_ID, self.test_X, self.test_Y = self.dataset.get_test_data()
    
    def models(self):
        clfs = self.clfs
        for clf in clfs:
            try:
                self.train(clf)
                self.dev(clf)
                y_pred = self.evaluate(clf)
                self.save_submission(clf, y_pred)
            except Exception as e:
                print(clf + " Error:")
                print(str(e))
                        
    def train(self, clf):
        print ("_____________________________________________")
        self.clfs[clf].fit(self.train_X, self.train_Y)
        y_pred = self.clfs[clf].predict(self.train_X)
        score = np.sqrt(metrics.mean_squared_error(np.log(y_pred),np.log(self.train_Y)))
        print ('%s train score=%.2f' % (clf, score))

    def dev(self, clf):
        y_pred = self.clfs[clf].predict(self.dev_X)
        score = np.sqrt(metrics.mean_squared_error(np.log(y_pred),np.log(self.dev_Y)))
        print ('%s dev score=%.2f' % (clf, score))
        
    def evaluate(self, clf):
        y_pred = self.clfs[clf].predict(self.test_X)
        score = np.sqrt(metrics.mean_squared_error(np.log(y_pred),np.log(self.test_Y)))
        print ('%s test score=%.2f' % (clf, score))
        return y_pred

    def save_submission(self, pre_name, y_pred):
        submission = pd.DataFrame({"Id": self.test_ID,
                                   "SalePrice": y_pred})
        name = 'data/submission/' + pre_name + '.csv'
        submission.to_csv(name, index = False)
        print(name, ": save")
        
    def grid_para(self):
        return
            
def main():
    model = Model()
    model.models()

if __name__ == '__main__':
    main()