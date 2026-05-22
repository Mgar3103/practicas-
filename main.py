from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, crud, schemas
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Videojuegos")

@app.post("/videojuegos/", response_model=schemas.VideojuegoResponse)
def crear(videojuego: schemas.VideojuegoCreate, db: Session = Depends(get_db)):
    return crud.crear_videojuego(db, videojuego)

@app.get("/videojuegos/", response_model=list[schemas.VideojuegoResponse])
def listar(db: Session = Depends(get_db)):
    return crud.obtener_videojuegos(db)

@app.get("/videojuegos/{id}", response_model=schemas.VideojuegoResponse)
def obtener(id: int, db: Session = Depends(get_db)):
    juego = crud.obtener_videojuego(db, id)
    if not juego:
        raise HTTPException(status_code=404, detail="Videojuego no encontrado")
    return juego

@app.put("/videojuegos/{id}", response_model=schemas.VideojuegoResponse)
def actualizar(id: int, videojuego: schemas.VideojuegoCreate, db: Session = Depends(get_db)):
    juego = crud.actualizar_videojuego(db, id, videojuego)
    if not juego:
        raise HTTPException(status_code=404, detail="Videojuego no encontrado")
    return juego

@app.delete("/videojuegos/{id}")
def eliminar(id: int, db: Session = Depends(get_db)):
    juego = crud.eliminar_videojuego(db, id)
    if not juego:
        raise HTTPException(status_code=404, detail="Videojuego no encontrado")
    return {"mensaje": "Videojuego eliminado correctamente"}