from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

app = FastAPI(
    title="Alchemy API",
    description="This is a sample API for managing Alchemy entities, used to demonstrate a platform project. It allows you to create, read, update, and delete Alchemy records.",
    version="1.0.0"
)

class Alchemy(Base):
    __tablename__ = "alchemy"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)

class AlchemyCreate(BaseModel):
    name: str
    description: str

class AlchemyUpdate(BaseModel):
    name: str
    description: str

# Ensure the table schema is created in the database
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/alchemy/", response_model=dict, tags=["Alchemy"])
def create_alchemy(alchemy: AlchemyCreate, db: Session = Depends(get_db)):
    db_alchemy = Alchemy(name=alchemy.name, description=alchemy.description)
    db.add(db_alchemy)
    db.commit()
    db.refresh(db_alchemy)
    return {"id": db_alchemy.id, "name": db_alchemy.name, "description": db_alchemy.description}

@app.get("/alchemy/{alchemy_id}", response_model=AlchemyCreate, tags=["Alchemy"])
def read_alchemy(alchemy_id: int, db: Session = Depends(get_db)):
    db_alchemy = db.query(Alchemy).filter(Alchemy.id == alchemy_id).first()
    if db_alchemy is None:
        raise HTTPException(status_code=404, detail="Alchemy not found")
    return db_alchemy

@app.put("/alchemy/{alchemy_id}", response_model=dict, tags=["Alchemy"])
def update_alchemy(alchemy_id: int, alchemy: AlchemyUpdate, db: Session = Depends(get_db)):
    db_alchemy = db.query(Alchemy).filter(Alchemy.id == alchemy_id).first()
    if db_alchemy is None:
        raise HTTPException(status_code=404, detail="Alchemy not found")
    db_alchemy.name = alchemy.name
    db_alchemy.description = alchemy.description
    db.commit()
    db.refresh(db_alchemy)
    return {"id": db_alchemy.id, "name": db_alchemy.name, "description": db_alchemy.description}

@app.delete("/alchemy/{alchemy_id}", response_model=AlchemyCreate, tags=["Alchemy"])
def delete_alchemy(alchemy_id: int, db: Session = Depends(get_db)):
    db_alchemy = db.query(Alchemy).filter(Alchemy.id == alchemy_id).first()
    if db_alchemy is None:
        raise HTTPException(status_code=404, detail="Alchemy not found")
    db.delete(db_alchemy)
    db.commit()
    return db_alchemy
