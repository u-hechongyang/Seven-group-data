import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.model_selection import learning_curve
import matplotlib.pyplot as plt

row_df = pd.read_csv('data/house_price.csv')
chaoyang = row_df[row_df.iloc[:,1] !='多']
X = chaoyang[['rooms','halls','size']]
y = chaoyang.price

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=33, test_size=0.25)
# 分析回归目标值的差异
print('max:', np.max(chaoyang.price), '\tmin:', np.min(chaoyang.price), '\taverage:', np.mean(chaoyang.price))

# 二、标准化处理
from sklearn.preprocessing import StandardScaler

ss_X = StandardScaler()
ss_y = StandardScaler()

X_train = ss_X.fit_transform(X_train)
X_test = ss_X.fit_transform(X_test)
y_train = ss_y.fit_transform(y_train.values.reshape(-1,1))
y_test = ss_y.fit_transform(y_test.values.reshape(-1,1))

#三、模型训练
# 分别导入普通随机森林回归模型、极端随机森林回归模型、梯度提升树回归模型
from sklearn.ensemble import RandomForestRegressor, ExtraTreesRegressor, GradientBoostingRegressor

rfr = RandomForestRegressor()
rfr.fit(X_train, y_train.ravel())
rfr_y_predict = rfr.predict(X_test)

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

etr = ExtraTreesRegressor()
etr.fit(X_train, y_train.ravel())
etr_y_predict = etr.predict(X_test)

gbr = GradientBoostingRegressor()
gbr.fit(X_train, y_train.ravel())
gbr_y_predict = gbr.predict(X_test)

output = pd.DataFrame(rfr_y_predict)
output.to_csv(r'D:/testdata/submission.csv',index=0)


# 对三种集成模型进行性能评价
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error

print("使用R方来评估模型，越接近于1，说明模型越准确，接近于0，说明模型不准确，接近于负数，说明数据之间没有线性关系")
print('R-squared value of RandomForestRegressor:',rfr.score(X_test,y_test))
print('R-squared value of ExtraTreesRegressor:',etr.score(X_test,y_test))
print('R-squared value of GradientBoostingRegressor:',gbr.score(X_test,y_test))

print("以下两种评估方法都与数据的单位有关系")
print("使用均方误差来评估模型")
print('The mean squared error of RandomForestRegressor:',mean_squared_error(ss_y.inverse_transform(y_test),ss_y.inverse_transform(rfr_y_predict)))
print('The mean squared error of ExtraTreesRegressor:',mean_squared_error(ss_y.inverse_transform(y_test),ss_y.inverse_transform(etr_y_predict)))
print('The mean squared error of GradientBoostingRegressor:',mean_squared_error(ss_y.inverse_transform(y_test),ss_y.inverse_transform(gbr_y_predict)))

print("使用平方绝对误差评估模型")
print('The mean absolute error of RandomForestRegressor:',mean_absolute_error(ss_y.inverse_transform(y_test),ss_y.inverse_transform(rfr_y_predict)))
print('The mean absolute error of ExtraTreesRegressor:',mean_absolute_error(ss_y.inverse_transform(y_test),ss_y.inverse_transform(etr_y_predict)))
print('The mean absolute error of GradientBoostingRegressor:',mean_absolute_error(ss_y.inverse_transform(y_test),ss_y.inverse_transform(gbr_y_predict)))


