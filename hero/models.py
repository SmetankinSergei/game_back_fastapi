from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Hero(Base):
    __tablename__ = 'heroes'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    level = Column(Integer, default=1)
    experience = Column(Integer, default=0)
    health = Column(Integer)

    strength = Column(Integer)
    perception = Column(Integer)
    agility = Column(Integer)
    research = Column(Integer)
    charisma = Column(Integer)
    lucky = Column(Integer)

    user_id = Column(Integer, ForeignKey('players.id'))
