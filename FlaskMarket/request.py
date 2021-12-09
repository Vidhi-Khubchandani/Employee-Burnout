from flask import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'Employee ID':"24368dbguw3", 'Date of Joining':2008-11-10, 'Gender':"Male", 'Company Type':"Service",'WFH Setup available':"Yes", 'Designation':2.0, 'Resource Allocation':4.0, 'Mental Fatigue Score': 5.6})

print(r.json())