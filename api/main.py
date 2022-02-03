
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware import Middleware
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from pydantic import BaseModel


class User(BaseModel):
    username: str
    password: str


middleware = [Middleware(
    CORSMiddleware, 
    allow_origins=['*'], 
    allow_credentials=True, 
    allow_methods=['*'], 
    allow_headers=['*']
    )]


app = FastAPI(middleware=middleware)


@app.post("/login")
async def users(user: User):

    if user.username == "artur" and user.password == "pokemon":
        msg = jsonable_encoder({"success": True})
        return JSONResponse(msg)

    else:
        msg = jsonable_encoder({"success": False})
        return JSONResponse(msg)