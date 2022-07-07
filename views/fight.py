from flask import request, render_template
from flask.views import MethodView

from classes.base import Arena
from config import Config

arena = Arena()
heroes = Config.heroes


#/fight
class StartFightView(MethodView):
    def get(self):
        arena.start_game(player=heroes.get('player'), enemy=heroes.get('enemy'))
        return render_template('fight.html')


#/fight/hit
class HitFightView(MethodView):

    def get(self):
        pass
