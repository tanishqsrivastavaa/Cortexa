class MemoryService:
    async def store(self, content: str) -> None:
        print({"content": content})
