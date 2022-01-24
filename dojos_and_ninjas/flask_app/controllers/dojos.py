from crypt import methods
from flask_app import app
from flask import Flask, render_template, redirect, session, request
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja


@app.route('/')
def index():
    return redirect ('/dojos')

@app.route('/dojos/')
def dojo_home():
    print(Dojo.getAll())
    return render_template('dojo_home.html', allDojos = Dojo.getAll())

@app.route('/createDojo', methods = ['POST'])
def new_dojo():
    info = {
        'name':request.form['name']
    }
    Dojo.save(info)
    return redirect ('/dojos')

@app.route('/dojo_show/<int:id>')
def one_dojo():
    return render_template('dojo_show.html', allNinjas = Ninja.getAll())