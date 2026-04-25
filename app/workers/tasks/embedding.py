from app.workers.celery_app import celery_app


@celery_app.task(name="embedding.create")
def create_embedding(message_id: int) -> dict[str, int]:
    return {"message_id": message_id}
