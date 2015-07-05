from flask import Flask, render_template
from models import *

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('splash.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/characters')
@app.route('/characters/sort_by=<sort_by>')
def characters(sort_by=None):

    if sort_by is not None:
        all_characters = Character.get_all_sorted_characters(sort_by)
    else:
        all_characters = Character.get_all_characters()

    return render_template('characters.html', all_characters=all_characters)

@app.route('/planets')
@app.route('/planets/sort_by=<sort_by>')
def planets(sort_by=None):

    if sort_by is not None:
        all_planets = Planet.get_all_sorted_planets(sort_by)
    else:
        all_planets = Planet.get_all_planets()

    return render_template('planets.html', all_planets=all_planets)

@app.route('/species')
@app.route('/species/sort_by=<sort_by>')
def species(sort_by=None):

    if sort_by is not None:
        all_species = Species.get_all_sorted_species(sort_by)
    else:
        all_species = Species.get_all_species()

    return render_template('species.html', all_species=all_species)

if __name__ == '__main__':
    app.run()
