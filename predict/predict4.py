#一、读取数据
import pandas as pd
train_df = pd.read_csv('data/houseprice.csv')

#二、特征选取
#经过特征相关度，选取最相关的两个数据维度
X = train_df[['longitude','latitude','year','month']]
y = train_df.unitPrice

#三、划分训练集和测试集
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=33, test_size=0.25)
# 四、标准化处理

# 五、模型训练
# 分别导入普通随机森林回归模型、极端随机森林回归模型、梯度提升树回归模型
from sklearn.linear_model import LinearRegression,SGDRegressor

lr = LinearRegression()
lr.fit(X_train, y_train.ravel())
lr_y_predict = lr.predict(X_test)

sgdr = SGDRegressor()
sgdr.fit(X_train, y_train.ravel())
sgdr_y_predict = sgdr.predict(X_test)

from sklearn.tree import DecisionTreeRegressor
dtr = DecisionTreeRegressor()
dtr.fit(X_train, y_train.ravel())
dtr_y_predict = dtr.predict(X_test)

from sklearn.ensemble import RandomForestRegressor, ExtraTreesRegressor, GradientBoostingRegressor

rfr = RandomForestRegressor()
rfr.fit(X_train, y_train.ravel())
rfr_y_predict = rfr.predict(X_test)

etr = ExtraTreesRegressor()
etr.fit(X_train, y_train.ravel())
etr_y_predict = etr.predict(X_test)

gbr = GradientBoostingRegressor()
gbr.fit(X_train, y_train.ravel())
gbr_y_predict = gbr.predict(X_test)

#六、对三种集成模型进行性能评价
# 对三种集成模型进行性能评价
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error
print("使用R方来评估模型")
lrr = lr.score(X_test,y_test)
print('R-squared value of LinearRegression:',lrr)
sgdrr = sgdr.score(X_test,y_test)
print('R-squared value of SGDRegressor:',sgdrr)
dtrr = dtr.score(X_test,y_test)
print('R-squared value of DecisionTreeRegressor:',dtrr)
rfrr = rfr.score(X_test,y_test)
print('R-squared value of RandomForestRegressor:',rfrr)
etrr = etr.score(X_test,y_test)
print('R-squared value of ExtraTreesRegressor:',etrr)
gbrr = gbr.score(X_test,y_test)
print('R-squared value of GradientBoostingRegressor:',gbrr)

import matplotlib.pyplot as plt
Yy = [lrr, dtrr, rfrr, etrr, gbrr]
Xx= ['LinearRegression','DecisionTreeRegressor','RandomForestRegressor','ExtraTreesRegressor','GradientBoostingRegressor']
fig = plt.figure(figsize=(10.0, 6.0))
plt.plot(Xx,Yy)
plt.ylim((-1, 1))
plt.xticks(Xx, rotation=45)
plt.show()