"""Main module for the FastAPI application."""

from typing import Dict

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root() -> Dict[str, str]:
    return {"message": "Hello coders!"}
