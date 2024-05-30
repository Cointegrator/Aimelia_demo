from fastapi import APIRouter

from src.nodes.inference import InferenceNode

router = APIRouter(prefix='/inference', tags=['Inference Node'])

@router.get('/{condition_id}')
async def get_info(condition_id: str):
    return InferenceNode().get_info(condition_id=condition_id)


@router.get('/{condition_id}/infer')
async def infer_and_participate(condition_id: str):
    """
    Helps draw inference from the gathered knowledge
    """
    return InferenceNode().infer_and_participate(condition_id=condition_id)
