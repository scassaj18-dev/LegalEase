from fastapi import FastAPI
from routes import router

app = FastAPI(
    title="LegalEase API",
    description="AI-Powered Legal Document Generator"
)

app.include_router(router)


@app.get("/")
def root():
    return {
        "message": "LegalEase API is running"
    }