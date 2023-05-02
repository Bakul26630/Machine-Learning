# Based on multiple features/variables perform Linear Regression. For example, based on a
# number of additional features like number of bedrooms, servant room, number of balconies,
# number of houses of years a house has been built – predict the price of a house.

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

data = pd.read_csv('./train.csv',usecols=['SalePrice','YearRemodAdd','BedroomAbvGr','KitchenAbvGr','LotArea',])
X=data.values[:,0:4]
Y=data.values[:,4]
model = LinearRegression()
model.fit(X,Y)

testData = pd.read_csv('./test.csv',usecols=['YearRemodAdd','BedroomAbvGr','KitchenAbvGr','LotArea',])
X_test = testData.values[:,0:]
Y_test = model.predict(X_test)
for i in range(len(Y_test)):
    if i==len(Y_test)-1:
        print("{:.2f}".format(Y_test[i]),end=".")
    print("{:.2f}".format(Y_test[i]),end=",")