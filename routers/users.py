from routers.movie import routerMovie
from pydantic import BaseModel
from fastapi.responses import HTMLResponse, JSONResponse
from auth import createToken, validateToken
from fastapi import APIRouter


login_user = APIRouter()


class User(BaseModel):
    email: str
    password: str


@login_user.post('/login', tags=['authentication'])
def login(user: User):
    if user.email == 'briandevital@gmail.com' and user.password == '123':

        token: str = createToken(user.model_dump())
        print(token)
    return JSONResponse(content=token)
