import streamlit as st
from sklearn import datasets



st.title("obesity")
st.write("table")


df = pd.read_csv("https://raw.githubusercontent.com/chriswmann/datasets/master/500_Person_Gender_Height_Weight_Index.csv")
st.write(df)