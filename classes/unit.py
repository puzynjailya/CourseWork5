from __future__ import annotations
from abc import ABC, abstractmethod
import random

from classes.equipment import Weapon, Armor
from typing import Optional


class BaseUnit(ABC):
    """
    Базовый класс юнита
    """

    def __init__(self, name: str, unit_class: UnitClass):
        """
        При инициализации класса Unit используем свойства класса UnitClass
        """
        self.name = name
        self.unit_class = unit_class
        self.hp = unit_class.max_health
        self.stamina = unit_class.max_stamina
        self.weapon = None
        self.armor = None
        self._is_skill_used = False

    @property
    def health_points(self):
        return round(self.hp, 2)

    @property
    def stamina_points(self):
        return round(self.stamina, 2)

    def equip_weapon(self, weapon: Weapon):
        self.weapon = weapon
        return f"{self.name} экипирован оружием {self.weapon.name}"

    def equip_armor(self, armor: Armor):
        self.armor = armor
        return f"{self.name} экипирован броней {self.weapon.name}"

    def _count_damage(self, target: BaseUnit) -> int:
        # Проверяем на выносливость персонажа
        if self.stamina >= self.weapon.stamina_per_hit:

            attack_damage = self.weapon.damage * self.unit_class.attack
            self.stamina -= self.weapon.stamina_per_hit
            if self.stamina < 0:
                self.stamina = 0
            # Смотрим на выносливость соперника, для расчета урона
            if target.stamina >= target.armor.stamina_per_turn:
                target_armor = target.armor.defence * target.unit_class.armor
                damage = attack_damage - target_armor
                target.stamina -= target.armor.stamina_per_turn
                if target.stamina < 0:
                    target.stamina = 0
            else:
                damage = attack_damage
            return target.get_damage(damage)
        else:
            return target.get_damage(0)

    def get_damage(self, damage: int) -> Optional[int]:
        if damage > 0:
            self.hp -= damage
            if self.hp < 0:
                self.hp = 0
            return round(damage, 2)
        else:
            return 0

    @abstractmethod
    def hit(self, target: BaseUnit) -> str:
        pass

    def use_skill(self, target: BaseUnit) -> str:
        """
        метод использования умения.
        если умение уже использовано возвращаем строку
        Навык использован
        Если же умение не использовано тогда выполняем функцию
        self.unit_class.skill.use(user=self, target=target)
        и уже эта функция вернем нам строку которая характеризует выполнение умения
        """
        if self._is_skill_used:
            return f'Навык уже использован.'
        else:
            self._is_skill_used = True
            return self.unit_class.skill.use(user=self, target=target)


class PlayerUnit(BaseUnit):

    def hit(self, target: BaseUnit) -> str:
        """
        функция удар игрока:
        здесь происходит проверка достаточно ли выносливости для нанесения удара.
        вызывается функция self._count_damage(target)
        а также возвращается результат в виде строки
        """
        damage = self._count_damage(target)
        if self.stamina < self.weapon.stamina_per_hit:
            return f"{self.name} попытался использовать {self.weapon.name}, но у него не хватило выносливости."
        else:
            if damage == self.weapon.damage * self.unit_class.attack:
                return f"{self.name} используя {self.weapon.name} пробивает {target.armor.name}" \
                       f" соперника и наносит {damage} урона."
            else:
                return f"{self.name} используя {self.weapon.name} наносит удар, но {target.armor.name}" \
                       f" cоперника его останавливает."


class EnemyUnit(BaseUnit):

    def hit(self, target: BaseUnit) -> str:
        """
        функция удар соперника
        должна содержать логику применения соперником умения
        (он должен делать это автоматически и только 1 раз за бой).
        Например, для этих целей можно использовать функцию randint из библиотеки random.
        Если умение не применено, противник наносит простой удар, где также используется
        функция _count_damage(target
        """
        randomlist = random.sample(range(0, 50), 10)
        if not self._is_skill_used:
            if random.randint(0, 50) in randomlist:
                self._is_skill_used = True
                return self.unit_class.skill.use(user=self, target=target)

        damage = self._count_damage(target)

        if self.stamina < self.weapon.stamina_per_hit:
            return f"{self.name} попытался использовать {self.weapon.name}, но у него не хватило выносливости."
        else:
            if damage == self.weapon.damage * self.unit_class.attack:
                return f"{self.name} используя {self.weapon.name} пробивает {target.armor.name}" \
                       f" соперника и наносит {damage} урона."
            else:
                return f"{self.name} используя {self.weapon.name} наносит удар, но {target.armor.name}" \
                       f" cоперника его останавливает."
