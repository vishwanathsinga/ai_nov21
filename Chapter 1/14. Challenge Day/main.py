import streamlit as st
import numpy as np
from sklearn import datasets


st.title("hello  world")

st.title("comparing the best ML classifier")

data_select = st.sidebar.selectbox("select your dataset", ("wine data", "iris data", "cancer data"))

st.write(data_select)

classifier_select = st.sidebar.selectbox("select your classifier", ("svn", "random forest", "decent"))


def load_data(data_select):
    if data_select == "wine data":
        df = datasets.load_wine()
    elif data_select == "iris data":
        df = datasets.load_iris()
    else:
        df = datasets.load_cancer()
    x = df.data
    y = df.target
    return x, y


x,y = load_data(data_select) 
st.write("shape of the data: ", x.shape)
st.write("length of y: ", len(np.unique(y)))





