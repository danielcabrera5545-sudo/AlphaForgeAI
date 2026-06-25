from backend.database.connection import engine
from backend.database.base import Base

from backend.models.company import Company

Base.metadata.create_all(bind=engine)

print("Database Initialized")
