from sqlalchemy.orm import Session
import models, schemas

# CREATE
def crear_videojuego(db: Session, videojuego: schemas.VideojuegoCreate):
    nuevo = models.Videojuego(**videojuego.model_dump())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

# READ ALL
def obtener_videojuegos(db: Session):
    return db.query(models.Videojuego).all()

# READ ONE
def obtener_videojuego(db: Session, id: int):
    return db.query(models.Videojuego).filter(models.Videojuego.id == id).first()

# UPDATE
def actualizar_videojuego(db: Session, id: int, datos: schemas.VideojuegoCreate):
    juego = db.query(models.Videojuego).filter(models.Videojuego.id == id).first()
    if juego:
        for key, value in datos.model_dump().items():
            setattr(juego, key, value)
        db.commit()
        db.refresh(juego)
    return juego

# DELETE
def eliminar_videojuego(db: Session, id: int):
    juego = db.query(models.Videojuego).filter(models.Videojuego.id == id).first()
    if juego:
        db.delete(juego)
        db.commit()
    return juego