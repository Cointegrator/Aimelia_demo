from fastapi import APIRouter

router = APIRouter(prefix="/predx", tags=["PredX"])


@router.post("/infer/{event_id}")
def infer_predx_event_by_id(event_id: str):
    raise NotImplementedError()
