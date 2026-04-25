from app.schemas.message import MessageEvent


class IngestionService:
    async def ingest_message(self, event: MessageEvent) -> None:
        # Persisting and queueing will be added once the database and workers are wired.
        print(event.model_dump())
