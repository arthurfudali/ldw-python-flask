from flask import render_template, request, redirect, url_for
import requests, os, datetime
from models.database import db, Car, Driver
from dotenv import load_dotenv


""" Essa aplicação deve possuir 3 rotas.
- Uma página inicial com uma navbar direcionando para outras rotas.
- Em uma dessas rotas a aplicação deve permitir a inclusão e exibição de dados na página através de uma lista.
- Em outra seção deve ser permitido a inclusão de dados através de um dicionário e a exibição deve ser feita através de uma tabela. """

load_dotenv()
api_key = os.getenv("KEY")

def init_app(app):
    @app.route('/')
    def index():
        return render_template('index.html')

    # CRUD pilotos
    
    @app.route('/drivers', methods=['GET', 'POST'])
    @app.route('/drivers/delete/<int:id>')
    def newDriver(id=None):
        if id:
            driver = Driver.query.get(id)
            db.session.delete(driver)
            db.session.commit()
        
        if request.method == 'POST':
            newdriver = Driver(request.form['name'], request.form['cpf'], request.form['birth'] )
            db.session.add(newdriver)
            db.session.commit()
            return redirect(url_for('newDriver'))
        
        else:
            # Captura o valor de 'page' que foi passado pelo método GET
            # Define como padrão o valor 1 e o tipo inteiro
            page = request.args.get('page', 1, type=int)
            # Valor padrão de registros por página 
            per_page = 10
            # Faz um SELECT no banco a partir da pagina informada (page)
            
            drivers_page = Driver.query.paginate(page=page, per_page=per_page)
            
            # Seleciona os consoles
            cars = Car.query.all()

            return render_template('drivers.html', drivers=drivers_page, cars=cars)
    
    @app.route('/drivers/edit/<int:id>', methods=['GET', 'POST'])
    def editDriver(id):
        driver = Driver.query.get(id)
        if request.method == 'POST':
            driver.name = request.form['name']
            driver.cpf = request.form['cpf']
            driver.birth = request.form['birth']
            db.session.commit()
            return redirect((url_for('newDriver')))
        return render_template('editDriver.html', driver=driver)
        

    #CRUD carros
    @app.route('/cars', methods=['GET', 'POST'])
    @app.route('/cars/delete/<int:id>')
    def newCar(id=None):
        if id:
            car = Car.query.get(id)
            db.session.delete(car)
            db.session.commit()
            return redirect(url_for('newCar'))
            
        if request.method == 'POST':
            newcar = Car(request.form['model'], request.form['year'], request.form['manufacturer'], request.form['power'], request.form['category'], request.form['driver_id'])
            db.session.add(newcar)
            db.session.commit()
            return redirect(url_for('newCar'))
        
        else:
            # Captura o valor de 'page' que foi passado pelo método GET
            # Define como padrão o valor 1 e o tipo inteiro
            page = request.args.get('page', 1, type=int)
            # Valor padrão de registros por página 
            per_page = 10
            # Faz um SELECT no banco a partir da pagina informada (page)
            
            cars_page = Car.query.paginate(page=page, per_page=per_page)
            
            # Seleciona os consoles
            drivers = Driver.query.all()

            return render_template('cars.html', cars=cars_page, drivers=drivers)

    @app.route('/cars/edit/<int:id>', methods=['GET', 'POST'])
    def editCar(id):
        car = Car.query.get(id)
        if request.method == 'POST':
            car.model = request.form['model']
            car.year = request.form['year']
            car.manufacturer = request.form['manufacturer']
            car.power = request.form['power']
            car.category = request.form['category']
            car.driver_id = request.form['driver_id']
            db.session.commit()
            return redirect(url_for('newCar'))
        drivers = Driver.query.all()
        return render_template('editCar.html', car=car, drivers=drivers)

    @app.route('/apiraces', methods=['GET'])
    def apiRaces():
        # pega o ano atual
        curYear = datetime.date.today().year
        # pega o ano mas tambem o ano atual como default
        year = request.args.get("year", curYear)
        url = "https://f1-motorsport-data.p.rapidapi.com/schedule"
        querystring = {"year": year}
        headers = {
            "x-rapidapi-key": api_key,
            "x-rapidapi-host": "f1-motorsport-data.p.rapidapi.com"
        }
        response = requests.get(url, headers=headers, params=querystring)
        races_data = response.json()
        print(response.text)
       
        # "flatten" o dicionário em uma lista de corridas
        races = []
        for date, race_list in races_data.items():
            for race in race_list:
                race["dateKey"] = date
                races.append(race)

        return render_template("apiraces.html", races=races, year=int(year), curYear = curYear)