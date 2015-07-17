import os
import subprocess
from setupDB import create_db
from flask import *
from models import *
import urllib
import json

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
    if not Character.get(name):
        abort(404)
    else: return json.dumps(Character.get(str(name)).serialize, indent=4)

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
    if not Planet.get(name):
        abort(404) 
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
    if not Species.get(name):
        abort(404)
    else: return json.dumps(Species.get(str(name)).serialize, indent=4)

@app.route('/species')
@app.route('/species/<species>')
def species(species=None):

    if species is not None:
        return render_template('specie.html', species=Species.get(species))
    else:
        all_species = Species.get_all()

    return render_template('species.html', all_species=all_species)



@app.route('/league')
def league(species=None):
    champions_url = urllib.request.urlopen("http://leagueofdowning.link/api/champions/")
    champions = json.loads(champions_url.read().decode('utf-8'))

    items_url = urllib.request.urlopen("http://leagueofdowning.link/api/items/")
    items = json.loads(items_url.read().decode('utf-8'))

    all_champions = {}
    
    for champ_id, champ_info in champions.items():
        champ_name = champ_info['name']
        champ_dict = {}
        
        champ_dict['champ_img'] = champ_info['image']

        champ_items = champ_info['recommended_items']
        total_cost = 0
        items_img_list = []

        for i in champ_items:
            items_info = items[str(i)]
            total_cost += items_info['total_gold']
            i_name = items_info['name']
            i_img = items_info['image']
            i_name_img = [i_name, i_img]
            items_img_list.append(i_name_img)

        champ_dict['total_cost'] = total_cost
        champ_dict['items_img_list'] = items_img_list
        all_champions[champ_name] = champ_dict

    
    return render_template('league.html', all_champions=all_champions)

@app.route('/sitemap.xml')
def site_map():

    sitemap_xml = render_template('sitemap.xml')
    response = make_response(sitemap_xml)
    response.headers["Content-Type"] = "application/xml"

    return response

# ---------
# UnitTests
# ---------

@app.route('/api/tests')
def run_tests():
    print("Running tests")
    script = subprocess.Popen("make test", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    try:
        outs, errs = script.communicate()
    except:
        script.kill()
    print(outs.decode())
    errs = errs.decode()
    return json.dumps({"results": errs})

if __name__ == '__main__':
    create_db()
    app.run(debug=True)
