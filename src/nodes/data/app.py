from nodes.data.router import router as data_router
from fastapi import FastAPI

app = FastAPI()
app.include_router(data_router)
