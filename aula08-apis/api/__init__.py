# o arquivo init diz que a pasta é um pacote -> permite realizar 'imports from api' 
# importando o flask
from flask import Flask
from flask_restful import Api

# carrega as importações nas variaveis
app = Flask(__name__)
api = Api(app)

#import dos recursos
from .resources import movie_resources