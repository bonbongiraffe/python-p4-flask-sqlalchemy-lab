#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Zookeeper, Enclosure, Animal

app = Flask(__name__)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return '<h1>Zoo app</h1>'

@app.route('/animal/<int:id>')
def animal_by_id(id):
    current_animal = Animal.query.filter(Animal.id == id).first()
    print(current_animal)
    return f'''
    <ul>
        <li>ID: {current_animal.id}</li>
        <li>Name: {current_animal.name}</li>
        <li>Species: {current_animal.species}</li>
        <li>Zookeeper: {current_animal.zookeeper.name}</li>
        <li>Enclosure: {current_animal.enclosure.environment}</li>
    </ul>
    '''

@app.route('/zookeeper/<int:id>')
def zookeeper_by_id(id):
    return ''

@app.route('/enclosure/<int:id>')
def enclosure_by_id(id):
    return ''


if __name__ == '__main__':
    app.run(port=5555, debug=True)
