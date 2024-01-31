from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.requests import Request
from routers.users import app as users
from db.database import create_database
# from routers.auth import app as authentication
from fastapi.middleware.cors import CORSMiddleware
from decouple import config

#initialize fastapi
app = FastAPI()

create_database()

#add middlewares
app.add_middleware(
    CORSMiddleware,
    allow_origins=["localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

app.include_router(users)
# app.include_router(authentication)

@app.get("/", name="home")
async def get_root(request: Request) -> dict:
    #return RedirectResponse(url="/docs/")
    return {
        "message": "Welcome, please go to /docs",
    }

