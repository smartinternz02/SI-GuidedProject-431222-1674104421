# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 11:56:38 2022

@author: SmartBridge-PC
"""

from flask import Flask, render_template, request
import numpy as np


import pandas as pd



import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "U2H78KYjZy34DePXTfeNyaXAVYotNo-PlHu9KOBSagUo"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}


app = Flask(__name__)




@app.route("/")
def about():
    return render_template('home.html')

@app.route("/home")
def abou():
    return render_template('home.html')

@app.route("/predict")
def home1():
    return render_template('predict.html')


@app.route("/pred", methods=['POST', 'GET'])
def predict():
    #x = [[float(x) for x in request.form.values()]]
    goitre = request.form['goitre']
    tumor = request.form['tumor']
    hypopituitary = request.form['hypopituitary']
    psych = request.form['psych']
    TSH = request.form['TSH']
    T3 = request.form['T3']
    TT4 = request.form['TT4']
    T4U = request.form['T4U']
    FTI = request.form['FTI']
    TBG = request.form['TBG']
    
    x = [[float(goitre),float(tumor),float(hypopituitary),float(psych),float(TSH),float(T3),float(TT4),float(T4U),float(FTI),float(TBG)]]
    

    #col = ['goitre','tumor','hypopituitary','psych','TSH','T3','TT4','T4U','FTI','TBG']

   
    #print(x.shape)

    print(x)
    
    payload_scoring = {"input_data": [{"field": [['goitre','tumor','hypopituitary','psych','TSH','T3','TT4','T4U','FTI','TBG']], "values": x}]}
    
    print(payload_scoring)

    response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/a0ea54a0-71de-438d-8e55-9edd0df906c8/predictions?version=2023-02-07', json=payload_scoring,
     headers={'Authorization': 'Bearer ' + mltoken})


    '''response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/5eaeceaa-e202-46d8-b2e1-58dc290e4183/predictions?version=2022-07-04', json=payload_scoring,
     headers={'Authorization': 'Bearer ' + mltoken})'''
    
    print("Scoring response")
    print(response_scoring.json())
    
    #pred = model.predict(x)
    #pred = le.inverse_transform(pred)
    #print(pred[0])
    predictions=response_scoring.json()
    print(predictions)
    
    pred = predictions['predictions'][0]['values'][0][0]
    print(pred[0])
    return render_template('submit.html', prediction_text=str(pred))

if __name__ == "__main__":
    app.run(debug=False)
                        
    
    
    
