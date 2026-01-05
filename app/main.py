from fastapi import FastAPI,APIRouter
from app.api.endpoints import calendly_intgration_api

app = FastAPI(
    title="Mock Calendly Scheduling API",
    description="Calendly-style appointment scheduling mock service for a medical clinic",
    version="1.0",
    docs_url="/model/api/docs",
)
calendly_intgration=APIRouter()
calendly_intgration.include_router(
    calendly_intgration_api.router
)

app.include_router(calendly_intgration, prefix="/api/calendly")
