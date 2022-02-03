import data_train as dt
import pandas as pd
import numpy as np
model = dt.train_model()

while True:
    #columns names indicates with datatypes to excute in cli and features 
    age = int(input("How old are you? \n"))
    sex = str(input("Which is your sex? If you are a male answer 'm', if you are a female answer with an 'f': \n"))
    if sex.lower() == 'm':
        sex = 'male'
    else:
        sex = 'female'
    bmi = float(input("Which is your bmi ('Body mass index')? \n"))
    child = int(input("How many children do you have? \n"))
    region = str(input("Which is your residential area in the US? Options: northeast, southeast, southwest, northwest \n"))
    charges = float(input("How much you will charges \n"))

    #Preprocess
    #ct is column transform taken from model
    ct = model[2]
    #scaler taken from model 
    scaler = model[3]
    x = pd.DataFrame({"age":age, "sex":sex, "bmi":bmi, "child":child, "region":region, "charges":charges}, index=[0])
    x_trans = ct.fit_transform(x)
    x_scaled = scaler.transform(x_trans)

    #Predict 

    predictions = np.array([clf.predict(x_scaled) for clf in model[:2]])

    print(f"Prediction for your conditions: {predictions}")