from flask import render_template, request, redirect, url_for

""" Essa aplicação deve possuir 3 rotas.
- Uma página inicial com uma navbar direcionando para outras rotas.
- Em uma dessas rotas a aplicação deve permitir a inclusão e exibição de dados na página através de uma lista.
- Em outra seção deve ser permitido a inclusão de dados através de um dicionário e a exibição deve ser feita através de uma tabela. """


def init_app(app):
    # inclusao e exibicao de dados na pagina atraves de uma lista
    drivers = ['Senna', 'Prost', 'Verstappen']

    @app.route('/')
    def index():
        return render_template('index.html')
    
    # rota para adicionar e exibir corredores em forma de lista
    @app.route('/drivers', methods=['GET', 'POST'])
    def newDriver():
        if request.method == 'POST':
            driverName = request.form.get('name')
            if driverName:
                drivers.append(driverName)
                return redirect(url_for('newDriver'))

        return render_template('drivers.html', drivers=drivers)


    # inclusao de dados atraves de um dicionario e exibicao em tabela
    cars = [{}]

    @app.route('/cars', methods=['GET', 'POST'])
    def newCar():
        if request.method == 'POST':
            cars.append({
                'model': request.form.get('model'),
                'year': request.form.get('year'),
                'manufacturer': request.form.get('manufacturer'),    
                'category': request.form.get('category'),
                'power': request.form.get('power')
            })
            return redirect(url_for('newCar'))
        
        return render_template('cars.html', cars=cars)
