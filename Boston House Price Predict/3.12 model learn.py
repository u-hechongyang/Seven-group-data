import numpy as np
import pandas as pd
df_train=pd.read_csv('kaggle_data/train.csv')
df_train.head()#结果在这里不展示

df_train.columns#展示各列的名字

df_train['SalePrice'].describe()#研究房价（target），即结果一列，会显示该列的均值 方差 标准差 四分位数 最值等信息
