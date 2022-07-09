from flask import request, render_template
from flask.views import MethodView

from classes.base import Arena
from views.choose_enemy import heroes

arena = Arena()


# /fight
class StartFightView(MethodView):
    def get(self):
        arena.start_game(player=heroes.get('player'), enemy=heroes.get('enemy'))
        return render_template('fight.html', heroes=heroes)


# /fight/hit/
class HitFightView(MethodView):

    def get(self):
        if arena.game_is_running:
            result = arena.player_hit()
            return render_template('fight.html', heroes=heroes, result=result)
        else:
            result = arena.battle_result
            return render_template('fight.html', heroes=heroes, result=result)


# /fight/use-skill/
class SkillFightView(MethodView):

    def get(self):
        if arena.game_is_running:
            result = arena.player_use_skill()
            return render_template('fight.html', heroes=heroes, result=result)
        else:
            result = arena.battle_result
            return render_template('fight.html', heroes=heroes, result=result)


# /fight/pass-turn
class PassTurnView(MethodView):

    def get(self):
        if arena.game_is_running:
            result = arena.next_turn()
            return render_template('fight.html', heroes=heroes, result=result)
        else:
            result = arena.battle_result
            return render_template('fight.html', heroes=heroes, result=result)


# /fight/end-fight
class EndFightView(MethodView):

    def get(self):
        return render_template("index.html", heroes=heroes)