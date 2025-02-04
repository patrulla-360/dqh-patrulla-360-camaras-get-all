from fastapi import FastAPI
from routers import router as camara_router
from models.db import engine
from sqlalchemy.sql import text

app = FastAPI(title="Cámaras API")

# Registrar las rutas de cámaras
app.include_router(camara_router, prefix="/api", tags=["camaras"])

@app.on_event("startup")
async def startup():
    """
    Verifica la conexión a la base de datos al iniciar.
    """
    async with engine.begin() as conn:
        await conn.execute(text("SELECT 1"))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main_d_camara:app", host="0.0.0.0", port=8000, reload=True)
