from nodes.inference.router import router as inference_router
from utils.utility import get_custom_openapi

from fastapi import FastAPI

app = FastAPI()
app.include_router(inference_router)
app.openapi_schema = get_custom_openapi("inference", app)
