from sqlalchemy import Column, Integer, String, Text, TIMESTAMP
from sqlalchemy.dialects.postgresql import ARRAY, JSONB
from sqlalchemy.sql import func
from backend.database import Base

class Artifact(Base):
    __tablename__ = "artifacts"

    id = Column(Integer, primary_key=True, index=True)
    artifact_id = Column(String(20), unique=True, index=True, nullable=False)
    name = Column(String(200), nullable=False)
    era = Column(String(100))
    museum = Column(String(200))
    images = Column(ARRAY(Text))
    summary = Column(Text)
    standard = Column(Text)
    deep = Column(Text)
    stories = Column(JSONB)
    keywords = Column(ARRAY(String(100)))
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())

    def __repr__(self):
        return f"<Artifact(id={self.id}, name='{self.name}')>"
