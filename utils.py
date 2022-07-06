import json
from json import JSONDecodeError
from typing import Optional
from classes.skills import *

from classes.classes import UnitClass


def json_loader(file_path: str) -> Optional[dict]:
    with open(file_path, 'r', encoding='utf-8') as file:
        try:
            data = json.load(file)
            return data
        except JSONDecodeError:
            print('Ошибка открытия файла JSON')
            return None
        except (FileNotFoundError, FileExistsError):
            print('Ошибка! Файл не найден или вообще не существует.')
            return None


def entity_update(unit: UnitClass) -> UnitClass:
    skill_name = unit.skill
    if skill_name == 'FuryPunch':
        unit.skill = FuryPunch()
    elif skill_name == 'HardShot':
        unit.skill = HardShot()
    elif skill_name == 'NecromantFart':
        unit.skill = NecromantFart()
    return unit

