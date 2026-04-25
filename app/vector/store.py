class VectorStore:
    async def upsert(self, message_id: int, vector: list[float]) -> None:
        print({"message_id": message_id, "dimensions": len(vector)})
