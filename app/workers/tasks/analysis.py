from app.workers.celery_app import celery_app


@celery_app.task(name="analysis.run")
def run_analysis(message_id: int) -> dict[str, int]:
    return {"message_id": message_id}
