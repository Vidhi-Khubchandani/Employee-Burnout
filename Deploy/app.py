import streamlit as st
from predict import main

page = st.sidebar.selectbox("Explore or Predict",("Predict","Explore"))

if page == "Predict":
    main()


