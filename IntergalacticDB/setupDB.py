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
    name = db.Column(db.String(50), unique=True)
    planet = db.Column(db.String(50))         # foreign key?
    species = db.Column(db.String(50))        # foreign key?
    #planet_id = db.Column('planet_id', db.Integer, db.ForeignKey("planets.planet_id"))
    #species_id = db.Column('species_id', db.Integer, db.ForeignKey("species.species_id"))
    description = db.Column(db.String(250))
    image = db.Column(db.String(100))
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
        return '<id {}>'.format(self.id)


class Planet(db.Model):
    """
    Planet encapsulates a planet dictionary containing its information
    """
    
    __tablename__ = 'planets'
    planet_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    characters = db.Column(db.String(50))     # list? foreign key?
    species = db.Column(db.String(50))        # list? foreign key?
    description = db.Column(db.String(50))
    image = db.Column(db.String(50))
    region = db.Column(db.String(50))
    system = db.Column(db.String(50))
    
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

    def __repr__(self):
        return '<id {}>'.format(self.id)


class Species(db.Model):
    """
    Species encapsulates a species dictionary containing its information
    """
    
    __tablename__ = 'species'
    species_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    characters = db.Column(db.String(50))     # list? #Foreign key?
    planet = db.Column(db.String(50))         # foreign key?
    description = db.Column(db.String(50))
    image = db.Column(db.String(50))
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
    def __repr__(self):
        return '<id {}>'.format(self.id)

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

def create_db():
    db.create_all()
    create_character()

create_db()

