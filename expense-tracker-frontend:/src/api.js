{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 const API_BASE = "http://127.0.0.1:8000";\
\
export async function fetchExpenses(category, sort) \{\
  const params = new URLSearchParams();\
  if (category) params.append("category", category);\
  if (sort) params.append("sort", sort);\
\
  const res = await fetch(`$\{API_BASE\}/expenses?$\{params.toString()\}`);\
  return res.json();\
\}\
\
export async function createExpense(payload) \{\
  const res = await fetch(`$\{API_BASE\}/expenses`, \{\
    method: "POST",\
    headers: \{ "Content-Type": "application/json" \},\
    body: JSON.stringify(payload),\
  \});\
\
  if (!res.ok) \{\
    throw new Error("Failed to create expense");\
  \}\
\
  return res.json();\
\}\
}