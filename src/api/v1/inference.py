from fastapi import APIRouter

from src.nodes.data import DataNode

router = APIRouter(prefix='/inference', tags=['Inference Node'])

@router.get('/{condition_id}')
async def draw_inference(condition_id: str):
    news = DataNode().get_relevant_news(condition_id)
    event = DataNode().get_event_by_condition_id(condition_id)
    return {'news': news, 'event': event}
