from flask import Flask, render_template

# instancia flask
# __name__ representa o nome do arquivo que esta sendo executado
app = Flask(__name__, template_folder='views')

# Rota principal


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


# se for executado diretamente pelo interpretador
if __name__ == '__main__':
    # iniciando o servidor
    app.run(host='localhost', port=5000, debug=True)
