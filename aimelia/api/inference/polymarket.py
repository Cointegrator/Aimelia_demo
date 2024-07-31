from fastapi import APIRouter
from typing import List, Any, Optional
from services.inference.polymarket import PolymarketInferenceService

router = APIRouter(prefix="/polymarket", tags=["Polymarket"])

from pydantic import BaseModel


class InferenceRequest(BaseModel):
    event_id: str
    question: str
    force: Optional[bool] = False


@router.post("/infer")
def infer_polymarket_event_by_id(body: InferenceRequest):
    service = PolymarketInferenceService()
    result = service.get_inference(body.event_id, body.question, force=body.force)
    return result
