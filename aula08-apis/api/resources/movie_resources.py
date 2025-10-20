from flask_restful import Resource
from api import api # variavel api do pacote api 

# criando os recursos de filmes
class MoviesList(Resource):
    # metodos
    def get(self):
        return "Hello world! api is ok!"
    
    
api.add_resource(MoviesList, '/movies')