import os
from dataclasses import dataclass
from typing import Union

from marshmallow import ValidationError
from marshmallow_dataclass import class_schema

from config import Config
from scripts.utils import json_loader

from classes.skills import UnitSkill, FuryPunch, HardShot, NecromantFart


@dataclass
class UnitClass:
    name: str
    max_health: Union[float | int]
    max_stamina: Union[float | int]
    attack: Union[float | int]
    stamina: Union[float | int]
    armor: Union[float | int]
    skill: Union[UnitSkill | str]


UnitSchema = class_schema(UnitClass)

HEROES_PATH = os.path.join(Config().DATA_PATH, Config().HEROES_FILE_NAME)
data = json_loader(HEROES_PATH)

try:
    WarriorEntity = UnitSchema().load(data.get('heroes').get('Воин'))
    WarriorEntity.skill = FuryPunch()

    ThiefEntity = UnitSchema().load(data.get('heroes').get('Вор'))
    ThiefEntity.skill = HardShot()

    MagicianEntity = UnitSchema().load(data.get('heroes').get('Маг'))
    MagicianEntity.skill = NecromantFart()

except ValidationError as err:
    print('УПС! Такого персонажа нет в данных.')

# Добавляем данные в словарь со значениями имя сущности: сущность
unit_classes = {
    WarriorEntity.name: WarriorEntity,
    ThiefEntity.name: ThiefEntity,
    MagicianEntity.name: MagicianEntity
}
