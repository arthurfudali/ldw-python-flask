from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Driver(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    cpf = db.Column(db.String(150))
    birth = db.Column(db.String(8))

    def __init__(self, name, cpf, birth):
        self.name = name
        self.cpf = cpf
        self.birth = birth

class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(150))
    year = db.Column(db.Integer)
    manufacturer = db.Column(db.String(150))
    power = db.Column(db.Integer)
    category = db.Column(db.String(150))
    driver_id = db.Column(db.Integer, db.ForeignKey('driver.id'))

    driver = db.relationship('Driver', backref=db.backref('car',  uselist=False ,lazy=True))

    def __init__(self, model, year, manufacturer, power, category, driver_id):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.power = power
        self.category = category
        self.driver_id = driver_id

    


""" 
<th>Modelo</th>
            <th>Ano</th>
            <th>Fabricante</th>
            <th>Potência</th>
            <th>Categoria</th>

 """