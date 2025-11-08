# FastAPI CRUD User Management

Un progetto backend CRUD realizzato con **FastAPI**, **SQLAlchemy** e **Pydantic**, con connessione a **PostgreSQL**.

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
