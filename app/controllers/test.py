from flask import Blueprint, render_template, abort, jsonify
from jinja2 import TemplateNotFound
from models.uno import Uno
from models.dos import Dos
from db import db

simple_page = Blueprint('simple_page', __name__,
                        template_folder='templates')

@simple_page.route('/', defaults={'page': 'index'})
def show(page):
    unos = db.session().query(Uno).all()
    try:
        return render_template('index.html',
                               key="Alejandro",
                               uno=unos)
    except TemplateNotFound:
        abort(404)


@simple_page.route('/create')
def create():
    uno = Uno(title='hola mundo')
    dos = Dos(title='asdasd',
              body='asdasd')
    uno.doses.append(dos)
    db.session.add(uno)
    db.session.add(dos)
    db.session.commit()
    db.session.close()
    try:
        return jsonify(hola='hecho')
    except TemplateNotFound:
        abort(404)