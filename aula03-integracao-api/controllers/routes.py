from flask import render_template, request, redirect, url_for
import urllib  # envia req a uma url
import json  # faz a conversao de dados


def init_app(app):
    # array em python
    players = ['arthur', 'amanda']
    gamelist = [{}]

    @app.route('/')
    def home():  # funcao que sera executada pela rota
        return render_template('index.html')

    # especifica os metodos permitidos
    @app.route('/games', methods=['GET', 'POST'])
    def games():
        title = 'The Witcher 3: Wild Hunt'
        year = 2015
        category = 'RPG'

        # dicionario em python
        console = {'name': 'Playstation 5', 'maker': 'Sony', 'year': 2020}

        # trantando uma requisicao post com request
        if request.method == 'POST':
            # coletando o texto da input
            if request.form.get('player'):
                # adiciona o player na lista
                players.append(request.form.get('player'))
                return redirect(url_for('games'))

        return render_template('games.html',
                               title=title,
                               year=year,
                               category=category,
                               players=players,
                               console=console)

    @app.route('/newGame', methods=['GET', 'POST'])
    def newGame():

        if request.method == 'POST':
            if request.form.get('title') and request.form.get('year') and request.form.get('category'):
                gamelist.append({
                    'title': request.form.get('title'),
                    'year': request.form.get('year'),
                    'category': request.form.get('category')
                })
                return redirect(url_for('newGame'))

        return render_template('newGame.html', gamelist=gamelist)

    @app.route('/apigames', methods=['GET', 'POST'])
    # criando parametros para a rota
    @app.route('/apigames/<int:id>', methods=['GET', 'POST'])
    def apigames(id=None):  # recebe o parametro com None como padrao para nao ser obrigatorio
        url = 'https://www.freetogame.com/api/games'
        response = urllib.request.urlopen(url)
        data = response.read()
        gamesList = json.loads(data)
        gamesDict = {game["id"]: game for game in gamesList}
        if id:
            gameInfo = gamesDict.get(id)

            if gameInfo:
                    return render_template('gameinfo.html', gameInfo=gameInfo)
            else:
                    return f'Jogo nao encontrado'
        else:   
            return render_template('apigames.html', gamesList=gamesList)
