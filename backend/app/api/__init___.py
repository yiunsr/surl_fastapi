from fastapi import APIRouter
from .users import router as user_router
from .items import router as items_router
from .auths import router as auths_router

apiRouter = APIRouter()

apiRouter.include_router(user_router, prefix="/users")
apiRouter.include_router(items_router, prefix="/items")
apiRouter.include_router(auths_router, prefix="/auths")
