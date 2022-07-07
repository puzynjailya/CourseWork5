from flask import request, render_template
from flask_restx import Resource, Namespace

from classes.base import Arena
from config import Config

fight_ns = Namespace('fight')
arena = Arena()
heroes = Config.heroes

@fight_ns.route('/')
class StartFightView(Resource):

    @fight_ns.doc('Стартовое окно')
    @fight_ns.response(200, "OK")
    def get(self):
        arena.start_game(player=heroes.get('player'), enemy=heroes.get('enemy'))
        return render_template('fight.html')

@fight_ns.route('/hit/')
class HitFightView(Resource):

    @fight_ns.doc('Стартовое окно')
    @fight_ns.response(200, "OK")
    def get(self):
        pass
