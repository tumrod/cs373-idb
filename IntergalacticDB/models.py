from flask import Flask, jsonify
from flask.ext.sqlalchemy import SQLAlchemy
import os
import json
from collections import OrderedDict

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/intergalacticdb'
db = SQLAlchemy(app)


relative_path = os.path.dirname(os.path.realpath(__file__)) + '/db/'


class Character(db.Model):
    """
    Character encapsulates a character dictionary containing its information
    """
    
    __tablename__ = 'characters'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    planet = db.Column(db.String(50))
    species = db.Column(db.String(50))
    description = db.Column(db.String(4000))
    image = db.Column(db.String(250))
    birth = db.Column(db.String(50))
    gender = db.Column(db.String(50))
    height = db.Column(db.String(50))
    

    def __init__(self, name, planet, species, description, image, birth, gender, height):
        """
        Initialize the character to have a dictionary of its information
        Input strings of the character's name, planet, species, description, image, birth, gender, and height
        """
        self.name = name
        self.planet = planet
        self.species = species
        self.description = description
        self.image = image
        self.birth = birth
        self.gender = gender
        self.height = height

    def __repr__(self):
        return '<name {}>'.format(self.name)

    @staticmethod
    def get_all():
        """
        Return an list of all character models
        """
        with open(relative_path + "/characters.json") as data_file:
            info_dict = json.load(data_file, object_pairs_hook=OrderedDict)

        characters = [Character(**info_dict[key]) for key in info_dict]

        return characters

    @staticmethod
    def get_all_sorted(sort_by):
        """
        Input the attribute by which to sort the characters
        Return an list of all character models, sorted by the given
               attribute
        """
        with open(relative_path + "/characters.json") as data_file:
            info_dict = json.load(data_file, object_pairs_hook=OrderedDict)

        sorting_options = sort_by.split('_')

        info_dict = OrderedDict(sorted(info_dict.items(), key=lambda x: x[1][sorting_options[0]]))

        if (len(sorting_options) > 1) :
            if sorting_options[1] != '^':
                temp = OrderedDict()

                for item in reversed(info_dict):
                    temp[item] = info_dict[item]

                info_dict = temp

        characters = [Character(**info_dict[key]) for key in info_dict]

        return characters

    @staticmethod
    def get(character):
        """
        Input the character name to retrieve
        Return an instance of this character
        """
        with open(relative_path + "/characters.json") as data_file:
            info_dict = json.load(data_file, object_pairs_hook=OrderedDict)

        return Character(**info_dict[character])

    @staticmethod
    def get_api_characters():
        with open(relative_path + "/characters.json") as data_file:
            info_dict = json.load(data_file, object_pairs_hook=OrderedDict)
        return jsonify({'characters': info_dict})


class Planet(db.Model):
    """
    Planet encapsulates a planet dictionary containing its information
    """
    
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    #characters = db.Column(db.String(4000))     # list? foreign key?
    #species = db.Column(db.String(4000))        # list? foreign key?
    description = db.Column(db.String(4000))
    image = db.Column(db.String(250))
    region = db.Column(db.String(50))
    system = db.Column(db.String(50))
    numberofcharacters = db.Column(db.Integer)
    numberofspecies = db.Column(db.Integer)


    def __init__(self, name, description, image, region, system, numberofcharacters, numberofspecies):
        """
        Initialize the planet to have a dictionary of its information
        Input strings of the planet's name, characters list, species list, description, image, region, and system
        """

        self.name = name
        self.description = description
        self.image = image
        self.region = region
        self.system = system
        self.numberofcharacters = numberofcharacters
        self.numberofspecies = numberofspecies

    def __repr__(self):
        return '<name {}>'.format(self.name)

    @staticmethod
    def get_all():
        """
        Return an list of all planets models
        """
        with open(relative_path + "/planets.json") as data_file:
            info_dict = json.load(data_file, object_pairs_hook=OrderedDict)

        planets = [Planet(**info_dict[key]) for key in info_dict]

        return planets

    @staticmethod
    def get_all_sorted(sort_by):
        """
        Input the attribute by which to sort the characters
        Return an list of all planet models, sorted by the given
               attribute
        """
        with open(relative_path + "/planets.json") as data_file:
            info_dict = json.load(data_file, object_pairs_hook=OrderedDict)

        sorting_options = sort_by.split('_')
        info_dict = OrderedDict(sorted(info_dict.items(), key=lambda x: x[1][sorting_options[0]]))
        if (len(sorting_options) > 1) :
            if sorting_options[1] != '^':
                temp = OrderedDict()

                for item in reversed(info_dict):
                    temp[item] = info_dict[item]

                info_dict = temp

        planet = [Planet(**info_dict[key]) for key in info_dict]

        return planet

    @staticmethod
    def get(planet):
        """
        Input the planet name to retrieve
        Return an instance of this planet
        """
        with open(relative_path + "/planets.json") as data_file:
            info_dict = json.load(data_file, object_pairs_hook=OrderedDict)

        return Planet(**info_dict[planet])


class Species(db.Model):
    """
    Species encapsulates a species dictionary containing its information
    """
    
    __tablename__ = 'species'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    #characters = db.Column(db.String(4000))     # list? #Foreign key?
    planet = db.Column(db.String(4000))         # foreign key?
    description = db.Column(db.String(4000))
    image = db.Column(db.String(250))
    language = db.Column(db.String(50))
    classification = db.Column(db.String(50))
    numberofcharacters = db.Column(db.Integer)


    def __init__(self, name, planet, description, image, language, classification, numberofcharacters):
        """
        Initialize the species to have a dictionary of its information
        Input strings of the species's name, characters list, planet list, description, image, language, and classification
        """
        
        self.name = name
        self.planet = planet
        self.description = description
        self.image = image
        self.language = language
        self.classification = classification
        self.numberofcharacters = numberofcharacters

    def __repr__(self):
        return '<name {}>'.format(self.name)

    @staticmethod
    def get_all():
        """
        Return an OrderedDict of all species, with their names as keys
               and their dicts of information as values
        """
        with open(relative_path + "/species.json") as data_file:
            info_dict = json.load(data_file, object_pairs_hook=OrderedDict)

        species = [Species(**info_dict[key]) for key in info_dict]

        return species

    @staticmethod
    def get_all_sorted(sort_by):
        """
        Input the attribute by which to sort the species
        Return an OrderedDict of all species, with their names as keys
               and their dicts of information as values, sorted by the given
               attribute
        """
        with open(relative_path + "/species.json") as data_file:
            info_dict = json.load(data_file, object_pairs_hook=OrderedDict)

        sorting_options = sort_by.split('_')
        info_dict = OrderedDict(sorted(info_dict.items(), key=lambda x: x[1][sorting_options[0]]))

        if (len(sorting_options) > 1) :
            if sorting_options[1] != '^':
                temp = OrderedDict()

                for item in reversed(info_dict):
                    temp[item] = info_dict[item]

                info_dict = temp

        species = [Species(**info_dict[key]) for key in info_dict]

        return species

    @staticmethod
    def get(species):
        """
        Input the species name to retrieve
        Return an instance of this species
        """
        with open(relative_path + "/species.json") as data_file:
            info_dict = json.load(data_file, object_pairs_hook=OrderedDict)

        return Species(**info_dict[species])


def create_character():

    # loop through json
    with open(relative_path + "/all_characters.json") as data_file:
            info_dict = json.load(data_file)

    for k,v in info_dict.items():
        name = v["name"]
        planet = v["planet"]
        species = v["species"]
        description = v["description"]
        image = v["image"]
        birth = v["birth"]
        gender = v["gender"]
        height = v["height"]

        character = Character(name, planet, species, description, image, birth, gender, height)
        db.session.add(character)
        db.session.commit()

def create_planet():

    # loop through json
    with open(relative_path + "/all_planets.json") as data_file:
            info_dict = json.load(data_file)

    for k,v in info_dict.items():
        name = v["name"]
        description = v["description"]
        image = v["image"]
        region = v["region"]
        system = v["system"]
        numberofcharacters = v["numberofcharacters"]
        numberofspecies = v["numberofspecies"]

        planet = Planet(name, description, image, region, system, numberofcharacters, numberofspecies)
        db.session.add(planet)
        db.session.commit()


def create_species():

    # loop through json
    with open(relative_path + "/all_species.json") as data_file:
            info_dict = json.load(data_file)

    for k,v in info_dict.items():
        name = v["name"]
        planet = v["planets"]
        description = v["description"]
        image = v["image"]
        language = v["language"]
        classification = v["classification"]
        numberofcharacters = v["numberofcharacters"]

        characters = Character.query.filter_by(species=name)
        species = Species(name, planet, description, image, language, classification, numberofcharacters)
        db.session.add(species)
        db.session.commit()


def create_db():
    db.session.commit()
    db.drop_all()
    db.create_all()
    create_character()
    create_planet()
    create_species()

create_db()

