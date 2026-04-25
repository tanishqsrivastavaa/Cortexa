from sqlalchemy import ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Embedding(Base):
    __tablename__ = "embeddings"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    message_id: Mapped[int] = mapped_column(ForeignKey("messages.id"), unique=True, index=True)
    model: Mapped[str] = mapped_column(Text)
    vector: Mapped[str] = mapped_column(Text)

    message: Mapped["Message"] = relationship(back_populates="embedding")
