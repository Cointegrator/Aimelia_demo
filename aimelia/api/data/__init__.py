from fastapi import APIRouter
from .polymarket import router as polymarket_router
from .predx import router as predx_router

router = APIRouter(prefix="/data", tags=["Data"])

router.include_router(polymarket_router)
router.include_router(predx_router)
