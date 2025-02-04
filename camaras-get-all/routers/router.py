from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.db import get_db
from models.models import DCamara

router = APIRouter()

@router.get("/camaras")
async def get_all_camaras(db: AsyncSession = Depends(get_db)):
    """
    Obtiene todas las cámaras de la tabla `usr_p360.d_camara`.
    """
    try:
        result = await db.execute(select(DCamara))
        camaras = result.scalars().all()
        
        return [{"d_camara_id": c.d_camara_id, 
                 "marca": c.marca, 
                 "modelo": c.modelo,
                 "tipo": c.tipo,
                 "latitud": c.latitud,
                 "longitud": c.longitud,
                 "fecha_alta": c.fecha_alta,
                 "fecha_modificacion": c.fecha_modificacion} for c in camaras]
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
