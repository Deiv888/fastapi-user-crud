#in questo file scrivo il codice per la connessione con il database postgresql


#importo le librerie sql alchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#URL DATABASE
SQLALCHEMY_DATABASE_URL = "postgresql://DATABASE_USERNAME:DATABASE_PASSWORD@DATABASE_HOSTNAME/DATABASE_NAME"

#creo l'engine che permette la connnesione con il mio database
engine = create_engine(SQLALCHEMY_DATABASE_URL)

#avvio una sessione locale
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#definisco la base
Base = declarative_base()

#funzione per la connessione con il database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()