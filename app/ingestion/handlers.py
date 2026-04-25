from datetime import UTC, datetime
from typing import Any


def format_message(message: Any) -> dict[str, str | None]:
    return {
        "event_type": "message_create",
        "message_id": str(message.id),
        "server_id": str(message.guild.id) if message.guild else None,
        "channel_id": str(message.channel.id),
        "user_id": str(message.author.id),
        "username": str(message.author),
        "content": str(message.content),
        "timestamp": datetime.now(UTC).isoformat(),
    }
