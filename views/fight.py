from flask import request, render_template
from flask_restx import Resource, Namespace
from config import arena

fight_ns = Namespace('fight')


@fight_ns.route('/')
class StartFightView(Resource):

    @fight_ns.doc('Стартовое окно')
    @fight_ns.response(200, "OK")
    def get(self):
        arena.start_game(player=heroes.get('player'), enemy=heroes.get('enemy'))
        return render_template('fight.html')

@fight_ns.route('/hit.')
class HitFightView(Resource):

    @fight_ns.doc('Стартовое окно')
    @fight_ns.response(200, "OK")
    def get(self):



    @fight_ns.doc('Добавление фильма в БД')
    @fight_ns.response(201, "Created")
    def post(self):

        return "", 201, {"location": f"/movies/{movie.id}"}


@movie_ns.route('/<int:bid>')
@movie_ns.doc(params={'genre_id': 'ИД фильма в БД'})
class MovieView(Resource):

    @movie_ns.doc('Получение данных по одному фильму')
    @movie_ns.response(200, "OK")
    @movie_ns.response(404, "Movie not found")
    def get(self, bid):
        try:
            result = movie_service.get_one(bid)
            return result, 200
        except ItemNotFound:
            movie_ns.abort(404, message="Movie not found")

    @movie_ns.doc('Обновление данных фильма')
    @movie_ns.response(204, "OK")
    def put(self, bid):
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = bid
        movie_service.update(req_json)
        return "", 204

    @movie_ns.doc('Удаление  фильма')
    @movie_ns.response(204, "OK")
    def delete(self, bid):
        movie_service.delete(bid)
        return "", 204
