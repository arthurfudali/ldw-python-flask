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
    return render_template('games.html')
# se for executado diretamente pelo interpretador
if __name__ == '__main__':
    # iniciando o servidor
    app.run(host='localhost', port=5000, debug=True)
