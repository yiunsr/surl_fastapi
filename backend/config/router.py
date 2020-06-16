from fastapi import APIRouter
from app.api.__init___ import apiRouter

router = APIRouter()

def init_router(app):
    app.include_router(apiRouter, prefix="/api")
