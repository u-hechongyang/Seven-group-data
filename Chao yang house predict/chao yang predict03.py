import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.model_selection import learning_curve
import matplotlib.pyplot as plt

chaoyang = pd.read_csv('data/house_price1.csv')
#选取的行中，第二列没有多，清洗数据
#chaoyang = row_df[row_df.iloc[:,1] !='多']
X = chaoyang[['rooms','halls','size','unit_price']]
#X = chaoyang[['rooms','halls','size']]
y = chaoyang.price

## 拆分成训练集(75%)和测试集(25%)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=33, test_size=0.25)
# 分析回归目标值的差异
print('max:', np.max(chaoyang.price), '\tmin:', np.min(chaoyang.price), '\taverage:', np.mean(chaoyang.price))

#三、模型训练
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

output = pd.DataFrame({"real Price":y_test,"predict":rfr_y_predict})
output.to_csv(r'D:/testdata/submission1.csv',index=0)

output = pd.DataFrame({"real Price":y_test,"predict":etr_y_predict})
output.to_csv(r'D:/testdata/submission2.csv',index=0)

output = pd.DataFrame({"real Price":y_test,"predict":gbr_y_predict})
output.to_csv(r'D:/testdata/submission3.csv',index=0)

# train_sizes, train_score, test_score = learning_curve(RandomForestRegressor(max_depth=16), X, y, cv=10, scoring='r2',
#     train_sizes=np.linspace(0.0, 1.0, num=30)[1:])
# train_score_mean = np.mean(train_score, axis=1)
# test_score_mean = np.mean(test_score, axis=1)
#
# plt.plot(train_sizes, train_score_mean, 'o-', color="r",
#          label="Training")
# plt.plot(train_sizes, test_score_mean, 'o-', color="g",
#         label="Validation")
#
# plt.xlabel("Training examples")
# plt.ylabel("Score")
# plt.legend(loc="best")
# plt.show()