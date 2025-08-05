from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import predict

app = FastAPI(
    title="ML Model Deployment Showcase",
    description="Test and log deployed ML models with real-time results.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(predict.router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "ML Model API is live"}
