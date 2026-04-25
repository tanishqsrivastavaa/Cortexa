from typing import Any


class EventPublisher:
    """Placeholder publisher; wire this to Redis when queueing is introduced."""

    async def publish(self, event: dict[str, Any]) -> None:
        print(event)
