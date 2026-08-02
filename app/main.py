import os
from fastapi import FastAPI
from sqlalchemy import create_engine, text

app = FastAPI()

DATABASE_URL = os.environ.get("DATABASE_URL")
engine = create_engine(DATABASE_URL)

@app.get("/")
def read_root():
    return {"message": "Two-tier app is alive"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/db-check")
def db_check():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT version();"))
        version = result.scalar()
    return {"database_connected": True, "postgres_version": version}