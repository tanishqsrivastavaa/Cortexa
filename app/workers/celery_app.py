from celery import Celery

from app.config.settings import get_settings


settings = get_settings()

celery_app = Celery(
    "cortexa",
    broker=settings.celery_broker_url,
    backend=settings.celery_result_backend,
    include=[
        "app.workers.tasks.embedding",
        "app.workers.tasks.summarization",
        "app.workers.tasks.analysis",
    ],
)
