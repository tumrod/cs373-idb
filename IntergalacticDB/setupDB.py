from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/intergalacticdb'
db = SQLAlchemy(app)


relative_path = os.path.dirname(os.path.realpath(__file__)) + '/db/'

class Character(db.Model):
    """
    Character encapsulates a character dictionary containing its information
    """
    
    __tablename__ = 'characters'
    character_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    planet = db.Column(db.String(50))         # foreign key?
    species = db.Column(db.String(50))        # foreign key?
    #planet_id = db.Column('planet_id', db.Integer, db.ForeignKey("planets.planet_id"))
    #species_id = db.Column('species_id', db.Integer, db.ForeignKey("species.species_id"))
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


class Planet(db.Model):
    """
    Planet encapsulates a planet dictionary containing its information
    """
    
    __tablename__ = 'planets'
    planet_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    characters = db.Column(db.String(50))     # list? foreign key?
    species = db.Column(db.String(50))        # list? foreign key?
    description = db.Column(db.String(4000))
    image = db.Column(db.String(250))
    region = db.Column(db.String(50))
    system = db.Column(db.String(50))
    numberofcharacters = db.Column(db.Integer)
    numberofspecies = db.Column(db.Integer)
    
    def __init__(self, name, characters, species, description, image, region, system, numberofcharacters, numberofspecies):
        """
        Initialize the planet to have a dictionary of its information
        Input strings of the planet's name, characters list, species list, description, image, region, and system
        """

        self.name = name
        self.characters = characters
        self.species = species
        self.description = description
        self.image = image
        self.region = region
        self.system = system
        self.numberofcharacters = numberofcharacters
        self.numberofspecies = numberofspecies

    def __repr__(self):
        return '<name {}>'.format(self.name)


class Species(db.Model):
    """
    Species encapsulates a species dictionary containing its information
    """
    
    __tablename__ = 'species'
    species_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    characters = db.Column(db.String(50))     # list? #Foreign key?
    planet = db.Column(db.String(50))         # foreign key?
    description = db.Column(db.String(4000))
    image = db.Column(db.String(250))
    language = db.Column(db.String(50))
    classification = db.Column(db.String(50))
    numberofcharacters = db.Column(db.Integer)
    
    def __init__(self, name, characters, planet, description, image, language, classification, numberofcharacters):
        """
        Initialize the species to have a dictionary of its information
        Input strings of the species's name, characters list, planet list, description, image, language, and classification
        """
        
        self.name = name
        self.characters = characters
        self.planet = planet
        self.description = description
        self.image = image
        self.language = language
        self.classification = classification
        self.numberofcharacters = numberofcharacters

    def __repr__(self):
        return '<name {}>'.format(self.name)

def create_character():

    # loop through json
    with open(relative_path + "/characters.json") as data_file:
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
    with open(relative_path + "/planets.json") as data_file:
            info_dict = json.load(data_file)

    for k,v in info_dict.items():
        name = v["name"]
        characters = v["characters"]
        species = v["species"]
        description = v["description"]
        image = v["image"]
        region = v["region"]
        system = v["system"]
        numberofcharacters = v["numberofcharacters"]
        numberofspecies = v["numberofspecies"]

        planet = Planet(name, characters, species, description, image, region, system, numberofcharacters, numberofspecies)
        db.session.add(planet)
        db.session.commit()

def create_species():

    # loop through json
    with open(relative_path + "/species.json") as data_file:
            info_dict = json.load(data_file)

    for k,v in info_dict.items():
        name = v["name"]
        characters = v["characters"]
        planet = v["planet"]
        description = v["description"]
        image = v["image"]
        language = v["language"]
        classification = v["classification"]
        numberofcharacters = v["numberofcharacters"]

        species = Species(name, characters, planet, description, image, language, classification, numberofcharacters)
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

