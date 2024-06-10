from fastapi import APIRouter

# API Routers
from .data import router as data_router
from .inference import router as inference_router
from .validation import router as validation_router
from .task import router as task_router

router = APIRouter(prefix="/v1")

router.include_router(data_router)
router.include_router(inference_router)
# router.include_router(validation_router)
# router.include_router(task_router)
