from fastapi import APIRouter

router = APIRouter(prefix='/task', tags=['Task Node'])

@router.get('/')
async def test():
    return {'data': 'data'}
