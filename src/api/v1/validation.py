from fastapi import APIRouter, status

router = APIRouter(prefix="/validation", tags=["Validation Node"])


@router.get("/{condition_id}/validate")
async def validate_event_by_condition_id():
    """
    **Currently not implemented.**

    This endpoints sole responsiblity is to use the inference and data node
    and the backend AI engine to automatically set or help the user
    come to a conclusion for the event.
    """
    return {
        "status": status.HTTP_501_NOT_IMPLEMENTED,
        "message": "Will be implemented shortly",
    }
