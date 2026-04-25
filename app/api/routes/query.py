from fastapi import APIRouter

from app.schemas.query import QueryRequest
from app.schemas.response import QueryResponse
from app.services.retrieval_service import RetrievalService


router = APIRouter()


@router.post("/", response_model=QueryResponse)
async def query_memory(payload: QueryRequest) -> QueryResponse:
    service = RetrievalService()
    results = await service.query(payload.query, limit=payload.limit)
    return QueryResponse(query=payload.query, results=results)
