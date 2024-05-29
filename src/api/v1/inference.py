from fastapi import APIRouter

router = APIRouter(prefix='/inference', tags=['Inference Node'])

@router.get('/media')
async def get_media():
    pass
