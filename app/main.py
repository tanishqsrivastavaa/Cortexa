from fastapi import FastAPI

from app.api.routes import insights, query, summarize
from app.config.settings import get_settings
from app.core.logging import configure_logging


settings = get_settings()
configure_logging(settings.log_level)

app = FastAPI(title=settings.app_name)

app.include_router(query.router, prefix="/query", tags=["query"])
app.include_router(summarize.router, prefix="/summarize", tags=["summarize"])
app.include_router(insights.router, prefix="/insights", tags=["insights"])


@app.get("/health")
async def health_check() -> dict[str, str]:
    return {"status": "ok"}
