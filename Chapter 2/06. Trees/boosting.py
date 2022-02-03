import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import OrdinalEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRFRegressor
from sklearn.ensemble import AdaBoostRegressor


df = pd.read_csv(r'C:\Users\DELL\Downloads\ai_nov21-main\ai_nov21\Chapter 2\06. Trees\insurance.csv')

#print(df.head())


enc = OrdinalEncoder()
df[[ 'sex','smoker', 'region']] = enc.fit_transform(df[[ 'sex','smoker', 'region']])
#df[[ 'sex','smoker', 'region']] = enc.transform(df[[ 'sex','smoker', 'region']])

X,y = df.iloc[:, :-1], df.iloc[:, -1]

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0, test_size=0.3)



dt_clf = DecisionTreeRegressor()
dt_clf = dt_clf.fit(X_train, y_train)

y_pred = dt_clf.predict(X_test)
#print(y_pred)

score = dt_clf.score(X_train,y_train)
print('dt_train = ',score)
score = dt_clf.score(X_test,y_test)
print('dt_test = ',score)



dt_clf1 = RandomForestRegressor()
dt_clf1 = dt_clf1.fit(X_train, y_train)

y_pred = dt_clf1.predict(X_test)

score = dt_clf1.score(X_train,y_train)
print('rfr_train = ',score)
score = dt_clf1.score(X_test,y_test)
print('rfr_test = ',score)


dt_clf3 = GradientBoostingRegressor()
dt_clf3 = dt_clf3.fit(X_train, y_train)

y_pred = dt_clf3.predict(X_test)


score = dt_clf3.score(X_train,y_train)
print('gb_train = ',score)
score = dt_clf3.score(X_test,y_test)
print('gb_test = ',score)

dt_clf4 = XGBRFRegressor()
dt_clf4 = dt_clf4.fit(X_train, y_train)

y_pred = dt_clf4.predict(X_test)


score = dt_clf4.score(X_train,y_train)
print('xgb_train = ',score)
score = dt_clf4.score(X_test,y_test)
print('xgb_test = ',score)


dt_clf5 = AdaBoostRegressor()
dt_clf5 = dt_clf5.fit(X_train, y_train)

y_pred = dt_clf5.predict(X_test)
#print(y_pred)

score = dt_clf5.score(X_train,y_train)
print('ada_train = ',score)
score = dt_clf5.score(X_test,y_test)
print('ada_test = ',score)