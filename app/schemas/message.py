from datetime import datetime

from pydantic import BaseModel


class MessageEvent(BaseModel):
    event_type: str
    message_id: str
    server_id: str | None = None
    channel_id: str
    user_id: str
    username: str
    content: str
    timestamp: datetime
