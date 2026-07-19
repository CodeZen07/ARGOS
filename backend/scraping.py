import requests
from bs4 import BeautifulSoup
from datetime import datetime
from database import SessionLocal
from models import Licitacion

def scrape_portal():
    url = "https://portalcompras.gob.do/licitaciones"  # ajustar al real
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    db = SessionLocal()

    for item in soup.select(".licitacion-item"):  # ajustar al selector real
        titulo = item.select_one(".titulo").text.strip()
        entidad = item.select_one(".entidad").text.strip()
        monto = float(item.select_one(".monto").text.replace(",", "").strip())
        rubro = item.select_one(".rubro").text.strip()
        fecha = datetime.now()  # aquí deberías parsear la fecha real
        enlace = item.select_one("a")["href"]

        lic = Licitacion(
            titulo=titulo,
            entidad=entidad,
            monto=monto,
            rubro=rubro,
            fecha_publicacion=fecha,
            enlace=enlace
        )
        db.add(lic)

    db.commit()
    db.close()

