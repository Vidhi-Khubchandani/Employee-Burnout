
import streamlit as st
import pickle 
import numpy as np
import pandas as pd
import time
import datetime
from datetime import datetime, date, time
    
def load_model():
    pickle_in =  open('saved_steps.pkl', 'rb')
    classifier = pickle.load(pickle_in)
    return classifier

def Predict(Employee_ID, Date_of_Joining, Gender, Company_Type, WFH_Setup_Available, Designation, Resource_Allocation, Mental_Fatigue_Score):


    st.title("Calculate Employee Burnout Score")
    C_Mental_Fatigue_Score = 0
    C_Resource_Allocation = 0 
    C_Designation = 0


# Gender of Employee   
    if Gender == "Female":
        Gender = 1
    else:
        Gender = 0

#Company Type 
    if Company_Type == "Service":
        Company_Type = 1
    else:
        Company_Type = 0   

# Work from Home setup
    if WFH_Setup_Available == "Yes":
        WFH_Setup_Available = 1
    else:
        WFH_Setup_Available = 0

# Designation 

    if Designation > 1.0 and Designation <= 3.0:
        C_Designation = 1

    elif Designation > 3.0 and Designation <= 5.0:
        C_Designation = 2

    else:    
        C_Designation = -1        

# Resource Allocation
    if Resource_Allocation > 3.0 and Resource_Allocation <= 6.0:
        C_Resource_Allocation = 1
    elif Resource_Allocation > 6.0 and Resource_Allocation <= 10.0:
        C_Resource_Allocation = 2
    else:    
        C_Resource_Allocation = -1

# Mental Fatigue Score
    if Mental_Fatigue_Score > 4.0 and Mental_Fatigue_Score <= 5.0:
        C_Mental_Fatigue_Score=1
    elif Mental_Fatigue_Score > 5.0 and Mental_Fatigue_Score <= 6.0:
        C_Mental_Fatigue_Score=2
    elif Mental_Fatigue_Score > 6.0 and Mental_Fatigue_Score <= 7.0:
        C_Mental_Fatigue_Score=3
    elif Mental_Fatigue_Score> 7.0:
        C_Mental_Fatigue_Score=4
    else:
        C_Mental_Fatigue_Score=-1     

# DATE OF JOINING

    Date_Today = pd.to_datetime('today')

    Date_of_Joining = pd.to_datetime(Date_of_Joining)
    Date_of_Joining = pd.to_datetime(Date_of_Joining)
    Date_of_Joining = (Date_Today - Date_of_Joining)

    return load_model.predict( Gender, Company_Type, WFH_Setup_Available, Designation, Resource_Allocation, Mental_Fatigue_Score,C_Mental_Fatigue_Score,C_Designation,C_Resource_Allocation,Date_of_Joining)


def main():
    Employee_ID=st.text_input('Employee ID')  

    Date_of_Joining   = st.date_input('Date_of_Joining')
      
    Gender=st.selectbox('Gender',("Male","Female")) 

    Company_Type=st.selectbox('Company Type',("Product","Service")) 

    WFH_Setup_Available=st.selectbox('WFH Setup Available',("Yes","No")) 

    Designation=st.slider('Designation',1,5,2)

    Resource_Allocation=st.slider('No. of Working Hours',1,10,4)

    Mental_Fatigue_Score=st.slider('Approximate Score',0.0,10.0,3.0)

    ok = st.button("Predict")
    if ok:
        Score = load_model.Predict(Employee_ID, Date_of_Joining, Gender, Company_Type, WFH_Setup_Available, Designation, Resource_Allocation, Mental_Fatigue_Score)
        st.subheader(f"The burnout score is {Score[0]:.2f}")