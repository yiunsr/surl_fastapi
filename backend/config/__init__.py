import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .env_config import app_config_map
from .db import init_db
from .router import init_router

_SERVER_TYPE = os.getenv('SERVER_TYPE') or 'development'
AppConfig = app_config_map[_SERVER_TYPE]

SessionLocal, Base = init_db(AppConfig)


def create_app():
    origins = [
        "http://localhost",
        "http://localhost:5000",
        "http://localhost:8000",
    ]

    app = FastAPI(title="SURL")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    AppConfig.init_app(app)
    init_router(app)
    return app
