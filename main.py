#!/usr/bin/python3

from fastapi import FastAPI

app =FastAPI()

app.get("/")
async def root():
    return {"Running..."}