from pydantic import BaseModel

class PredictRequest(BaseModel):
    model_name: str
    input_text: str

class PredictResponse(BaseModel):
    prediction: str
    confidence: float
    model_used: str
