from fastapi import APIRouter

router = APIRouter()

@router.get("/", tags=["users"])
async def read_users():
    return [
        {"id":1, "username": "김영일"},
        {"id":2, "username": "안성민"},
        {"id":3, "username": "최지후"}
    ]


@router.get("/me", tags=["users"])
async def read_user_me():
    return {"username": "안성민"}


@router.get("/{username}", tags=["users"])
async def read_user(username: str):
    return {"username": username}
