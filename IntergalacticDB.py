import os
import setupDB
from flask import render_template
from models import *

relative_path = os.path.dirname(os.path.realpath(__file__)) + '/db/'

@app.route('/')
def index():
    return render_template('splash.html')

@app.route('/about')
def about():
    return render_template('about.html')

# ----------
# characters
# ----------

@app.route('/api/characters', methods=['GET'])
def get_characters():
    with open(relative_path + "/characters.json") as data_file:
        info_dict = json.load(data_file, object_pairs_hook=OrderedDict)
    return jsonify({'characters': info_dict})

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
    with open(relative_path + "/planets.json") as data_file:
        info_dict = json.load(data_file, object_pairs_hook=OrderedDict)
    return jsonify({'planets': info_dict})

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
    with open(relative_path + "/species.json") as data_file:
        info_dict = json.load(data_file, object_pairs_hook=OrderedDict)
    return jsonify({'species': info_dict})

@app.route('/species')
@app.route('/species/<species>')
def species(species=None):

    if species is not None:
        return render_template('specie.html', species=Species.get(species))
    else:
        all_species = Species.get_all()

    return render_template('species.html', all_species=all_species)

if __name__ == '__main__':
    app.run()
