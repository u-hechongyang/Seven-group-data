import pandas as pd
train_df = pd.read_csv('data/houseprice.csv')

X = train_df[['longitude','latitude','year','month']]
y = train_df.unitPrice

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=10, test_size=0.25)
from sklearn.ensemble import RandomForestRegressor

rfr = RandomForestRegressor()
rfr.fit(X_train, y_train.ravel())
rfr_y_predict = rfr.predict(X_test)
#print('R-squared value of RandomForestRegressor:',rfr.score(X_test,y_test))
#output = pd.DataFrame({"real Price":y_test,"predict":rfr_y_predict})
#output.to_csv(r'D:/testdata/submission.csv',index=0)

predict_df = pd.read_csv('data/predict1.csv')
title = predict_df.areaName
longitude = predict_df.longitude
latitude = predict_df.latitude
year = predict_df.year
month = predict_df.month
predict_x = predict_df[['longitude','latitude','year','month']]
predict_y = rfr.predict(predict_x)
output = pd.DataFrame({"areaName":title,",year":year,",month":month,",predict":predict_y})
output.to_csv(r'D:/testdata/predict_test.csv',index=0)