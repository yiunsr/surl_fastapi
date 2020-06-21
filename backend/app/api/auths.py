from fastapi import APIRouter
from fastapi import HTTPException

router = APIRouter()


@router.post("/", tags=["auths"])
async def signup():
    return
