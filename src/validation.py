# src/validation.py

class DataValidator:
    
    @staticmethod
    def validate_input(data):
        
        errors = []

        # Age validation
        if data["age"] < 18 or data["age"] > 100:
            errors.append("Age must be between 18 and 100")

        # BMI validation
        if data["bmi"] < 10 or data["bmi"] > 60:
            errors.append("BMI must be between 10 and 60")

        # Children validation
        if data["children"] < 0 or data["children"] > 10:
            errors.append("Children count must be between 0 and 10")

        # Sex validation
        if data["sex"] not in ["male", "female"]:
            errors.append("Invalid sex value")

        # Smoker validation
        if data["smoker"] not in ["yes", "no"]:
            errors.append("Invalid smoker value")

        # Region validation
        if data["region"] not in [
            "southwest",
            "southeast",
            "northwest",
            "northeast"
        ]:
            errors.append("Invalid region value")

        return errors