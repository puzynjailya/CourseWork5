from flask import request, render_template
from flask_restx import Resource, Namespace

ch_ns = Namespace('choose-hero')


@ch_ns.route('/')
class ChooseHeroView(Resource):

    @ch_ns.doc('Отрисовка формы выбора персонажа игрока')
    @ch_ns.response(200, "OK")
    def get(self):
