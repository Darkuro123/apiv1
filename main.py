from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel
from auth import createToken, validateToken
from bd.database import engine, Base
from routers.movie import routerMovie
from routers.users import login_user
import os
import uvicorn

app = FastAPI(
    title='Aprendiendo FastApi',
    description='Aprendiendo FastApi con Python',
    version='0.0.1',

)

app.include_router(routerMovie)
app.include_router(login_user)

Base.metadata.create_all(bind=engine)


@app.get('/', tags=["Inicio"])
def read_root():
    return HTMLResponse('<h1>Bienvenido a FastAPI</h1>')


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host='0.0.0.0', port=port)
