from fastapi import APIRouter

router = APIRouter(prefix="/predx", tags=["PredX"])


@router.get("/events")
def get_all_predx_events():
    raise NotImplementedError()
