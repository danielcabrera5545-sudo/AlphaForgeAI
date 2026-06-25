from fastapi import APIRouter
from backend.services.market_data import MarketDataService

router = APIRouter()

@router.get("/company/{ticker}")
def company_info(ticker: str):
    service = MarketDataService()
    return service.get_company_info(ticker)