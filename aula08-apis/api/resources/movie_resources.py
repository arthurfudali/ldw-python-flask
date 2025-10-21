from flask_restful import Resource
from api import api # variavel api do pacote api 
# importando os schemas
from ..schemas import movie_schemas
# importando model
from ..models import movie_model
# importando o service
from ..services import movie_service

from flask import make_response, jsonify

# criando os recursos de filmes
class MoviesList(Resource):
    # metodos
    def get(self):
        movies = movie_service.get_movies()
    
api.add_resource(MoviesList, '/movies')