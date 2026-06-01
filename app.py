from flask import Flask, request, render_template
import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler
from src.pipelines.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)
app = application

##Route for a home page

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/predictdata',methods=['GET','POST'])
# def predict_datapoint():
#    if request.method=='GET':
#       return render_template('home.html')
#    else:
#       data = CustomData(
#     age=int(request.form.get('age')),
#     sex=request.form.get('sex'),
#     bmi=float(request.form.get('bmi')),
#     children=int(request.form.get('children')),
#     smoker=request.form.get('smoker'),
#     region=request.form.get('region')
# )
      
#       pred_df=data.get_data_as_data_frame()
#       print(pred_df)
      
#       predict_pipeline=PredictPipeline()
#       results = predict_pipeline.predict(pred_df)
#       return render_template('home.html',results=round(results[0], 2))
   
@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():

    if request.method == 'GET':
        return render_template('home.html')

    else:

        try:

            data = CustomData(
                age=int(request.form.get('age')),
                sex=request.form.get('sex'),
                bmi=float(request.form.get('bmi')),
                children=int(request.form.get('children')),
                smoker=request.form.get('smoker'),
                region=request.form.get('region')
            )

            pred_df = data.get_data_as_data_frame()

            print(pred_df)

            predict_pipeline = PredictPipeline()

            results = predict_pipeline.predict(pred_df)

            return render_template(
                'home.html',
                results=round(results[0], 2)
            )

        except Exception as e:

            error_text = str(e)

            if "Age must be" in error_text:
                user_error = "Age must be between 18 and 100."

            elif "BMI must be" in error_text:
                user_error = "BMI must be between 10 and 60."

            elif "Children" in error_text:
                user_error = "Children count must be between 0 and 10."

            else:
                user_error = "Invalid input. Please review your entries."

            return render_template(
               "home.html",
               error_message=user_error
            )
import os

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )