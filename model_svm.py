import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR 
def model(to_predict):
    df=pd.read_csv("train_set.csv")
    le=LabelEncoder()
    df['Date']=le.fit_transform(df['Date'])
    x=df.iloc[:,2:6].values
    y=df.iloc[:,6:7].values
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 100)
    sc=StandardScaler()
    X_train=sc.fit_transform(X_train)
    X_test=sc.fit_transform(X_test)
    regressor_svm=SVR(kernel='rbf')
    regressor_svm.fit(X_train,y_train)
    test=sc.fit_transform(to_predict)
    y_new_test=regressor_svm.predict(test)
    if(y_new_test <2.5):
        y_new_test=np.round(y_new_test-0.5)
    else:
        y_new_test=np.round(y_new_test+0.5)
    return y_new_test[0]

def predict_result_svm(CodedDay,Zone,Weather,Temperature):
    c=int(CodedDay)
    z=int(Zone)
    w=int(Weather)
    t=int(Temperature)
    values=[]
    values.append(c)
    values.append(z)
    values.append(w)
    values.append(t)
    to_predict=[]
    to_predict.append(values)
    prediction= model(to_predict)
    return prediction


