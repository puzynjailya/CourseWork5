from flask import Flask, render_template
from flask_restx import Api

from classes.base import Arena
from classes.unit import BaseUnit

# Функция создания основного объекта app
from config import Config
from views.choose_enemy import ChooseEnemyView
from views.choose_hero import ChooseHeroView
from views.fight import StartFightView
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
    #app.add_namespace(index_ns)

'''
@app.route("/fight/")
def start_fight():
    arena.start_game(player=heroes.get('player'), enemy=heroes.get('enemy'))
    return render_template('fight.html')


@app.route("/fight/hit")
def hit():
    # TODO кнопка нанесения удара
    # TODO обновляем экран боя (нанесение удара) (шаблон fight.html)
    # TODO если игра идет - вызываем метод player.hit() экземпляра класса арены
    # TODO если игра не идет - пропускаем срабатывание метода (простот рендерим шаблон с текущими данными)
    pass


@app.route("/fight/use-skill")
def use_skill():
    # TODO кнопка использования скилла
    # TODO логика пркатикчески идентична предыдущему эндпоинту
    pass


@app.route("/fight/pass-turn")
def pass_turn():
    # TODO кнопка пропус хода
    # TODO логика пркатикчески идентична предыдущему эндпоинту
    # TODO однако вызываем здесь функцию следующий ход (arena.next_turn())
    pass


@app.route("/fight/end-fight")
def end_fight():
    return render_template("index.html", heroes=heroes)


@app.route("/choose-hero/", methods=['post', 'get'])
def choose_hero():
    # TODO кнопка выбор героя. 2 метода GET и POST
    # TODO на GET отрисовываем форму.
    # TODO на POST отправляем форму и делаем редирект на эндпоинт choose enemy
    pass


@app.route("/choose-enemy/", methods=['post', 'get'])
def choose_enemy():
    # TODO кнопка выбор соперников. 2 метода GET и POST
    # TODO также на GET отрисовываем форму.
    # TODO а на POST отправляем форму и делаем редирект на начало битвы
    pass
'''

app = create_app(Config())
app.debug = True


if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)
