# Implement Linear Regression problem. For example, based on a dataset comprising of 
# existing set of prices and area/size of the houses, predict the estimated price of a given house.

# Using Least Square Method to implement Linear Regression
import pandas as pd
import numpy as np
import math

data = pd.read_csv('./train.csv')
N=len(data.values[:,0])
X=np.array(data.values[:,4])
Y=np.array(data.values[:,80])

XY = X*Y
X2 = X*X

sumXY = XY.sum()
sumX2 = X2.sum()
sumX = X.sum()
sumY = Y.sum()
beta0 = (N*sumXY-sumX*sumY)/(N*sumX2-sumX*sumX)
beta1 = (Y.sum()-beta0*X.sum())/N

testData = pd.read_csv('./test.csv')
X_test = testData.values[:,4]
Y_test = [math.trunc(beta0*i+beta1) for i in X_test]
print(Y_test)

