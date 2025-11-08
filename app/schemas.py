#qui definisco il modello pydantic con cui richiedo le informazioni all'utente in una richiesta HTTP e decido cosa mostrare nelle risposte json

#importo le librerie necessarie:
from pydantic import BaseModel
from datetime import datetime

class UsersBase(BaseModel):
    name: str
    surname: str
    email: str
    phone_number: str
    registered: bool = False #di default è false

#ne posso creare altre che ereditano da UsersBase per usi specifici, ad esempio:
class UsersCreate(UsersBase):
    pass

#in più posso definire precisamente la risposta della richiesta http
class UsersResponse(UsersBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True