from pydantic import BaseModel

class VideojuegoBase(BaseModel):
    titulo: str
    genero: str
    plataforma: str
    precio: float

class VideojuegoCreate(VideojuegoBase):
    pass

class VideojuegoResponse(VideojuegoBase):
    id: int

    class Config:
        from_attributes = True