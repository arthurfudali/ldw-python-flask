from flask import Flask;
import pymysql
from controllers import routes;
from models.database import db

app = Flask(__name__, template_folder='views')
routes.init_app(app)

DB_NAME = 'racingcrud'
app.config['DATABASE_NAME'] = DB_NAME

# Passando o endereço do banco ao Flask
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://root@localhost/{DB_NAME}'


if __name__ == '__main__':
    # Criando os dados de conexão:
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='',
                                 charset='',
                                 cursorclass=pymysql.cursors.DictCursor)
    # Tentando criar o banco
    # Try, trata o sucesso
    try:
        # with cria um recurso temporariamente
        with connection.cursor() as cursor:  # alias
            # Cria o banco de dados (se ele não existir)
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
            print(f"O banco de dados {DB_NAME} está criado!")
    # Except, trata a falha
    except Exception as e:
        print(f"Erro ao criar o banco de dados: {e}")
    finally:
        connection.close()

    # Passando o flask para SQLAlchemy
    db.init_app(app=app)

    # Criando as tabelas a partir do model
    with app.test_request_context():
        db.create_all()
        
    # mudar para 0.0.0.0
    app.run(host='localhost', port=4000, debug=True)
