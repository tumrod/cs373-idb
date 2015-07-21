from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/intergalacticdb'
db = SQLAlchemy(app)


class Character(db.Model):
    """
    Character encapsulates attributes of a character, initialized by default from database
    or from constructor
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
        Initialize the character to the given information
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
        """
        Return representation of this character in format
        <name {}> where {} is character's name
        """
        return '<name {}>'.format(self.name)

    @property
    def serialize(self):
        """
        Return a dictionary of information on this character
        """
        return {
            'name' : self.name,
            'planet' : self.planet,
            'species' : self.species,
            'description' : self.description,
            'image' : self.image,
            'birth' : self.birth,
            'gender' : self.gender,
            'height' : self.height
        }

    @staticmethod
    def get_all():
        """
        Return an list of all character models
        """
        return Character.query.all()

    @staticmethod
    def get(character):
        """
        Input the character name to retrieve
        Return an instance of this character
        """
        return Character.query.filter_by(name=character).first()


class Planet(db.Model):
    """
    Planet encapsulates attributes of a planet, initialized by default from database
    or from constructor
    """
    
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(4000))
    image = db.Column(db.String(250))
    region = db.Column(db.String(50))
    system = db.Column(db.String(50))

    def __init__(self, name, description, image, region, system):
        """
        Initialize the planet to the given information
        Input strings of the planet's name, description, image, region, and system
        """

        self.name = name
        self.description = description
        self.image = image
        self.region = region
        self.system = system

    def __repr__(self):
        """
        Return representation of this character in format
        <name {}> where {} is character's name
        """
        return '<name {}>'.format(self.name)

    @property
    def serialize(self):
        """
        Return a dictionary of information on this planet
        """
        return {
            'name' : self.name,
            'description' : self.description,
            'image' : self.image,
            'region' : self.region,
            'system' : self.system,
        }

    def get_characters(self):
        """
        Return an list of the names of all characters of this planet
        """
        return Character.query.filter_by(planet=self.name).all()

    def get_species(self):
        """
        Return an list of the names of all species of this planet
        """
        character_species = {c.species for c in Character.query.filter_by(planet=self.name).all() if c.species != "Unknown"}
        species_name = {s.name for s in Species.query.filter_by(planet=self.name).all() if s.name != "Unknown"}

        return character_species | species_name

    @staticmethod
    def get_all():
        """
        Return an list of all planet models
        """
        return Planet.query.all()

    @staticmethod
    def get(planet):
        """
        Input the character name to retrieve
        Return an instance of this planet
        """
        return Planet.query.filter_by(name=planet).first()


class Species(db.Model):
    """
    Species encapsulates attributes of a species, initialized by default from database
    or from constructor
    """
    
    __tablename__ = 'species'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    planet = db.Column(db.String(4000))
    description = db.Column(db.String(4000))
    image = db.Column(db.String(250))
    language = db.Column(db.String(50))
    classification = db.Column(db.String(50))

    def __init__(self, name, planet, description, image, language, classification):
        """
        Initialize the species to the given information
        Input strings of the species's name, planet, description, image, language, and classification
        """
        
        self.name = name
        self.planet = planet
        self.description = description
        self.image = image
        self.language = language
        self.classification = classification

    def __repr__(self):
        """
        Return representation of this character in format
        <name {}> where {} is character's name
        """
        return '<name {}>'.format(self.name)

    @property
    def serialize(self):
        """
        Return a dictionary of information on this species
        """
        return {
            'name' : self.name,
            'planet' : self.planet,
            'description' : self.description,
            'image' : self.image,
            'language' : self.language,
            'classification' : self.classification,
        }

    def get_characters(self):
        """
        Return an list of the names of all characters of this species
        """
        return Character.query.filter_by(species=self.name).all()

    @staticmethod
    def get_all():
        """
        Return an list of all character species
        """
        return Species.query.all()

    @staticmethod
    def get(species):
        """
        Input the character name to retrieve
        Return an instance of this species
        """
        return Species.query.filter_by(name=species).first()
