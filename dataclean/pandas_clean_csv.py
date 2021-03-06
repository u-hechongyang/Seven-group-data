import numpy as np
import pandas as pd

train_df = pd.read_csv('data/nj_transform1.csv')
#print(train_df.head(5))
#数据清洗
#去除数据中暂无数据的列,去除电梯比例大于20的数据
train_df = train_df[train_df.iloc[:,7] !='暂无数据']
train_df = train_df[train_df.iloc[:,12] !='暂无数据']
train_df = train_df[train_df.iloc[:,10] !='其他']
train_df = train_df[train_df.iloc[:,7] !='错层']
train_df[train_df['elevaPropora']<=20]
#print(train_df)
#查看各列的信息
#train_df.info()
#查看floors这一列的数据统计信息
#print(train_df.houseStruct.value_counts())
#print(train_df.describe())

from matplotlib import pyplot as plt
plt.style.use('ggplot')
train_df.hist(bins=50,figsize=(16,9))