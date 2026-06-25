from backend.services.market_data import MarketDataService
from finance.ratios import price_to_book


class FinancialAnalyzer:

    def __init__(self):
        self.market = MarketDataService()

    def analyze(self, ticker):

        company = self.market.get_company_info(ticker)

        pb = price_to_book(
            company["current_price"],
            company["book_value"]
        )

        return {
            "company": company["company"],
            "ticker": company["ticker"],
            "sector": company["sector"],
            "industry": company["industry"],
            "market_cap": company["market_cap"],
            "current_price": company["current_price"],
            "price_to_book": pb,
            "trailing_pe": company["trailing_pe"]
        }