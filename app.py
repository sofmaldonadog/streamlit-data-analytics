import streamlit as st
import pandas as pd

st.title("Hola Mundo!")
st.header("Esto es un header")
st.markdown("*i cooka da pizza*")

df = pd.read_csv("train.csv")
st.dataframe(df)