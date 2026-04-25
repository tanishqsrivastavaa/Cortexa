from app.workers.celery_app import celery_app


@celery_app.task(name="summarization.create")
def create_summary(message_id: int) -> dict[str, int]:
    return {"message_id": message_id}
