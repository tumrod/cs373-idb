import os
import json
from flask import render_template
import setupDB
from models import *

relative_path = os.path.dirname(os.path.realpath(__file__)) + '/db/'

@app.route('/')
def index():
    return render_template('splash.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/characters/null')
@app.route('/species/null')
@app.route('/planets/null')
@app.route('/planets/Unknown')
@app.route('/characters/Unknown')
@app.route('/species/Unknown')
def unknown():
    return render_template('unknown.html')

# ----------
# characters
# ----------

@app.route('/api/characters', methods=['GET'])
def get_characters():
    return json.dumps([i.serialize for i in Character.get_all()], indent=4)

@app.route('/api/characters/<name>')
def get_character_detail(name):
    return json.dumps(Character.get(str(name)).serialize, indent=4)

@app.route('/characters')
@app.route('/characters/<character>')
def characters(character=None):

    if character is not None:
        return render_template('character.html', character=Character.get(character))
    else:
        all_characters = Character.get_all()

    return render_template('characters.html', all_characters=all_characters)

# -------
# planets
# -------

@app.route('/api/planets', methods=['GET'])
def get_planets():
    return json.dumps([i.serialize for i in Planet.get_all()], indent=4)
    
@app.route('/api/planets/<name>')
def get_planet_detail(name):
    return json.dumps(Planet.get(str(name)).serialize, indent=4)

@app.route('/planets')
@app.route('/planets/<planet>')
def planets(planet=None):

    if planet is not None:
        return render_template('planet.html', planet=Planet.get(planet))
    else:
        all_planets = Planet.get_all()

    return render_template('planets.html', all_planets=all_planets)

# -------
# species
# -------

@app.route('/api/species', methods=['GET'])
def get_species():
    return json.dumps([i.serialize for i in Species.get_all()],indent=4)

@app.route('/api/species/<name>')
def get_species_detail(name):
    return json.dumps(Species.get(str(name)).serialize, indent=4)

@app.route('/species')
@app.route('/species/<species>')
def species(species=None):

    if species is not None:
        return render_template('specie.html', species=Species.get(species))
    else:
        all_species = Species.get_all()

    return render_template('species.html', all_species=all_species)

if __name__ == '__main__':
    setupDB.create_db()
    app.run()
