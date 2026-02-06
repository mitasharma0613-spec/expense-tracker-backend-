{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 from datetime import date, datetime\
from decimal import Decimal\
from pydantic import BaseModel, Field\
\
class ExpenseCreate(BaseModel):\
    amount: Decimal = Field(gt=0)\
    category: str\
    description: str | None = None\
    date: date\
    request_id: str\
\
class ExpenseResponse(BaseModel):\
    id: str\
    amount: Decimal\
    category: str\
    description: str | None\
    date: date\
    created_at: datetime\
\
    class Config:\
        from_attributes = True\
}