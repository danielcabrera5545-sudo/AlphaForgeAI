from sqlalchemy import create_engine

DATABASE_URL = "postgresql+psycopg2://postgres:2701@127.0.0.1:5432/alphaforge"

engine = create_engine(
    DATABASE_URL,
    echo=True
)
