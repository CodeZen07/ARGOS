import requests

def run_update():
    # URL pública de tu API en Render
    url = "https://argos-91ks.onrender.com/actualizar"
    
    # Hacemos la petición POST al endpoint /actualizar
    response = requests.post(url)
    
    # Mostramos el resultado en la consola de Render
    print("Actualización ejecutada:", response.status_code, response.text)

if __name__ == "__main__":
    run_update()
