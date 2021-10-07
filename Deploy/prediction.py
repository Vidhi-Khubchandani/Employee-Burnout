
import streamlit as st
import pickle 
import pandas as pd
import numpy as np
import sklearn        
import datetime 
from datetime import datetime, date, time
    
def load_model():
    line = open('cat_model_pickle','rb')
    cat_model=pickle.load(line)
    return cat_model

def Prediction(Employee_ID, Date_of_Joining, Gender, Company_Type, WFH_Setup_Available, Designation, Resource_Allocation, Mental_Fatigue_Score):

    Mental_Fatigue_Score = 0
    Resource_Allocation = 0 
    Designation = 0


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
        Designation = 1

    elif Designation > 3.0 and Designation <= 5.0:
        Designation = 2

    else:    
       Designation = -1        

# Resource Allocation
    if Resource_Allocation > 3.0 and Resource_Allocation <= 6.0:
        Resource_Allocation = 1
    elif Resource_Allocation > 6.0 and Resource_Allocation <= 10.0:
        Resource_Allocation = 2
    else:    
        Resource_Allocation = -1

# Mental Fatigue Score
    if Mental_Fatigue_Score > 4.0 and Mental_Fatigue_Score <= 5.0:
        Mental_Fatigue_Score=1
    elif Mental_Fatigue_Score > 5.0 and Mental_Fatigue_Score <= 6.0:
      Mental_Fatigue_Score=2
    elif Mental_Fatigue_Score > 6.0 and Mental_Fatigue_Score <= 7.0:
       Mental_Fatigue_Score=3
    elif Mental_Fatigue_Score> 7.0:
        Mental_Fatigue_Score=4
    else:
        Mental_Fatigue_Score=-1  

# date time convert 
    Date_Today = pd.to_datetime('today')

    Date_of_Joining = pd.to_datetime(Date_of_Joining)
    Date_of_Joining = pd.to_datetime(Date_of_Joining)
    Date_of_Joining = Date_Today - Date_of_Joining        

    return load_model().predict([[Employee_ID, Date_of_Joining, Gender, Company_Type, WFH_Setup_Available, Designation, Resource_Allocation, Mental_Fatigue_Score]])

def main():

    st.title("Calculate Employee Burnout Score")

    Employee_ID=st.text_input('Employee ID')  

    Date_of_Joining  = st.date_input('Date_of_Joining')
      
    Gender=st.selectbox('Gender',("Male","Female")) 

    Company_Type=st.selectbox('Company Type',("Product","Service")) 

    WFH_Setup_Available=st.selectbox('WFH Setup Available',("Yes","No")) 

    Designation=st.slider('Designation Level(1 - Lowest , 5 - Highest)',1,5,2)

    Resource_Allocation=st.slider('No. of Working Hours',1,10,4)

    Mental_Fatigue_Score=st.slider('Approx mental fatigue Rating',0.0,10.0,3.0)

    ok = st.button("Predict")

    if ok:
        Score = load_model.predict([[Employee_ID, Date_of_Joining, Gender, Company_Type, WFH_Setup_Available, Designation, Resource_Allocation, Mental_Fatigue_Score]])

        if Score<= 0.3:
            st.subheader(f"Your have Low Burnout")
        elif Score <=0.7 and Score > 0.3:
            st.subheader(f"Your have Moderate Burnout")
        else:
            st.subheader(f"Your have High Burnout")

       