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

#receives a list of animal as argument, returns list of animal lists formatted as li elements 
def animal_names_li_elements(animal_list):
    output = ""
    for animal in animal_list:
        output += f"<ul>Animal: {animal.name}</ul>\n"
    return output

@app.route('/')
def home():
    return '<h1>Zoo app</h1>'

@app.route('/animal/<int:id>')
def animal_by_id(id):
    current_animal = Animal.query.filter(Animal.id == id).first()
    return f'''
    <ul>ID: {current_animal.id}</ul>
    <ul>Name: {current_animal.name}</ul>
    <ul>Species: {current_animal.species}</ul>
    <ul>Zookeeper: {current_animal.zookeeper.name}</ul>
    <ul>Enclosure: {current_animal.enclosure.environment}</ul>
    '''

@app.route('/zookeeper/<int:id>')
def zookeeper_by_id(id):
    current_zookeeper = Zookeeper.query.filter(Zookeeper.id == id).first()
    return f'''
    <ul>ID: {current_zookeeper.id}</ul>
    <ul>Name: {current_zookeeper.name}</ul>
    <ul>Birthday {current_zookeeper.birthday}</ul>
    {animal_names_li_elements(current_zookeeper.animals)}
    '''

@app.route('/enclosure/<int:id>')
def enclosure_by_id(id):
    current_enclosure = Enclosure.query.filter(Enclosure.id == id).first()
    return f'''
    <ul>ID {current_enclosure.id}</ul>
    <ul>Environment: {current_enclosure.environment}</ul>
    <ul>Open to Visitors: {True if current_enclosure.open_to_visitors else False}</ul>
    {animal_names_li_elements(current_enclosure.animals)}
    '''

if __name__ == '__main__':
    app.run(port=5555, debug=True)
