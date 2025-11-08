#nel main integro l'engine che connette il db e scrivo le mie API con FASTAPI

#importo le librerie necessarie
from typing import List
from fastapi import FastAPI, Depends, status, HTTPException, Response
from . import models, schemas
from .database import engine, get_db
from sqlalchemy.orm import Session

#per integrare l'engine che connette il db
models.Base.metadata.create_all(bind=engine)

#istanza di FastApi
app = FastAPI()

#richiesta get per vedere tutti gli utenti presenti nel db
@app.get("/users", response_model=List[schemas.UsersResponse])
def get_users(db: Session = Depends(get_db)):

    users = db.query(models.Users_Table).all()
    return users

#richiesta post per aggiungere un nuovo utente al db
@app.post("/users", status_code=status.HTTP_201_CREATED, response_model=schemas.UsersResponse)
def add_user(utente: schemas.UsersCreate, db: Session = Depends(get_db)):

    new_user = models.Users_Table(**utente.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

#per ottenere un utente preciso in base all'id dal db
@app.get("/users/{id}", response_model=schemas.UsersResponse)
def get_user(id: int, db: Session = Depends(get_db)):

    user = db.query(models.Users_Table).filter(models.Users_Table.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"l'utente con id: {id} non esiste")
    return user

#per aggiornare i dati di un utente in base all'id
@app.put("/users/{id}", response_model=schemas.UsersResponse)
def update_user(id: int, utente: schemas.UsersCreate, db: Session = Depends(get_db)):

    user_query = db.query(models.Users_Table).filter(models.Users_Table.id == id)
    user_update = user_query.first()
    
    if not user_update:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"l'utente con id: {id} non esiste")
    
    user_query.update(utente.model_dump(), synchronize_session=False)
    db.commit()
    db.refresh(user_update)
    return user_update

#per eliminare un utente dal db
@app.delete("/users/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id: int, db: Session = Depends(get_db)):

    utente = db.query(models.Users_Table).filter(models.Users_Table.id == id)

    if not utente.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"l'utente con id: {id} non esiste")
    
    utente.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)