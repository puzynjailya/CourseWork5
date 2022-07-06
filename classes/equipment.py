import os
import random
from dataclasses import dataclass
from typing import List, Union, Optional
from random import uniform
import marshmallow_dataclass
import marshmallow


from config import EQUIPMENT_FILE_NAME, DATA_PATH
from utils import json_loader


@dataclass
class Armor:
    id: int
    name: str
    defence: Union[float, int]
    stamina_per_turn: Union[float, int]


@dataclass
class Weapon:
    id: int
    name: str
    min_damage: Union[float, int]
    max_damage: Union[float, int]
    stamina_per_hit: Union[float, int]

    @property
    def damage(self):
        return random.uniform(self.min_damage, self.max_damage)


@dataclass
class EquipmentData:
    weapons: List[Weapon]
    armors: List[Armor]


class Equipment:

    def __init__(self):
        self.equipment = self._get_equipment_data()

    def get_weapon(self, weapon_name) -> Optional[Weapon]:
        if weapon_name in self.get_weapons_names():
            for weapon in self.equipment.weapons:
                if weapon.name == weapon_name:
                    return weapon
        else:
            return None

    def get_armor(self, armor_name) -> Optional[Armor]:
        if armor_name in self.get_armors_names():
            for armor in self.equipment.armors:
                if armor.name == armor_name:
                    return armor
        else:
            return None

    def get_weapons_names(self) -> List[str]:
        return [weapon.name for weapon in self.equipment.weapons]

    def get_armors_names(self) -> List[str]:
        return [armor.name for armor in self.equipment.armors]

    @staticmethod
    def _get_equipment_data() -> EquipmentData:
        data = json_loader(os.path.join(DATA_PATH, EQUIPMENT_FILE_NAME))
        equipment_schema = marshmallow_dataclass.class_schema(EquipmentData)
        try:
            return equipment_schema().load(data)
        except marshmallow.exceptions.ValidationError:
            raise ValueError
