from flask import request, render_template, redirect, abort, url_for
from flask.views import MethodView

from classes.classes import unit_classes
from classes.equipment import Equipment
from classes.unit import PlayerUnit

equipment = Equipment()

heroes = {}


class ChooseHeroView(MethodView):

    def get(self):
        result = {
            "header": 'Здесь нужно выбрать своего героя',  # для названия страниц
            "classes": unit_classes,
            "weapons": equipment.get_weapons_names(),
            "armors": equipment.get_armors_names()
        }
        return render_template('hero_choosing.html', result=result)

    def post(self):
        player_name = request.form['name']
        player_unit_class = request.form['unit_class']
        player_weapon = request.form['weapon']
        player_armor = request.form['armor']

        player = PlayerUnit(
            name=player_name,
            unit_class=unit_classes.get(player_unit_class),
        )
        if player_weapon not in equipment.get_weapons_names() or player_armor not in equipment.get_armors_names():
            return abort(406)
        else:
            player.equip_weapon(equipment.get_weapon(player_weapon))
            player.equip_armor(equipment.get_armor(player_armor))
            global heroes
            heroes['player'] = player
        return redirect(url_for('enemy_choosing'))

