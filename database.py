# igreja_mvp/database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///igreja.db"

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False} # Necessário para SQLite com GUI
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def init_db():
    # Importe todos os modelos aqui para que sejam registrados no Base
    import models
    Base.metadata.create_all(bind=engine)
    print("Banco de dados inicializado e tabelas criadas.")