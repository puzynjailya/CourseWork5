from flask import request, render_template, redirect, abort, url_for
from flask.views import MethodView

from classes.classes import unit_classes
from classes.equipment import Equipment
from classes.unit import EnemyUnit
from views.choose_hero import heroes

equipment = Equipment()


class ChooseEnemyView(MethodView):

    def get(self):
        result = {
            "header": 'Здесь нужно выбрать соперника',  # для названия страниц
            "classes": unit_classes,
            "weapons": equipment.get_weapons_names(),
            "armors": equipment.get_armors_names()
        }
        return render_template('hero_choosing.html', result=result)

    def post(self):
        global heroes
        enemy_name = request.form['name']
        enemy_unit_class = request.form['unit_class']
        enemy_weapon = request.form['weapon']
        enemy_armor = request.form['armor']

        enemy = EnemyUnit(
            name=enemy_name,
            unit_class=unit_classes.get(enemy_unit_class),
        )
        if enemy_weapon not in equipment.get_weapons_names() or enemy_armor not in equipment.get_armors_names():
            return abort(406)
        else:
            enemy.equip_weapon(equipment.get_weapon(enemy_weapon))
            enemy.equip_armor(equipment.get_armor(enemy_armor))
            heroes['enemy'] = enemy
        return redirect(url_for('fight'))



