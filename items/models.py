from sqlalchemy import Column, Integer, String, Boolean

from layers.models import Base


class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    is_storable = Column(Boolean, default=True)

    def __repr__(self):
        return f"<Item(name={self.name}, is_storable={self.is_storable})>"
