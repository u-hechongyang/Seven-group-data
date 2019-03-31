import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

#一、导入数据
row_df = pd.read_csv('data/house_price.csv')
chaoyang = row_df[row_df.iloc[:,1] !='多']
X1 = chaoyang[['rooms','halls','size','unit_price']]
X = chaoyang[['rooms','halls','size']]
y = chaoyang.price

## 拆分成训练集(75%)和测试集(25%)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=33, test_size=0.25)
# 分析回归目标值的差异
print('max:', np.max(chaoyang.price), '\tmin:', np.min(chaoyang.price), '\taverage:', np.mean(chaoyang.price))

#二、模型训练
# 梯度提升回归（Gradient boosting regression，GBR）
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

#三、对模型进行评估
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

#四、存储预测的值
output = pd.DataFrame({"real Price":y_test,"predict":rfr_y_predict})
output.to_csv(r'D:/testdata/submission1.csv',index=0)

output = pd.DataFrame({"real Price":y_test,"predict":etr_y_predict})
output.to_csv(r'D:/testdata/submission2.csv',index=0)

output = pd.DataFrame({"real Price":y_test,"predict":gbr_y_predict})
output.to_csv(r'D:/testdata/submission3.csv',index=0)




