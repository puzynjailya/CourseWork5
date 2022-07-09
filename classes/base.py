from classes.unit import BaseUnit
from config import Config


class BaseSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Arena(metaclass=BaseSingleton):
    # STAMINA_RECOVERY is taken from config.py
    player = None
    enemy = None
    game_is_running: bool = False
    battle_result = None

    def start_game(self, player: BaseUnit, enemy: BaseUnit) -> None:
        self.game_is_running = True
        self.player = player
        self.enemy = enemy

    def _check_players_hp(self) -> str:

        if self.player.hp > 0 and self.enemy.hp > 0:
            return None

        if self.player.hp <= 0:
            self.battle_result = f'Игрок {self.player.name} проиграл битву'

        elif self.enemy.hp <= 0:
            self.battle_result = f"Игрок {self.player.name} выиграл битву"

        elif self.player.hp <= 0 and self.enemy.hp <= 0:
            self.battle_result = 'Ничья'

        self._end_game()
        return self.battle_result

    def _stamina_regeneration(self):
        pl_max_stamina = self.player.unit_class.max_stamina
        en_max_stamina = self.enemy.unit_class.max_stamina

        # player
        if pl_max_stamina < Config().STAMINA_RECOVERY * self.player.unit_class.stamina + self.player.stamina:
            self.player.stamina = self.player.unit_class.max_stamina
        else:
            self.player.stamina += Config().STAMINA_RECOVERY * self.player.unit_class.stamina

        # enemy
        if en_max_stamina < Config().STAMINA_RECOVERY * self.enemy.unit_class.stamina + self.enemy.stamina:
            self.enemy.stamina = self.enemy.unit_class.max_stamina
        else:
            self.enemy.stamina += Config().STAMINA_RECOVERY * self.enemy.unit_class.stamina

    def next_turn(self) -> str:

        if self._check_players_hp() is not None:
            return self._check_players_hp()

        if self.game_is_running:
            self._stamina_regeneration()
            return self.enemy.hit(self.player)

    def _end_game(self) -> str:
        self._instances = {}
        self.game_is_running = False

    def player_hit(self) -> str:
        hit_result = self.player.hit(self.enemy)
        turn_result = self.next_turn()
        return f'Результат мясорубки:\n{hit_result}\n{turn_result}'

    def player_use_skill(self):
        skill_result = self.player.use_skill(self.enemy)
        turn_result = self.next_turn()
        return f'Результат мясорубки:\n{skill_result}\n{turn_result}'
