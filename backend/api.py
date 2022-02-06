from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from .schemas import User

api = APIRouter(prefix="/api/v1")

@api.post("/login")
async def users(user: User):

    print("Received on API")

    if user.username == "artur" and user.password == "pokemon":
        msg = jsonable_encoder({"success": True, "user": user})
        return JSONResponse(msg)

    else:
        msg = jsonable_encoder({"success": False, "user": user})
        return JSONResponse(msg)