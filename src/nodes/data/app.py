from nodes.data.router import router as data_router
from utils.utility import get_custom_openapi

from fastapi import FastAPI

app = FastAPI()
app.include_router(data_router)
app.openapi_schema = get_custom_openapi("data", app)
