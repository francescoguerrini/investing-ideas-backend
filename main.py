from fastapi import FastAPI
from services.fetch_by_ticker import fetch_company_data
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "http://localhost:3000",  # URL del frontend in sviluppo
    "http://192.168.178.27:3000",  # Indirizzo IP del frontend nella tua rete locale
    "https://yourfrontenddomain.com",  # Aggiungi il dominio di produzione, se necessario
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Consenti le richieste da questi domini
    allow_credentials=True,
    allow_methods=["*"],  # Consenti tutti i metodi HTTP
    allow_headers=["*"],  # Consenti tutte le intestazioni
)

@app.get("/company/{ticker}")
async def get_company_data(ticker: str):
    company_data = fetch_company_data(ticker)
    if company_data:
        return company_data
    else:
        return {"error": "Impossibile recuperare i dati per il ticker fornito"}
