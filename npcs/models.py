from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey

from database import Base


class NPC(Base):
    __tablename__ = 'npcs'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    gender = Column(String)

    strength = Column(Integer, default=0)
    perception = Column(Integer, default=0)
    agility = Column(Integer, default=0)
    research = Column(Integer, default=0)
    charisma = Column(Integer, default=0)
    luck = Column(Integer, default=0)

    health = Column(Integer, default=100)
    level = Column(Integer, default=1)
    npc_class = Column(String)

    inventory_weight = Column(Float, default=0.0)
    inventory_count = Column(Integer, default=0)

    hero_reputation = Column(Integer, default=0)

    possible_drop = Column(String)

    def __repr__(self):
        return (f"<NPC(name={self.name}, gender={self.gender}, level={self.level}, "
                f"health={self.health}, npc_class={self.npc_class}, "
                f"reputation={self.hero_reputation})>")

    def take_damage(self, amount: int):
        """Уменьшить здоровье на определенное значение."""
        self.health -= amount
        if self.health <= 0:
            self.health = 0
            print(f"{self.name} был побежден.")

    def check_research(self, trick_difficulty: int) -> bool:
        """Проверка способности NPC раскрыть хитрость героя."""
        return self.research >= trick_difficulty
