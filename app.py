from flask import Flask, render_template
from flask_restx import Api

from classes.base import Arena
from classes.unit import BaseUnit

# Функция создания основного объекта app
from config import Config
from views.choose_enemy import ChooseEnemyView
from views.choose_hero import ChooseHeroView
from views.fight import StartFightView, HitFightView, PassTurnView, SkillFightView, EndFightView
from views.index import StartPageView


def create_app(config):
    app = Flask(__name__, template_folder='templates')
    app.config.from_object(config)
    register_extensions(app)
    return app


# Функция подключения расширений (Flask-SQLAlchemy, Flask-RESTx, ...)
def register_extensions(app):
    app.add_url_rule('/', view_func=StartPageView.as_view('index'))
    app.add_url_rule('/choose-hero/', view_func=ChooseHeroView.as_view('hero_choosing'))
    app.add_url_rule('/choose-enemy/', view_func=ChooseEnemyView.as_view('enemy_choosing'))
    app.add_url_rule('/fight/', view_func=StartFightView.as_view('fight'))
    app.add_url_rule('/fight/hit/', view_func=HitFightView.as_view('hit'))
    app.add_url_rule('/fight/use-skill/', view_func=SkillFightView.as_view('use-skill'))
    app.add_url_rule('/fight/pass-turn/', view_func=PassTurnView.as_view('pass'))
    app.add_url_rule('/fight/end-fight/', view_func=EndFightView.as_view('end'))


app = create_app(Config())
app.debug = True


if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)
