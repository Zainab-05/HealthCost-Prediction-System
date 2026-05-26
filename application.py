from flask import Flask,request,render_template
import pandas as pd
import numpy as pd

from sklearn.preprocessing import StandardScaler
from src.pipelines.predict_pipeline import CustomData,PredictPipeline

application=Flask(__name__)

app=application

##Route for a home page

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
   if request.method=='GET':
      return render_template('home.html')
   else:
      data=data = CustomData(
    age=int(request.form.get('age')),
    sex=request.form.get('sex'),
    bmi=float(request.form.get('bmi')),
    children=int(request.form.get('children')),
    smoker=request.form.get('smoker'),
    region=request.form.get('region')
)
      
      pred_df=data.get_data_as_data_frame()
      print(pred_df)
      
      predict_pipeline=PredictPipeline()
      results = predict_pipeline.predict(pred_df)
      return render_template('home.html',results=round(results[0],2))
   
if __name__=="__main__":
   app.run(host="0.0.0.0")