from fastapi import FastAPI

from backend.routers import analysis
from backend.routers import company
from backend.api.v1 import health

app = FastAPI(
    title="AlphaForge AI",
    description="Institutional AI Equity Research Platform",
    version="1.0.0"
)

app.include_router(health.router)
app.include_router(company.router)
app.include_router(analysis.router)