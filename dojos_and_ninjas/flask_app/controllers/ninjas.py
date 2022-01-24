from dataclasses import dataclass
from flask import render_template, request, redirect

from flask_app import app
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo


@app.route('/ninjas')
def users():
    return render_template('add_ninjas.html')


@app.route('/ninja/new', methods = ['POST'])
def new_ninja():
    print(request.form)
    Ninja.save(request.form)
    return redirect ('/dojos')

