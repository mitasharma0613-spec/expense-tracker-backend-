{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import uuid\
from sqlalchemy import Column, String, Date, DateTime, Numeric\
from sqlalchemy.sql import func\
from .database import Base\
\
class Expense(Base):\
    __tablename__ = "expenses"\
\
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))\
    request_id = Column(String, unique=True, nullable=False)\
\
    amount = Column(Numeric(10, 2), nullable=False)\
    category = Column(String, nullable=False)\
    description = Column(String, nullable=True)\
    date = Column(Date, nullable=False)\
\
    created_at = Column(DateTime(timezone=True), server_default=func.now())\
}