#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 20:07:51 2018

@author: amd6ua
"""

# Reading in the libraries
import os
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import numpy as np
#import numpy as np

#Reading in the train and test datasets 
train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")

# Converting test and test into a single file 'combined file.csv'
file= pd.concat([train,test], axis = 0)



#### Categorical Column
   
#Selecting certain top Categorical columns and replacing the missing values with their corresponding model values
file.MasVnrType[file.MasVnrType.isna()] = "None"
file.Electrical[file.Electrical.isna()] = "SBrkr"

#file.GarageType[file.GarageType.isna()] = "Attchd"
#file.GarageFinish[file.GarageFinish.isna()] = "Unf"
#file.GarageQual[file.GarageQual.isna()] = "TA"
#file.BsmtFinType1[file.BsmtFinType1.isna()] = "Unf"
#file.GarageCond[file.GarageCond.isna()] = "TA"

#Get train variables
x_train=x_dummy.iloc[:1460,1:].values
x_train



######################## Preparing the data for modeling #############################

#Getting the SalePrice (reponse variable) values
y_train=file['SalePrice'][:1460].values
y_train


#reorder the columns according to their importance
x_dummy_reind = x_dummy.reindex(newColumnOrder, axis=1)
x_dummy_reind=x_dummy_reind.values
imputer.fit(x_dummy_reind[:,:])
x_dummy_reind[:,:]=imputer.transform(x_dummy_reind[:,:])
#scale features
from sklearn.preprocessing import scale
x_dummy_reind=scale(x_dummy_reind)
x_dummy_reind
x_train_reind=x_dummy_reind[:1460]
len(x_train_reind[0])

#get variable variables
x_pred=x_dummy_reind[1460:,1:10]
x_train_reind=x_train_reind[:,1:10]
len(x_train_reind)
len(x_pred)

x_pred


############################ PARAMETRIC APPROACH #####################################

### Linear Regression
## Since the response varaible is continuous and we might need to see the significance for each features
## we move ahead with performing linear regression
#Linear regression is the best to get significance of features and it is easy to explain

from sklearn.linear_model import LinearRegression,Lasso
Linear_result = run_cv(x_train_reind, y_train, LinearRegression)
mean_squared_error(y_train, Linear_result)


from sklearn.linear_model import LinearRegression
regr = LinearRegression()
# Train the model using the training sets
regr.fit(x_train_reind, y_train)
linear_pred=regr.predict(x_pred)
prediction_linear=pd.DataFrame({'Id':range(1461,2920),'SalePrice':linear_pred})
prediction_linear.to_csv('prediction_linear.csv', index = False)