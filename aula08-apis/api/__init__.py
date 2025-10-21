# o arquivo init diz que a pasta é um pacote -> permite realizar 'imports from api' 
# importando o flask
from flask import Flask
from flask_restful import Api
# importando o pymongo
from flask_pymongo import PyMongo
from flask_marshmallow import Marshmallow

# carrega as importações nas variaveis
app = Flask(__name__)

# seta o endereco do DB
app.config["MONGO_URI"] = 'mongodb://localhost:27017/api-movies'

api = Api(app)
mongo = PyMongo(app) # carregando o pymongo
ma = Marshmallow(app)


#import dos recursos
from .resources import movie_resources