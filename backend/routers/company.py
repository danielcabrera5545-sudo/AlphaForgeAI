from backend.schemas.company import CompanyResponse
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.database.session import get_db
from backend.services.market_data import MarketDataService

router = APIRouter()


@router.get(
    "/company/{ticker}",
    response_model=CompanyResponse,
)
def company_info(
    ticker: str,
    db: Session = Depends(get_db)
):
    service = MarketDataService(db)

    return service.get_company_info(ticker)