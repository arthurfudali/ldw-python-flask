from flask import Flask;
from controllers import routes;

app = Flask(__name__, template_folder='views')
routes.init_app(app)

if __name__ == '__main__':
    # mudar para 0.0.0.0
    app.run(host='localhost', port=4000, debug=True)
