import data_anlaysis as da
#from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
#from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score,confusion_matrix


def train_model():

    x_train, x_test, y_train, y_test, ct, scaler = da.get_data(r'C:\Users\DELL\Desktop\treeboosting\insurance (1).csv')

    clf_1 = RandomForestClassifier()
    clf_2 = DecisionTreeClassifier()
    #clf_3 = GradientBoostingClassifier()
    #clf_4 = XGBClassifier()
    
    clf_1.fit(x_train,y_train)
    clf_2.fit(x_train,y_train)
    #clf_3.fit(x_train,y_train)
    #clf_4.fit(x_train,y_train)

    y_pred1 = clf_1.predict(x_test)
    y_pred2 = clf_2.predict(x_test)
    #y_pred3 = clf_3.predict(x_test)
    #y_pred4 = clf_4.predict(x_test)


    score1 = accuracy_score(y_test,y_pred1)
    score2 = accuracy_score(y_test,y_pred2)
    #score3 = accuracy_score(y_test,y_pred3)
    #score4 = accuracy_score(y_test,y_pred4)

    


    return clf_1, clf_2, ct ,scaler

