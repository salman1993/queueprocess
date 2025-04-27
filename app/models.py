from sqlalchemy import Column, Integer, String
from .db import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    status = Column(String, default="queued")  # queued, processing, done
    result = Column(String, nullable=True)
