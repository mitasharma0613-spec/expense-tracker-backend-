{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 from sqlalchemy.orm import Session\
from . import models, schemas\
\
def create_expense(db: Session, expense: schemas.ExpenseCreate):\
    # Idempotency check\
    existing = (\
        db.query(models.Expense)\
        .filter(models.Expense.request_id == expense.request_id)\
        .first()\
    )\
\
    if existing:\
        return existing\
\
    new_expense = models.Expense(\
        amount=expense.amount,\
        category=expense.category,\
        description=expense.description,\
        date=expense.date,\
        request_id=expense.request_id,\
    )\
\
    db.add(new_expense)\
    db.commit()\
    db.refresh(new_expense)\
    return new_expense\
\
\
def get_expenses(db: Session, category: str | None, sort: str | None):\
    query = db.query(models.Expense)\
\
    if category:\
        query = query.filter(models.Expense.category == category)\
\
    if sort == "date_desc":\
        query = query.order_by(models.Expense.date.desc())\
\
    return query.all()\
}