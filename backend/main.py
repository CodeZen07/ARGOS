from fastapi import FastAPI
from database import engine
from models import Base, Licitacion
from scraping import scrape_portal

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API ARGOS funcionando 🚀"}

@app.get("/licitaciones")
def get_licitaciones():
    from database import SessionLocal
    db = SessionLocal()
    data = db.query(Licitacion).all()
    db.close()
    return data

@app.post("/actualizar")
def actualizar():
    scrape_portal()
    return {"message": "Datos actualizados"}

