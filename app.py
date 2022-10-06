from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'planets.db')

db = SQLAlchemy(app)


@app.cli.command('db_create')
def db_create():
    db.create_all()
    print("Database created")


@app.cli.command('db_drop')
def db_drop():
    db.drop_all()
    print("Database dropped")


@app.cli.command('db_seed')
def db_seed():
    mercury = Planet(planet_name='mercury',
                     planet_type='Class D',
                     home_star='Sol',
                     mass=3.2e33,
                     radius=1516,
                     distance=39.98e9)
    venus = Planet(planet_name='venus',
                   planet_type='Class D',
                   home_star='Sol',
                   mass=3.2e33,
                   radius=1516,
                   distance=39.98e9)
    jupter = Planet(planet_name='jupter',
                    planet_type='Class D',
                    home_star='Sol',
                    mass=3.2e33,
                    radius=1516,
                    distance=39.98e9)
    db.session.add(mercury)
    db.session.add(venus)
    db.session.add(jupter)

    test_user = User(first_name='wilk',
                     last_name='gillian',
                     email="email",
                     password="123dsd")
    db.session.add(test_user)
    # db.session.commit()
    print("Database seeded")


@app.route('/')
def hello_world():
    return jsonify(message='hello world')


@app.route('/super_simple')
def super_simple():
    return jsonify(message='Hello from the planetary api')


@app.route('/planets', methods=['GET'])
def planets():
    planets_list = Planet.query.all()
    return jsonify(data=planets_list)


class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)


class Planet(db.Model):
    __tablename__ = 'planets'
    planet_id = Column(Integer, primary_key=True)
    planet_name = Column(String)
    planet_type = Column(String)
    home_star = Column(String)
    mass = Column(Float)
    radius = Column(Float)
    distance = Column(Float)


if __name__ == '__main__':
    app.run()
