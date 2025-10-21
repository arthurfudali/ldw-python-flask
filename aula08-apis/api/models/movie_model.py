from api import mongo



class Movie():
    def __init__(self, title, description, duration, director, year):
        self.title = title
        self.description = description
        self.duration = duration
        self.director = director
        self.year = year