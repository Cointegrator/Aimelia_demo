from fastapi import APIRouter, FastAPI
from service import DataNode

router = APIRouter(prefix="/data", tags=["Data Node"])


@router.get("/event")
async def get_all_events_data():
    """
    Get all ongoing markets data. (Paginated)
    """
    r = DataNode().get_all_events_data()
    return r


@router.get("/event/{condition_id}")
async def get_event_by_condition_id(condition_id: str):
    """
    Get market details by the market's condition-id.
    """
    r = DataNode().get_event_by_condition_id(condition_id)
    return r


@router.get("/event/{condition_id}/news")
async def get_relevant_news(condition_id: str):
    """
    Get relevant news for the market.
    """
    r = DataNode().get_relevant_news(condition_id)
    return r


app = FastAPI()
app.include_router(router)
