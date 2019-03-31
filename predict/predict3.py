import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

train_df = pd.read_csv('data/houseprice.csv')
X = train_df[['longitude','latitude','year','month']]
y = train_df.unitPrice

from sklearn.model_selection import train_test_split, KFold

# X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=33, test_size=0.25)
#
from sklearn.ensemble import RandomForestRegressor
# rfr = RandomForestRegressor()
# rfr.fit(X_train,y_train)
# print("拟合率：",rfr.score(X_train,y_train))
# print("预测率：",rfr.score(X_test,y_test))

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score

# randomForest_model = RandomForestRegressor()
# kf = KFold(n_splits=5, shuffle=True)
# score_ndarray = cross_val_score(randomForest_model, X, y, cv=kf)
# print(score_ndarray)
# print(score_ndarray.mean())

import numpy as np
from sklearn.linear_model import LogisticRegression,LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import AdaBoostRegressor
def classifier():
    scores=[]
    models=[LinearRegression(),LogisticRegression()]
    for model in models:
        score=cross_val_score(model,X,y,cv=10)
        mean_score=np.mean(score)
        scores.append(mean_score)
    return scores
a=classifier()
print('aaa',a)
import  matplotlib.pyplot as plt
plt.plot([i for i in range(len(a))],a)