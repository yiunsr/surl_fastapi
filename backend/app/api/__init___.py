from fastapi import APIRouter
from .users import router as user_router
from .items import router as items_router

apiRouter = APIRouter()

apiRouter.include_router(user_router, prefix="/users")
apiRouter.include_router(items_router, prefix="/items")
