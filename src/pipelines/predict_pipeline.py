import os
import sys
import pandas as pd

from src.exception import CustomException
from src.utils import load_object
from src.validation import DataValidator
from src.prediction_logger import PredictionLogger


class PredictPipeline:

    def __init__(self):
        pass

    def predict(self, features):

        try:
            model_path = os.path.join("artifacts", "model.pkl")
            preprocessor_path = os.path.join("artifacts", "preprocessor.pkl")

            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)

            data_scaled = preprocessor.transform(features)

            preds = model.predict(data_scaled)

            # Convert dataframe row into dictionary
            input_data = features.iloc[0].to_dict()

            # Log successful prediction
            PredictionLogger.log_prediction(
                input_data,
                float(preds[0])
            )

            return preds

        except Exception as e:

            try:
                PredictionLogger.log_exception(
                    features.to_dict(),
                    str(e)
                )
            except:
                pass

            raise CustomException(e, sys)


class CustomData:

    def __init__(
        self,
        age: int,
        sex: str,
        bmi: float,
        children: int,
        smoker: str,
        region: str
    ):

        self.age = age
        self.sex = sex
        self.bmi = bmi
        self.children = children
        self.smoker = smoker
        self.region = region

    def get_data_as_data_frame(self):

        try:

            input_data = {
                "age": self.age,
                "sex": self.sex,
                "bmi": self.bmi,
                "children": self.children,
                "smoker": self.smoker,
                "region": self.region
            }

            # VALIDATION STEP
            validation_errors = DataValidator.validate_input(
                input_data
            )

            # IF INVALID → LOG + STOP
            if validation_errors:

                PredictionLogger.log_exception(
                    input_data,
                    validation_errors
                )

                raise ValueError(validation_errors)

            # CREATE DATAFRAME
            custom_data_input_dict = {
                "age": [self.age],
                "sex": [self.sex],
                "bmi": [self.bmi],
                "children": [self.children],
                "smoker": [self.smoker],
                "region": [self.region],
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)