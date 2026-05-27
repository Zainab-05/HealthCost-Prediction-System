# src/prediction_logger.py

import pandas as pd
import os
from datetime import datetime

LOG_DIR = "logs"

prediction_log_file = os.path.join(LOG_DIR, "prediction_logs.csv")
exception_log_file = os.path.join(LOG_DIR, "exception_logs.csv")

os.makedirs(LOG_DIR, exist_ok=True)


class PredictionLogger:

    @staticmethod
    def log_prediction(data, prediction):

        log_data = {
            "timestamp": datetime.now(),
            "age": data["age"],
            "bmi": data["bmi"],
            "children": data["children"],
            "sex": data["sex"],
            "smoker": data["smoker"],
            "region": data["region"],
            "prediction": prediction
        }

        df = pd.DataFrame([log_data])

        if os.path.exists(prediction_log_file):
            df.to_csv(prediction_log_file, mode='a', header=False, index=False)
        else:
            df.to_csv(prediction_log_file, index=False)

    @staticmethod
    def log_exception(data, errors):

        log_data = {
            "timestamp": datetime.now(),
            "input_data": str(data),
            "errors": str(errors)
        }

        df = pd.DataFrame([log_data])

        if os.path.exists(exception_log_file):
            df.to_csv(exception_log_file, mode='a', header=False, index=False)
        else:
            df.to_csv(exception_log_file, index=False)