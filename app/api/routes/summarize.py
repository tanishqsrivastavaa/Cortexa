from fastapi import APIRouter

from app.schemas.response import SummaryResponse


router = APIRouter()


@router.post("/", response_model=SummaryResponse)
async def summarize() -> SummaryResponse:
    return SummaryResponse(summary="Summarization service is not implemented yet.")
