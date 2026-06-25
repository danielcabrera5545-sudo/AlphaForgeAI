from sqlalchemy.orm import Session

from backend.models.company import Company


class CompanyRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_company(self, ticker: str):

        return (
            self.db.query(Company)
            .filter(
                Company.ticker == ticker
            )
            .first()
        )

    def create_company(
        self,
        ticker,
        company_name,
        sector,
        industry,
        market_cap,
    ):

        company = Company(
            ticker=ticker,
            company_name=company_name,
            sector=sector,
            industry=industry,
            market_cap=market_cap,
        )

        self.db.add(company)

        self.db.commit()

        self.db.refresh(company)

        return company