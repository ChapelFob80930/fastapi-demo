from fastapi import FastAPI
# from fastapi.params import Body

# from random import randrange
# import psycopg2
# from psycopg2.extras import RealDictCursor 
# import time
from . import models
from .database import engine
from . routers import post, user, auth, vote
from .config import settings
from fastapi.middleware.cors import CORSMiddleware

# models.Base.metadata.create_all(bind=engine) 
# makes SQLAlchemy create tables but now alembic will handle migrations, so we don't need to create tables here

app = FastAPI()

origins = ["*"] # list of origins that are allowed to make requests to the API
# This can be set to specific domains like ["https://example.com", "http://localhost:3000"] for security
# or can be set to ["*"] to allow all origins (not recommended for production)

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins, # allows requests from these origins
    allow_credentials = True, # allows cookies to be sent with requests
    allow_methods = ["*"], # allows all methods (GET, POST, PUT, DELETE, etc.)
    allow_headers = ["*"], # allows all headers
)

app.include_router(post.router)

app.include_router(user.router)

app.include_router(auth.router)

app. include_router(vote.router)

@app.get("/")
async def root():
    return {"message": "Hello World!"}


