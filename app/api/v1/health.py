from fastapi import APIRouter

router = APIRouter()


@router.get("/ping", tags=["Health"])
def ping():
    return {"pong": True}
