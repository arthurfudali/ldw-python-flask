from flask import render_template, request, redirect, url_for

""" Essa aplicação deve possuir 3 rotas.
- Uma página inicial com uma navbar direcionando para outras rotas.
- Em uma dessas rotas a aplicação deve permitir a inclusão e exibição de dados na página através de uma lista.
- Em outra seção deve ser permitido a inclusão de dados através de um dicionário e a exibição deve ser feita através de uma tabela. """


def init_app(app):
    # inclusao e exibicao de dados na pagina atraves de uma lista
    racers = ['Senna', 'Prost', 'Verstappen']

    @app.route('/')
    def index():
        return render_template('index.html')
    
    # rota para adicionar e exibir corredores
    @app.rouute('/racers', methods=['GET', 'POST'])
    def racers():
        if request.method == 'POST':
            if request.form.get('racer'):
                racers.append(request.form.get('racer'))
                return redirect(url_for('racers'))

        return render_template('racers.html', racers=racers)
