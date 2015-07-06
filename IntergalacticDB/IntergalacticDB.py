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
@app.route('/characters/<character>')
@app.route('/characters/sort_by=<sort_by>')
def characters(character=None, sort_by=None):

    if character is not None:
        character = Character.get_character(character)
        return render_template('character.html', character=character)
    elif sort_by is not None:
        all_characters_sorted = Character.get_all_sorted_characters(sort_by)
        return render_template('characters.html', all_characters=all_characters_sorted)
    else:
        all_characters = Character.get_all_characters()
        return render_template('characters.html', all_characters=all_characters)

@app.route('/planets')
@app.route('/planets/<planet>')
@app.route('/planets/sort_by=<sort_by>')
def planets(planet=None, sort_by=None):

    if planet is not None:
        planet = Character.get_character(planet)
        return render_template('planet.html', planet=planet)
    elif sort_by is not None:
        all_planets = Planet.get_all_sorted_planets(sort_by)
    else:
        all_planets = Planet.get_all_planets()

    return render_template('planets.html', all_planets=all_planets)

@app.route('/species')
@app.route('/species/<species>')
@app.route('/species/sort_by=<sort_by>')
def species(species=None, sort_by=None):

    if species is not None:
        species = Species.get_species(species)
        return render_template('species.html', species=species)
    elif sort_by is not None:
        all_species = Species.get_all_sorted_species(sort_by)
    else:
        all_species = Species.get_all_species()

    return render_template('species.html', all_species=all_species)

if __name__ == '__main__':
    app.run()
