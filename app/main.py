from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="KRX 저평가 종목 API")

app.include_router(router)