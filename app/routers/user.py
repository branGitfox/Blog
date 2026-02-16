from fastapi import APIRouter


router  =  APIRouter(prefix="/user", tags=["users"])


@router.post('/')
def create():
    return {'message': "hello world"}