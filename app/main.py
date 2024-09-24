from fastapi import FastAPI

from .routers import users

app = FastAPI()

app.include_router(users.router, prefix="/users")

@app.get("/")
async def root():
    return {"message": "Hello From Structured API"}