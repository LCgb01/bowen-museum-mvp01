from sqlalchemy import Column, Integer, String, Text, TIMESTAMP
from sqlalchemy.sql import func
from backend.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    openid = Column(String(128), unique=True, index=True, nullable=False)
    nickname = Column(String(64))
    avatar_url = Column(Text)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    last_login_at = Column(TIMESTAMP(timezone=True))

    def __repr__(self):
        return f"<User(id={self.id}, nickname='{self.nickname}')>"
