import os
import random
from dataclasses import dataclass
from typing import List, Union
from random import uniform
import marshmallow_dataclass
import marshmallow
import json

from config import EQUIPMENT_FILE_NAME, DATA_PATH
from utils import json_loader


@dataclass
class Armor:
    name: str
    defence: Union[float, int]
    stamina_per_turn: Union[float, int]


@dataclass
class Weapon:
    name: str
    min_damage: Union[float, int]
    max_damage: Union[float, int]
    stamina_per_hit: Union[float, int]

    @property
    def damage(self):
        return random.uniform(self.min_damage, self.max_damage)


@dataclass
class EquipmentData:
    # TODO содержит 2 списка - с оружием и с броней
    pass


class Equipment:

    def __init__(self):
        self.equipment = self._get_equipment_data()

    def get_weapon(self, weapon_name) -> Weapon:
        # TODO возвращает объект оружия по имени
        pass

    def get_armor(self, armor_name) -> Armor:
        # TODO возвращает объект брони по имени
        pass

    def get_weapons_names(self) -> list:
        # TODO возвращаем список с оружием
        pass

    def get_armors_names(self) -> list:
        # TODO возвращаем список с броней
        pass

    @staticmethod
    def _get_equipment_data() -> EquipmentData:
        # TODO этот метод загружает json в переменную EquipmentData
        data = json_loader(os.path.join(DATA_PATH, EQUIPMENT_FILE_NAME))
        equipment_schema = marshmallow_dataclass.class_schema(EquipmentData)
        try:
            return equipment_schema().load(data)
        except marshmallow.exceptions.ValidationError:
            raise ValueError
