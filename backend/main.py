
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware import Middleware
from fastapi.staticfiles import StaticFiles

from .http import http
from .api import api

middleware = [Middleware(
    CORSMiddleware, 
    allow_origins=['*'], 
    allow_credentials=True, 
    allow_methods=['*'], 
    allow_headers=['*']
    )]

app = FastAPI(middleware=middleware)

app.include_router(http)
app.include_router(api)

app.mount(
    "/static",
    StaticFiles(directory="web/static"),
    name="static"
    )