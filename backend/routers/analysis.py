from fastapi import APIRouter
from finance.analyzer import FinancialAnalyzer

router = APIRouter()

@router.get("/analysis/{ticker}")
def analyze_company(ticker: str):
    analyzer = FinancialAnalyzer()
    return analyzer.analyze(ticker)