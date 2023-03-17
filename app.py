import pickle
import sklearn
import streamlit as st
import numpy as np 
model=pickle.load(open("model.pickle","rb"))
st.title("Revenue Prediction")
t= st.number_input("Input Temperature")
t=np.array(t)
t=t.reshape(-1,1)
if st.button("Predict"):
  y = model.predict(t)
  st.success(*y)
