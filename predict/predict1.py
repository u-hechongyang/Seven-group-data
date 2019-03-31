import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

#一、清洗数据
train_df = pd.read_csv('data/nj_transform1.csv')
train_df = train_df[train_df.iloc[:,7] !='暂无数据']
train_df = train_df[train_df.iloc[:,12] !='暂无数据']
train_df = train_df[train_df.iloc[:,10] !='其他']
train_df = train_df[train_df.iloc[:,7] !='错层']
train_df = train_df[train_df['elevaPropora']<=20]
train_df[['floors', 'houseStruct','decoration','isElevator']] = train_df[['floors', 'houseStruct','decoration','isElevator']].convert_objects(convert_numeric=True)
#print(train_df)

#二、特征选取
#经过特征相关度，选取最相关的两个数据维度
X = train_df[['longitude','latitude']]
y = train_df.unitPrice

#三、划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=33, test_size=0.25)

#四、模型训练
# 分别导入普通随机森林回归模型、极端随机森林回归模型、梯度提升树回归模型
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

#五、对三种集成模型进行性能评价
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error
#print("使用R方来评估模型，越接近于1，说明模型越准确，接近于0，说明模型不准确，接近于负数，说明数据之间没有线性关系")
print("使用R方来评估模型")
print('R-squared value of RandomForestRegressor:',rfr.score(X_test,y_test))
print('R-squared value of ExtraTreesRegressor:',etr.score(X_test,y_test))
print('R-squared value of GradientBoostingRegressor:',gbr.score(X_test,y_test))
print("使用绝对平方误差来评估模型")
print('The mean absolute error of RandomForestRegressor:',mean_absolute_error(rfr_y_predict,y_test))
print('The mean absolute error of ExtraTreesRegressor:',mean_absolute_error(etr_y_predict,y_test))
print('The mean absolute error of GradientBoostingRegressor:',mean_absolute_error(gbr_y_predict,y_test))

output = pd.DataFrame({"real Price":y_test,"predict":rfr_y_predict})
output.to_csv(r'D:/testdata/submission1.csv',index=0)

output = pd.DataFrame({"real Price":y_test,"predict":etr_y_predict})
output.to_csv(r'D:/testdata/submission2.csv',index=0)

output = pd.DataFrame({"real Price":y_test,"predict":gbr_y_predict})
output.to_csv(r'D:/testdata/submission3.csv',index=0)