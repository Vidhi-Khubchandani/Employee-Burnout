import streamlit as st
from prediction import main

page = st.sidebar.selectbox("Explore or Predict",("Predict","Explore"))

if page == "Predict":
    main()


