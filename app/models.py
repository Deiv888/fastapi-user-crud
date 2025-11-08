#voglio definire la mia tabella "users" che dovrà contenere le seguenti colonne:
#id, nome, cognome, email, numero_telefono, registrato, data

#importo le librerie necessarie (Base e i tipi di variabili da usare nella tabella)
from .database import Base
from sqlalchemy import Column, Integer, String, Boolean, text, TIMESTAMP

#la tabella viene creata come se fosse una classe:
class Users_Table(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    phone_number = Column(String, nullable=False)
    registered = Column(Boolean, server_default='FALSE', nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
