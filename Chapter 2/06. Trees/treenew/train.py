from sklearn.ensemble import GradientBoostingRegressor
from xgboost import XGBRegressor
#from sklearn.tree import DecisionTreeRegressor
import data_handler as dh

def train_model():
    
    x_train, x_test, y_train, y_test, c_transformer, scaler = dh.get_data(r"C:\Users\DELL\Downloads\ai_nov21-main\ai_nov21\Chapter 2\06. Trees\treenew\insurance.csv")
    
    xgb_r = XGBRegressor()
    gboosting_r = GradientBoostingRegressor(learning_rate=0.01, n_estimators=50)
    dtree_r = DecisionTreeRegressor(random_state=42, max_depth=4 )
    
    xgb_r.fit(x_train,y_train)
    gboosting_r.fit(x_train, y_train)
    dtree_r.fit(x_train, y_train)
    
    return xgb_r , gboosting_r, dtree_r , scaler,c_transformer

train_model()



    
    
    


