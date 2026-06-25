from datetime import datetime

from pydantic import BaseModel, ConfigDict


class CompanyResponse(BaseModel):

    id: int
    ticker: str
    company_name: str
    sector: str
    industry: str
    market_cap: int
    created_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )