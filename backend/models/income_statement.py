from sqlalchemy import (
    Column,
    Integer,
    String,
    BigInteger,
    ForeignKey,
    Date
)

from sqlalchemy.orm import relationship

from backend.database.base import Base


class IncomeStatement(Base):
    __tablename__ = "income_statements"

    id = Column(Integer, primary_key=True)

    company_id = Column(
        Integer,
        ForeignKey("companies.id")
    )

    fiscal_date = Column(Date)

    revenue = Column(BigInteger)

    gross_profit = Column(BigInteger)

    operating_income = Column(BigInteger)

    net_income = Column(BigInteger)

    company = relationship(
        "Company",
        back_populates="income_statements"
    )