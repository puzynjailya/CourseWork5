import os
from dataclasses import dataclass
from typing import Union

from marshmallow import ValidationError
from marshmallow_dataclass import class_schema

from config import DATA_PATH, HEROES_FILE_NAME
from ..utils import json_loader

from skills import UnitSkill


@dataclass
class UnitClass:
    name: str
    max_health: Union[float | int]
    max_stamina: Union[float | int]
    attack: Union[float | int]
    armor: Union[float | int]
    stamina: Union[float | int]
    skill: UnitSkill


UnitSchema = class_schema(UnitClass)

HEROES_PATH = os.path.join(DATA_PATH, HEROES_FILE_NAME)
data = json_loader(HEROES_PATH)

try:
    WarriorEntity = UnitSchema().load(data.get('heroes').get('Воин'))
    ThiefEntity = UnitSchema().load(data.get('heroes').get('Вор'))
    MagicianEntity = UnitSchema().load(data.get('heroes').get('Маг'))
except ValidationError as err:
    print('УПС! Такого персонажа нет в данных.')

# Добавляем данные в словарь со значениями имя сущности: сущность
unit_classes = {
    WarriorEntity.name: WarriorEntity,
    ThiefEntity.name: ThiefEntity,
    MagicianEntity.name: MagicianEntity
}
