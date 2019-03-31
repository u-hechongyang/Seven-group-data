import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression,Ridge,Lasso

n_sample=50
n_feature=200
x_train=np.random.randn(n_sample,n_feature)
print(x_train)
#创建y_train目标
#200  coef
coef=np.random.randn(n_feature)
print(coef)
# # y_train=np.dot(x_train,coef)
# inds=np.arange(0,200)
# #随机打乱顺序
# np.random.shuffle(inds)
#
# coef[inds[:190]]=0
# y_train=np.dot(x_train,coef)

# #分别使用线性回归，岭回归，Lasso回归进行数据预测
# lrg=LinearRegression()
# ridge=Ridge()
# lasso=Lasso()
# lrg.fit(x_train,y_train)
# ridge.fit(x_train,y_train)
# lasso.fit(x_train,y_train)
#
# #数据视图，此处获取各个算法的训练数据的coef_:系数，coef_可以理解为系数
#
# plt.figure(figsize=(12,9))
# axes=plt.subplot(221)
# axes.plot(coef)
# axes.set_title('True_coef')
#
# #线性回归 得到的coef
# axes=plt.subplot(222)
# axes.plot(lrg.coef_)
# axes.set_title('lrg_coef')
#
# #l岭回归 得到的coef
# axes=plt.subplot(223)
# axes.plot(ridge.coef_)
# axes.set_title('ridge_coef')
#
# #lasso回归 得到的coef
# axes=plt.subplot(224)
# axes.plot(lasso.coef_)
# axes.set_title('lasso_coef')