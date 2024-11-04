from sqlalchemy import Column, Integer, String, Float, Boolean, Enum, ForeignKey
from sqlalchemy.orm import relationship
from enum import Enum as PyEnum

from database import Base


# Определяем ветви магии
class MagicBranch(PyEnum):
    OFFENSIVE = "offensive"  # Атакующая магия
    HEALING = "healing"  # Исцеляющая магия
    CREATIVE = "creative"  # Создающая магия


class BaseSpell(Base):
    __tablename__ = 'spells'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    branch = Column(Enum(MagicBranch), nullable=False)  # Ветка магии
    mana_cost = Column(Float, default=10.0)
    level = Column(Integer, default=1)
    cooldown = Column(Float, default=5.0)  # время отката в секундах
    is_area_effect = Column(Boolean, default=False)  # массовое заклинание или нет

    def __call__(self, caster, target):
        """Метод для применения заклинания."""
        if not self._can_cast(caster):
            print(f"{caster.name} не может использовать {self.name}. Недостаточно маны.")
            return
        self.cast(caster, target)

    def _can_cast(self, caster):
        """Проверка, достаточно ли маны и прошло ли время отката."""
        return caster.mana >= self.mana_cost

    def cast(self, caster, target):
        """Метод применения заклинания, переопределяется в дочерних классах."""
        raise NotImplementedError("Метод cast() должен быть реализован в дочерних классах.")

    def upgrade(self):
        """Метод для прокачки заклинания, может быть переопределён в дочерних классах."""
        self.level += 1
        self.mana_cost *= 1.1  # Пример увеличения стоимости маны с уровнем

    def __repr__(self):
        return (f"<Spell(name={self.name}, branch={self.branch}, level={self.level}, "
                f"mana_cost={self.mana_cost})>")


class Fireball(BaseSpell):
    __tablename__ = 'fireballs'

    id = Column(Integer, ForeignKey('spells.id'), primary_key=True)
    base_damage = Column(Integer, default=20)

    def __init__(self, base_damage=20):
        super().__init__()
        self.base_damage = base_damage
        self.branch = "OFFENSIVE"

    def __call__(self, target):
        """Использовать заклинание на цели"""
        damage = self.calculate_damage()
        target.take_damage(damage)
        return f"{self.name} наносит {damage} урона цели {target.name}."

    def calculate_damage(self):
        # Пример вычисления урона, где используется уровень и базовый урон
        return self.base_damage + (self.level * 2)
