from flask import Flask, request, jsonify, render_template
#from flask_ngrok import run_with_ngrok
import numpy as np
import pickle


app = Flask(__name__)
#run_with_ngrok(app)

    
model_RF=pickle.load(open('Major_RF.pkl', 'rb')) 
model_KNN=pickle.load(open('Major_KNN.pkl', 'rb')) 
model_K_SVM=pickle.load(open('Major_SVM_linear.pkl', 'rb')) 
model_DT=pickle.load(open('Major_DT.pkl', 'rb')) 
model_NB=pickle.load(open('Major_NB.pkl', 'rb')) 



@app.route('/')
def home():
  
    return render_template("index.html")
#------------------------------About us-------------------------------------------
@app.route('/aboutusnew')
def aboutusnew():
    return render_template('aboutusnew.html')
  
@app.route('/predict',methods=['GET'])

def predict():
    
     
    age = float(request.args.get('age'))
    sex = float(request.args.get('sex'))
    chest_pain = float(request.args.get('chest_pain'))
    bp = float(request.args.get('bp'))
    st = float(request.args.get('st'))


 
    Model = (request.args.get('Model'))

    if Model=="Random Forest Classifier":
      prediction = model_RF.predict([[age, sex, chest_pain, bp, st]])

    elif Model=="Decision Tree Classifier":
      prediction = model_DT.predict([[age, sex, chest_pain, bp, st]])

    elif Model=="KNN Classifier":
      prediction = model_KNN.predict([[age, sex, chest_pain, bp, st]])

    elif Model=="SVM Classifier":
      prediction = model_K_SVM.predict([[age, sex, chest_pain, bp, st]])

    else:
      prediction = model_NB.predict([[age, sex, chest_pain, bp, st]])

    
    if prediction == [0]:
      return render_template('index.html', prediction_text="NO heart disease", extra_text =" -- Prediction by " + Model)

    else :
      return render_template('index.html', prediction_text='heart disease', extra_text =" -- Prediction by " + Model)

#app.run()
if __name__ == "__main__":
  app.run(debug=True)

