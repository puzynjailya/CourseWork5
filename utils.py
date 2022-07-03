import json
from json import JSONDecodeError


def json_loader(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        try:
            data = json.load(file)
            return data
        except JSONDecodeError:
            print('Ошибка открытия файла JSON')
        except (FileNotFoundError, FileExistsError):
            print('Ошибка! Файл не найден или вообще не существует.')
