from fastapi import APIRouter

from app.schemas.response import InsightResponse


router = APIRouter()


@router.get("/", response_model=InsightResponse)
async def insights() -> InsightResponse:
    return InsightResponse(insights=[])
