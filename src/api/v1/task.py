from pydantic import BaseModel
from fastapi import APIRouter, status
from typing import List, Dict, Optional

router = APIRouter(prefix="/task", tags=["Task Node"])


class EventRequest(BaseModel):
    question: str
    description: str
    categories: Dict[str, List[str]]
    initial_yes_price: Optional[float] = 50
    initial_no_price: Optional[float] = 50


@router.post("/")
async def create_new_event(event: EventRequest):
    """
    Currently not implemented.
    This endpoint will be used to create a new event in the system.
    """
    _ = event
    return {
        "status": status.HTTP_501_NOT_IMPLEMENTED,
        "message": "Will be implemented shortly",
    }
