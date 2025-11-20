import pickle
from pathlib import Path
import numpy as np
from app.schemas import PredictionResponse

class IrisModel:
    def __init__(self):
        model_path = Path("models/classifier.pkl")
        with open(model_path, "rb") as f:
            self.model = pickle.load(f)
        
    def predict(self, input_data):
        X = np.array([[
            input_data.sepal_length,
            input_data.sepal_width,
            input_data.petal_length,
            input_data.petal_width
        ]])
        pred = self.model.predict(X)[0]
        return PredictionResponse(prediction=int(pred))
