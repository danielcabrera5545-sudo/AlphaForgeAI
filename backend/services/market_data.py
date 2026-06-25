import yfinance as yf

from sqlalchemy.orm import Session

from backend.database.repositories.company_repository import CompanyRepository


class MarketDataService:

    def __init__(self, db: Session):
        self.db = db
        self.repository = CompanyRepository(db)

    def get_company_info(self, ticker):

        company = self.repository.get_company(ticker.upper())

        if company:

            print("Loaded from PostgreSQL")

            return company

        print("Downloading from Yahoo Finance")

        stock = yf.Ticker(ticker)

        info = stock.info

        company = self.repository.create_company(
            ticker=ticker.upper(),
            company_name=info.get("longName"),
            sector=info.get("sector"),
            industry=info.get("industry"),
            market_cap=info.get("marketCap"),
        )

        return company