from flask import Flask, render_template
from controllers import routes
from models.database import db
import os
# instancia flask
# __name__ representa o nome do arquivo que esta sendo executado
app = Flask(__name__, template_folder='views')

# inicializa as rotas dentro de controllers
routes.init_app(app)

dir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(dir, 'models/games.sqlite3')

# se for executado diretamente pelo interpretador
if __name__ == '__main__':
    db.init_app(app=app)

    # verifica se o bd ja existe
    with app.test_request_context():
        db.create_all()

    # iniciando o servidor
    app.run(host='localhost', port=5000, debug=True)
