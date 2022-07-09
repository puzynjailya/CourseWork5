import os.path


class Config(object):
    DEBUG = True
    DATA_PATH = os.path.join(os.getcwd(), 'data')
    HEROES_FILE_NAME = 'heroes.json'
    EQUIPMENT_FILE_NAME = 'equipment.json'
    STAMINA_RECOVERY = 1


