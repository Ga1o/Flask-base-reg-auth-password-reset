from flask import render_template
from . import main


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/about')
def about():
    return render_template('about.html')


@main.route('/contacts')
def contacts():
    return render_template('contacts.html')
