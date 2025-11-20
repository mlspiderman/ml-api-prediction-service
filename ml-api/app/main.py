from fastapi import FastAPI
from app.model import IrisModel
from app.schemas import IrisInput, PredictionResponse

app = FastAPI(
    title="ML Classification API",
    description="Simple ML model served via FastAPI",
    version="1.0")

model = IrisModel()

@app.post("/predict", response_model=PredictionResponse)
def predict(input_data: IrisInput):
    return model.predict(input_data)
