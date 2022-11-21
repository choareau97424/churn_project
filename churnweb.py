import streamlit as st
import pandas as pd
from PIL import Image
import json
import requests

 # Query
web_api = requests.post("172.50.0.3:8001")
json_str = json.dumps(web_api.json())
respon = json.loads(json_str)
st.subheader(f"{respon[0]}")

 
    
# About
st.write(
    """
    ## About
     In this project we defined the forecast the customer which are at risk of churning 
    **This Streamlit App  utilizes a Machine Learning model(randomforest) API in order to detect whether the customers from a Telco company will churns or not**
    The notebook, model, documentationand  analysis are available on [Github]()

    Made by christophe & william
    """)

def main():
    
    image = Image.open('images/customer_churn.png')
    image2 = Image.open('images/icone.png')
    st.image(image,use_column_width=False)
    add_selectbox = st.sidebar.selectbox("How would you like to predict?",("Online", "Batch"))
    st.sidebar.info('Prediction Customer Churn')
    st.sidebar.image(image2)
    st.title("Predicting Customer Churn")
    if add_selectbox == 'Online':
        gender = st.selectbox('Gender', ['male', 'female'])
        seniorcitizen= st.selectbox(' Customer is a senior citizen', [0, 1])
        partner= st.selectbox(' Customer has a partner', ['yes', 'no'])
        dependents = st.selectbox("Does the customer live with any dependents(children, parents, etc.)?", ['yes', 'no'])
        tenure= st.number_input('Number of months the customer has been with the provider', min_value=0, max_value=120, value=0)
        phoneservice = st.selectbox(' Customer has phoneservice:', ['yes', 'no'])
        multiplelines = st.selectbox(' multiple Internet line services?', ['yes', 'no', 'no_phone_service'])
        internetservice= st.selectbox(' Customer has online security service ', ['dsl', 'no', 'fiber_optic'])
        onlinesecurity= st.selectbox(' Customer has online security service', ['yes', 'no', 'no_internet_service'])
        onlinebackup = st.selectbox(' Customer has online backup service', ['yes', 'no', 'no_internet_service'])
        deviceprotection = st.selectbox(' Customer has device protection service', ['yes', 'no', 'no_internet_service'])
        techsupport = st.selectbox(' Customer has tech support service', ['yes', 'no', 'no_internet_service'])
        streamingtv = st.selectbox(' Customer has streaming tv service', ['yes', 'no', 'no_internet_service'])
        streamingmovies = st.selectbox(' Customer has streaming movies service', ['yes', 'no', 'no_internet_service'])
        contract= st.selectbox(" Which customer's current contract type?", ['month-to-month', 'one_year', 'two_year'])
        paperlessbilling = st.selectbox(' Customer has a Paperless billing', ['yes', 'no'])
        paymentmethod= st.selectbox('Payment method', ['Bank_transfer_(automatic)', 'Credit_card_(automatic)', 'Electronic_check' ,'Mailed_check'])
        monthlycharges= st.number_input('Monthly charges :', min_value=0, max_value=240, value=0,format="%.2f")
        totalcharges = tenure*monthlycharges
        output= ""
        output_prob = ""
        data={
				"gender":gender ,
				"seniorcitizen": seniorcitizen,
				"partner": partner,
				"dependents": dependents,
    			"tenure": tenure,
				"phoneservice": phoneservice,
				"multiplelines": multiplelines,
				"internetservice": internetservice,
				"onlinesecurity": onlinesecurity,
				"onlinebackup": onlinebackup,
				"deviceprotection": deviceprotection,
				"techsupport": techsupport,
				"streamingtv": streamingtv,
				"streamingmovies": streamingmovies,
				"contract": contract,
				"paperlessbilling": paperlessbilling,
				"paymentmethod": paymentmethod,
				"monthlycharges": monthlycharges,
				"totalcharges": totalcharges
			}
        if st.button("Predict"):
            X = respon.transform([data])
            y_pred = respon.predict_proba(X)[0, 1]
            churn = y_pred >= 0.5
            output_prob = float(y_pred)
            output = bool(churn)
            st.success('Churn: {0}, Risk Score: {1}'.format(output, output_prob))
            
        if add_selectbox == 'Batch':
            file_upload = st.file_uploader("Upload csv file for predictions", type=["csv"])
        if file_upload is not None:
            data = pd.read_csv(file_upload)
            X = respon.transform([data])
            y_pred = respon.predict_proba(X)[0, 1]
            churn = y_pred >= 0.5
            churn = bool(churn)
            st.write(churn)
  
   