from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Hero(Base):
    __tablename__ = 'heroes'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    level = Column(Integer, default=1)
    player_id = Column(Integer, ForeignKey('players.id'))
