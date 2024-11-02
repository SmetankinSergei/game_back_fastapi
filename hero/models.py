from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Hero(Base):
    __tablename__ = 'heroes'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    level = Column(Integer, default=1)
    experience = Column(Integer, default=0)
    health = Column(Integer)
    inventory_capacity = Column(Integer, default=20)
    inventory_weight_capacity = Column(Float, default=50.0)

    strength = Column(Integer)
    perception = Column(Integer)
    agility = Column(Integer)
    research = Column(Integer)
    charisma = Column(Integer)
    lucky = Column(Integer)

    user_id = Column(Integer, ForeignKey('users_user.id'))
    inventory_items = relationship('InventoryItem', back_populates='hero')


class InventoryItem(Base):
    __tablename__ = 'inventory_items'

    id = Column(Integer, primary_key=True, index=True)
    hero_id = Column(Integer, ForeignKey('heroes.id'))
    item_name = Column(String, index=True)
    quantity = Column(Integer, default=1)

    hero = relationship('Hero', back_populates='inventory_items')
