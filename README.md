# FastAPI CRUD User Management
![Python](https://img.shields.io/badge/python-3.11+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.111-green.svg)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue.svg)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-orange.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)


Un progetto backend CRUD realizzato con **FastAPI**, **SQLAlchemy** e **Pydantic**, con connessione a **PostgreSQL**.
## 🎓 Obiettivi del progetto
Questo progetto è stato sviluppato come esercizio di backend development con FastAPI.
L’obiettivo principale è comprendere il funzionamento di un’architettura CRUD moderna,
utilizzando un ORM (SQLAlchemy) per la gestione del database e Pydantic per la validazione dei dati.
Il progetto è una base solida per future implementazioni di autenticazione, sicurezza e interfacce utente.


## 🚀 Funzionalità
- Creazione, lettura, aggiornamento ed eliminazione utenti (CRUD)
- Database gestito con SQLAlchemy e PostgreSQL
- Validazione dei dati tramite Pydantic
- Documentazione automatica Swagger (`/docs`) integrata in FastAPI

## 🧱 Struttura del progetto
app/
├── main.py # Avvio dell'app FastAPI
├── database.py # Connessione e sessione al DB
├── models.py # Tabelle SQLAlchemy
├── schemas.py # Modelli Pydantic


## 🧰 Tecnologie utilizzate
- FastAPI
- SQLAlchemy
- Pydantic
- Uvicorn
- PostgreSQL
- Psycopg2

## ▶️ Come eseguire il progetto

```bash
# 1. Crea un virtual environment
python -m venv venv
source venv/bin/activate   # o su Windows: venv\Scripts\activate

# 2. Installa le dipendenze
pip install -r requirements.txt

# 3. Avvia il server
uvicorn app.main:app --reload
