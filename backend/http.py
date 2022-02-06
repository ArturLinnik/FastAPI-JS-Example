from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

import requests
from typing import Optional

from .schemas import User

http = APIRouter()

templates = Jinja2Templates(directory="web/templates")

@http.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@http.get("/login")
async def login(request: Request):

    return templates.TemplateResponse("login.html", {"request": request}) 



@http.post("/login")
async def prueba(request: Request, username: str = Form(...), password: str = Form(...)):

    return templates.TemplateResponse("login.html", {"request": request, "username": username}) 