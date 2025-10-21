from api import mongo
from ..models import movie_model

# funcao de cadastrar
def add_movie(movie):
    mongo.db.movies.insert_one({
        'title': movie.title,
        'description': movie.description,
        'duration': movie.duration,
        'director': movie.director,
        'year': movie.year
    })

# funcao listar
def get_movie():
    
    return list(mongo.db.movies.find())
