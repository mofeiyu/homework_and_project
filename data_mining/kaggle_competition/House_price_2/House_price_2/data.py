#encoding=utf-8

from __future__ import division
from __future__ import print_function

import sys
import datetime
import numpy as np
import pandas as pd

from sklearn import preprocessing
from sklearn.model_selection import train_test_split

class DataFactory:
    def __init__(self):
        self.split_size = 0.25
        self.data_preparation()
             
    def data_preparation(self):
        self.train_data_df = pd.read_csv('data/train.csv')
        self.test_data_df= pd.read_csv('data/test.csv')
        self.test_Id_and_Y = pd.read_csv('data/sample_submission.csv')
        self.test_Y = self.test_Id_and_Y['SalePrice']
        self.test_Id = self.test_Id_and_Y['Id']
        self.drop_data()
        self.train_len = len(self.train_data_df)
        self.train_dev_Y = self.train_data_df['SalePrice']
        self.data = pd.concat([self.train_data_df.loc[:,'MSSubClass':'SaleCondition'], self.test_data_df.loc[:,'MSSubClass':'SaleCondition']])
        self.fill_na()
        self.feature_continu, self.feature_discrete = self.get_continu_discrete()
        self.create_new_feature()
        self.drop_feature()
        self.data_Normalization()
        self.data_one_hot()
        self.train_dev_X,self.test_X = self.split_train_dev_test_X()
        self.train_X, self.dev_X, self.train_Y, self.dev_Y = self.split_train_dev()
              
    def get_train_data(self):        
        return self.train_X, self.train_Y
    
    def get_dev_data(self):
        return self.dev_X, self.dev_Y
    
    def get_test_data(self):
        return self.test_Id, self.test_X, self.test_Y 

    def drop_data(self):
        ids = []
        ids.append(1299)
        ids.append(524)
        ids.append(314)
        ids.append(335)
        ids.append(250)
        ids.append(935)
        np.unique(ids)
        for id in np.unique(ids):
            self.train_data_df = self.train_data_df.drop(self.train_data_df[self.train_data_df['Id'] == id].index)
    def fill_na(self):
        data = self.data
        data['LotFrontage'].fillna(value = -10,inplace = True)
        data['Alley'].fillna(value = 'NA',inplace = True)
        data['Exterior1st'].fillna(value = 'VinylSd',inplace = True)
        data['Exterior2nd'].fillna(value = 'VinylSd',inplace = True)
        data['MasVnrType'].fillna(value = 'NA',inplace = True)
        data['MasVnrArea'].fillna(value = 0,inplace = True)
        data['BsmtQual'].fillna(value = 'NA',inplace = True)
        data['BsmtCond'].fillna(value = 'NA',inplace = True)
        data['BsmtExposure'].fillna(value = 'NA',inplace = True)
        data['BsmtFinType1'].fillna(value = 'NA',inplace = True)
        data['BsmtFinSF1'].fillna(value = 0,inplace = True)
        data['BsmtFinType2'].fillna(value = 'NA',inplace = True)
        data['BsmtFinSF2'].fillna(value = 0,inplace = True)
        data['BsmtUnfSF'].fillna(value = 'NA',inplace = True)
        data['TotalBsmtSF'].fillna(value = 0,inplace = True)
        data['Electrical'].fillna(value = 'NA',inplace = True)
        data['BsmtFullBath'].fillna(value = 0,inplace = True)
        data['BsmtHalfBath'].fillna(value = 0,inplace = True)
        data['KitchenQual'].fillna(value = 'TA',inplace = True)
        data['Functional'].fillna(value = 'Typ',inplace = True)
        data['FireplaceQu'].fillna(value = 'NA',inplace = True)
        data['GarageType'].fillna(value = 'NA',inplace = True)
        data['GarageYrBlt'].fillna(value = 3000,inplace = True)
        data['GarageFinish'].fillna(value = 'NA',inplace = True)
        data['GarageCars'].fillna(value = 2,inplace = True)
        data['GarageArea'].fillna(value = 519,inplace = True)
        data['GarageQual'].fillna(value = 'NA',inplace = True)
        data['GarageCond'].fillna(value = 'NA',inplace = True)
        data['PoolQC'].fillna(value = 'NA',inplace = True)
        data['Fence'].fillna(value = 'NA',inplace = True)
        data['MiscFeature'].fillna(value = 'NA',inplace = True)
        data['SaleType'].fillna(value = 'WD',inplace = True)

    def get_continu_discrete(self):
        data = self.data
        feats_numeric  = data.dtypes[data.dtypes != "object"].index.values
        feats_object = data.dtypes[self.data.dtypes == "object"].index.values    
        feats_numeric_discrete  = ['MSSubClass','OverallQual','OverallCond']
        feats_numeric_discrete += ['TotRmsAbvGrd','KitchenAbvGr','BedroomAbvGr','GarageCars','Fireplaces']
        feats_numeric_discrete += ['FullBath','HalfBath','BsmtHalfBath','BsmtFullBath']
        feats_numeric_discrete += ['MoSold','YrSold']    
        feature_continu = feats_numeric.copy()
        feature_discrete = feats_object.copy()
        return feature_continu, feature_discrete
          
    def create_new_feature(self):
        data = self.data
        
    def drop_feature(self):
        data = self.data
    
    def data_Normalization(self):
        data = self.data
        feature_continu = self.feature_continu
        min_max_scaler = preprocessing.MaxAbsScaler()
        data[feature_continu] = min_max_scaler.fit_transform(data[feature_continu])
        
    def data_one_hot(self):
        data = self.data
        self.data = pd.get_dummies(data)
        
    def split_train_dev_test_X(self):
        data = self.data
        train_dev_X = data[:self.train_len]
        test_X = data[self.train_len:]
        return train_dev_X, test_X
    
    def split_train_dev(self):
        data_X = self.train_dev_X
        data_Y = self.train_dev_Y
        return train_test_split(data_X, data_Y, test_size=self.split_size)

def main():
    data_factory = DataFactory()
    x, y = data_factory.get_train_data()
    
    print (x.info())
    print (x.shape,y.shape)
    
if __name__ == '__main__':
    main()        