# src/prediction_logger.py

import pandas as pd
import os
from datetime import datetime

BASE_DIR = os.getcwd()

LOG_DIR = os.path.join(BASE_DIR, "logs")

prediction_log_file = os.path.join(
    LOG_DIR,
    "prediction_logs.csv"
)

exception_log_file = os.path.join(
    LOG_DIR,
    "exception_logs.csv"
)

os.makedirs(LOG_DIR, exist_ok=True)

print("Logger initialized")
print("Prediction log path:", prediction_log_file)
print("Exception log path:", exception_log_file)


class PredictionLogger:

    @staticmethod
    def log_prediction(data, prediction):

        age = data["age"]

        if age < 30:
            age_group = "18-29"
        elif age < 50:
            age_group = "30-49"
        else:
            age_group = "50+"

        bmi = data["bmi"]

        if bmi < 18.5:
            bmi_category = "Underweight"
        elif bmi < 25:
            bmi_category = "Normal"
        elif bmi < 30:
            bmi_category = "Overweight"
        else:
            bmi_category = "Obese"

        if prediction < 10000:
            risk_category = "Low Risk"
        elif prediction < 25000:
            risk_category = "Medium Risk"
        else:
            risk_category = "High Risk"

        high_cost_flag = "Yes" if prediction >= 25000 else "No"
        
        smoker_flag = "Smoker" if data["smoker"] == "yes" else "Non-Smoker"

        family_type = (
         "Large Family"
         if data["children"] >= 3
         else "Small Family" )
        
        log_data = {
            "timestamp": datetime.now(),
            "age": age,
            "age_group": age_group,
            "bmi": bmi,
            "bmi_category": bmi_category,
            "children": data["children"],
            "sex": data["sex"],
            "smoker": data["smoker"],
            "region": data["region"],
            "prediction": prediction,
            "risk_category": risk_category,
            "high_cost_flag": high_cost_flag,
            "smoker_flag": smoker_flag,
            "family_type": family_type
        }

        print("Inside log_prediction")

        df = pd.DataFrame([log_data])

        if os.path.exists(prediction_log_file):
            df.to_csv(
                prediction_log_file,
                mode="a",
                header=False,
                index=False
            )
        else:
            df.to_csv(
                prediction_log_file,
                index=False
            )

        print("Prediction logged successfully")

    @staticmethod
    def log_exception(data, errors):

        error_text = str(errors)

        if isinstance(errors, list) and len(errors) > 1:
            error_type = "Multiple Validation Errors"

        elif "Age" in error_text:
            error_type = "Age Validation"

        elif "BMI" in error_text:
            error_type = "BMI Validation"

        elif "Children" in error_text:
            error_type = "Children Validation"

        elif "sex" in error_text.lower():
            error_type = "Sex Validation"

        elif "smoker" in error_text.lower():
            error_type = "Smoker Validation"

        elif "region" in error_text.lower():
            error_type = "Region Validation"

        else:
            error_type = "Unknown Error"

        log_data = {
            "timestamp": datetime.now(),
            "error_type": error_type,
            "input_data": str(data),
            "errors": error_text
        }

        print("Inside log_exception")

        df = pd.DataFrame([log_data])

        if os.path.exists(exception_log_file):
            df.to_csv(
                exception_log_file,
                mode="a",
                header=False,
                index=False
            )
        else:
            df.to_csv(
                exception_log_file,
                index=False
            )

        print("Exception logged successfully")