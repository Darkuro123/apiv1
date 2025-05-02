from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel
from auth import createToken, validateToken
from bd.database import engine, Base
from routers.movie import routerMovie
from routers.users import login_user

app = FastAPI(
    title='Aprendiendo FastApi',
    description='Aprendiendo FastApi con Python',
    version='0.0.1',

)

app.include_router(routerMovie)
app.include_router(login_user)

Base.metadata.create_all(bind=engine)


moviess = [
    {
        "id": 3,
        "title": "The Shawshank Redemption",
        "overview": "Two imprisoned men bond over a number of years ...",
        "year": 1994,
        "rating": 9.3,
        "category": "Drama"

    },
    {
        "id": 3,
        "title": "The Godfather",
        "overview": "An organized crime dynastys aging patriarch ...",
        "year": 1972,
        "rating": 9.2,
        "category": "Drama"
    },
    {
        "id": 3,
        "title": "The Dark Knight",
        'overview': 'When the menace known as the Joker emerges ...',
        "year": 2008,
        "rating": 9.0,
        "category": "Action",
    }
]
