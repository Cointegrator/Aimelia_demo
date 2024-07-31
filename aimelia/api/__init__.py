from fastapi import APIRouter
from .data import router as data_router
from .inference import router as inference_router

router = APIRouter(prefix="/api")

router.include_router(data_router)
router.include_router(inference_router)
