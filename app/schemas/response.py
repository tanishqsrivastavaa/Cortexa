from pydantic import BaseModel


class QueryResponse(BaseModel):
    query: str
    results: list[dict[str, str]]


class SummaryResponse(BaseModel):
    summary: str


class InsightResponse(BaseModel):
    insights: list[dict[str, str]]
