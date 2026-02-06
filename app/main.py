{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 from fastapi import FastAPI, Depends\
from sqlalchemy.orm import Session\
\
from .database import SessionLocal, engine\
from . import models, schemas, crud\
\
models.Base.metadata.create_all(bind=engine)\
\
app = FastAPI(title="Expense Tracker API")\
\
def get_db():\
    db = SessionLocal()\
    try:\
        yield db\
    finally:\
        db.close()\
\
@app.post("/expenses", response_model=schemas.ExpenseResponse)\
def create_expense(\
    expense: schemas.ExpenseCreate,\
    db: Session = Depends(get_db)\
):\
    return crud.create_expense(db, expense)\
\
@app.get("/expenses", response_model=list[schemas.ExpenseResponse])\
def list_expenses(\
    category: str | None = None,\
    sort: str | None = None,\
    db: Session = Depends(get_db)\
):\
    return crud.get_expenses(db, category, sort)\
}