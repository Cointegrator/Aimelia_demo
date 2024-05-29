from fastapi import APIRouter

router = APIRouter(prefix='/validation', tags=['Validation Node'])

@router.get('/')
async def test():
    return {'data': 'data'}
