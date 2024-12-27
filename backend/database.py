from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL подключения к базе данных PostgreSQL
DATABASE_URL = "postgresql+psycopg2://username:password@localhost:5432/dbname"

# Создание подключения
engine = create_engine(DATABASE_URL)

# Создание базового класса для моделей
Base = declarative_base()

# Создание фабрики для сессий
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
