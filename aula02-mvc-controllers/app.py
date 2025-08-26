from flask import Flask, render_template
from controllers import routes
# instancia flask
# __name__ representa o nome do arquivo que esta sendo executado
app = Flask(__name__, template_folder='views')

# inicializa as rotas dentro de controllers
routes.init_app(app)


# se for executado diretamente pelo interpretador
if __name__ == '__main__':
    # iniciando o servidor
    app.run(host='localhost', port=5000, debug=True)
