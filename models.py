from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/intergalacticdb'
db = SQLAlchemy(app)


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
    Planet encapsulates a planet dictionary containing its information
    """
    
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    characters = db.Column(db.String(16))
    species = db.Column(db.String(16))
    description = db.Column(db.String(4000))
    image = db.Column(db.String(250))
    region = db.Column(db.String(50))
    system = db.Column(db.String(50))

    def __init__(self, name, description, image, region, system):
        """
        Initialize the planet to have a dictionary of its information
        Input strings of the planet's name, characters list, species list, description, image, region, and system
        """

        self.name = name
        self.description = description
        self.image = image
        self.region = region
        self.system = system
        self.characters = len(Character.query.filter_by(planet=self.name).all())
        self.species = len(Species.query.filter_by(planet=self.name).all())

    def __repr__(self):
        return '<name {}>'.format(self.name)

    def get_characters(self):
        return Character.query.filter_by(planet=self.name).all()

    def get_species(self):
        return Species.query.filter_by(planet=self.name).all()

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
    Species encapsulates a species dictionary containing its information
    """
    
    __tablename__ = 'species'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    planet = db.Column(db.String(4000))
    description = db.Column(db.String(4000))
    image = db.Column(db.String(250))
    language = db.Column(db.String(50))
    classification = db.Column(db.String(50))
    characters = db.Column(db.Integer)

    def __init__(self, name, planet, description, image, language, classification):
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
        self.characters = len(Character.query.filter_by(species=self.name).all())

    def __repr__(self):
        return '<name {}>'.format(self.name)

    def get_characters(self):
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
