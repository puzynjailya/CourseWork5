from typing import Union

from unit import BaseUnit
from config import STAMINA_RECOVERY


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

    def start_game(self, player: BaseUnit, enemy: BaseUnit) -> None:
        self.game_is_running = True
        self.player = player
        self.enemy = enemy

    def _check_players_hp(self) -> str:
        if self.player.hp <= 0:
            self.battle_result = f'Игрок {self.player.name} проиграл битву'
            self._end_game()

        elif self.enemy.hp <=0:
            self.battle_result = f"Игрок {self.player.name} выиграл битву"
            self._end_game()

        elif self.player.hp <= 0 and self.enemy.hp <= 0:
            self.battle_result = 'Ничья'
            self._end_game()

    def _stamina_regeneration(self):
        # TODO регенерация здоровья и стамины для игрока и врага за ход
        # TODO в этом методе к количеству стамины игрока и врага прибавляется константное значение.
        # TODO главное чтобы оно не привысило максимальные значения (используйте if)
        if self.player.unit_class.max_stamina <= STAMINA_RECOVERY + self.player.stamina:
            self.player.stamina = self.player.unit_class.max_stamina
        else:
            self.player.stamina +=

    def next_turn(self) -> Union[str, int]:
        # TODO СЛЕДУЮЩИЙ ХОД -> return result | return self.enemy.hit(self.player)
        # TODO срабатывает когда игроп пропускает ход или когда игрок наносит удар.
        # TODO создаем поле result и проверяем что вернется в результате функции self._check_players_hp
        # TODO если result -> возвращаем его
        # TODO если же результата пока нет и после завершения хода игра продолжается,
        # TODO тогда запускаем процесс регенирации стамины и здоровья для игроков (self._stamina_regeneration)
        # TODO и вызываем функцию self.enemy.hit(self.player) - ответный удар врага
        turn_result = self._check_players_hp()
        if turn_result:
            return turn_result
        else:
            self._stamina_regeneration()
            self.enemy.hit(self.player)

    def _end_game(self) -> str:
        self._instances = {}
        self.game_is_running = False
        return self.battle_result

    def player_hit(self) -> str:
        hit_result = self.player.hit(self.enemy)

        # TODO КНОПКА УДАР ИГРОКА -> return result: str
        # TODO получаем результат от функции self.player.hit
        # TODO запускаем следующий ход
        # TODO возвращаем результат удара строкой
        pass

    def player_use_skill(self):
        # TODO КНОПКА ИГРОК ИСПОЛЬЗУЕТ УМЕНИЕ
        # TODO получаем результат от функции self.use_skill
        # TODO включаем следующий ход
        # TODO возвращаем результат удара строкой
        pass
