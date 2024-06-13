from nodes.inference.router import router as inference_router
from fastapi import FastAPI

app = FastAPI()
app.include_router(inference_router)
