from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
import matplotlib
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('Customer_Churn_Prediction.pkl', 'rb'))
@app.route('/', methods=['GET'])
def Home():
    return render_template('index.html')

standard_to = StandardScaler()
@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        days_since_last_login = int(request.form['days_since_last_login'])
        Age = int(request.form['Age'])
        avg_time_spent = int(request.form['avg_time_spent'])
        avg_transaction_value = float(request.form['avg_transaction_value'])
        points_in_wallet = float(request.form['points_in_wallet'])
        gender = float(request.form['Gender'])
        region_category = int(request.form['Region Category'])
        membership_category = float(request.form['Membership Category'])
        year = float(request.form['Year'])
        joined_through_Referral= float(request.form['Joined through Referral'])
        preferred_offer_type = float(request.form['Preferred Offer Type'])
        Medium_of_Operation = float(request.form['Medium of Operation'])
        Internet_Option = float(request.form['Internet Option'])
        Used_Special_Discount=  float(request.form['Used Special Discount'])
        Offer_Application_Preference=  float(request.form['Offer Application Preference'])
        Past_Complain_Code=  float(request.form['Past Complain Code'])
        Complaint_Status =  float(request.form['Complaint Status'])
        Feedback=  float(request.form['Feedback'])
        




       
           
        

        
        prediction = model.predict([[Age,days_since_last_login,avg_time_spent,avg_transaction_value,points_in_wallet,gender,region_category ,membership_category,year,
          joined_through_Referral,
        preferred_offer_type,
        Medium_of_Operation,
        Internet_Option,
        Used_Special_Discount,
        Offer_Application_Preference,
        Past_Complain_Code,
        Complaint_Status,
        Feedback]])
        if prediction < 3 :
             return render_template('index.html',prediction_text="The Customer will churn")
        else:
             return render_template('index.html',prediction_text="The Customer will not  churn ")
                
if __name__=="__main__":
    app.run(debug= False)
