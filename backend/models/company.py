from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import BigInteger
from sqlalchemy import DateTime
from datetime import datetime

from backend.database.base import Base


class Company(Base):

    __tablename__ = "companies"

    id = Column(Integer, primary_key=True)

    ticker = Column(String, unique=True)

    company_name = Column(String)

    sector = Column(String)

    industry = Column(String)

    market_cap = Column(BigInteger)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )