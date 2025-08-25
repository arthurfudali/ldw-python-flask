from flask import render_template


def init_app(app):
    @app.route('/')
    def home():  # funcao que sera executada pela rota
        return render_template('index.html')


    @app.route('/games')
    def games():
        title = 'The Witcher 3: Wild Hunt'
        year = 2015
        category = 'RPG'
        # array em python
        players = ['arthur', 'amanda']
        # dicionario em python
        console = {'name': 'Playstation 5', 'maker': 'Sony', 'year': 2020}
        return render_template('games.html',
                            title=title,
                            year=year,
                            category=category,
                            players=players,
                            console=console)
