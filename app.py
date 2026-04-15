from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
import os

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")

def serve(filename):
    ruta = os.path.join(BASE_DIR, "templates", filename)
    with open(ruta, "r", encoding="utf-8") as f:
        return HTMLResponse(content=f.read(), status_code=200)

@app.get("/", response_class=HTMLResponse)
async def home():
    return serve("home.html")

@app.get("/camaras", response_class=HTMLResponse)
async def camaras():
    return serve("camaras.html")

@app.get("/camaras-index", response_class=HTMLResponse)
async def camaras_index():
    return serve("camaras_index.html")

@app.get("/deportivo", response_class=HTMLResponse)
async def deportivo():
    return serve("deportivo.html")

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8001)