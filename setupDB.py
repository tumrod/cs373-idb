from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/intergalacticdb'
db = SQLAlchemy(app)

#relative_path = os.path.dirname(os.path.realpath(__file__)) + '/db/'

class Character(db.Model):
    """
    Character encapsulates a character dictionary containing its information
    """
    
    __tablename__ = 'characters'
    character_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    #planet = Column(String(50))         # foreign key?
    #species = Column(String(50))        # foreign key?
    planet = db.Column('planet_id', db.Integer, db.ForeignKey("planets.planet_id"))
    species = db.Column('species_id', db.Integer, db.ForeignKey("species"))
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
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    characters = Column(String(50))     # list? foreign key?
    species = Column(String(50))        # list? foreign key?
    description = Column(String(50))
    image = Column(String(50))
    region = Column(String(50))
    system = Column(String(50))
    
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

    def get_info(self):
        """
        Return the dictionary of information on this planet
        """
        return self.planet

    def get_name(self):
        """
        Return a string, the name of this planet
        """
        return self.planet["name"]

    def get_characters(self):
        """
        Return a string, the list of characters of this planet
        """
        return self.planet["characters"]

    def get_species(self):
        """
        Return a string, the list of species of this planet
        """
        return self.planet["species"]

    def get_description(self):
        """
        Return a string, the description of this planet
        """
        return self.planet["description"]

    def get_image(self):
        """
        Return a string, the url of an image of this planet
        """
        return self.planet["image"]
        
    def get_region(self):
        """
        Return a string, the region of this planet
        """
        return self.planet["region"]
        
    def get_system(self):
        """
        Return a string, the system of this planet
        """
        return self.planet["system"]

    @staticmethod
    def get_all_planets():
        """
        Return an list of all planets models
        """
        with open(relative_path + "/planets.json") as data_file:
            info_dict = json.load(data_file, object_pairs_hook=OrderedDict)

        planets = [Planet(**info_dict[key]) for key in info_dict]

        return planets

    @staticmethod
    def get_all_sorted_planets(sort_by):
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
    def get_planet(planet):
        """
        Input the planet name to retrieve
        Return an instance of this planet
        """
        with open(relative_path + "/planets.json") as data_file:
            info_dict = json.load(data_file, object_pairs_hook=OrderedDict)

        return Planet(**info_dict[planet])

class Species:
    """
    Species encapsulates a species dictionary containing its information
    """
    
    __tablename__ = 'species'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    characters = Column(String(50))     # list? #Foreign key?
    planet = Column(String(50))         # foreign key?
    description = Column(String(50))
    image = Column(String(50))
    language = Column(String(50))
    classification = Column(String(50))
    numberofcharacters = Column(Integer)
    
    def __init__(self, name, characters, planet, description, image, language, classification, numberofcharacters):
        """
        Initialize the species to have a dictionary of its information
        Input strings of the species's name, characters list, planet list, description, image, language, and classification
        """
        self.species = {}
        self.species["name"] = name
        self.species["characters"] = characters
        self.species["planet"] = planet
        self.species["description"] = description
        self.species["image"] = image
        self.species["language"] = language
        self.species["classification"] = classification
        self.species["numberofcharacters"] = numberofcharacters

    def get_info(self):
        """
        Return the dictionary of information on this species
        """
        return self.species

    def get_name(self):
        """
        Return a string, the name of this species
        """
        return self.species["name"]

    def get_characters(self):
        """
        Return a string, the list of characters of this species
        """
        return self.species["characters"]

    def get_planet(self):
        """
        Return a string, the home planet of this species
        """
        return self.species["planet"]

    def get_description(self):
        """
        Return a string, the description of this species
        """
        return self.species["description"]

    def get_image(self):
        """
        Return a string, the url of an image of this species
        """
        return self.species["image"]
        
    def get_language(self):
        """
        Return a string, the language of this species
        """
        return self.species["language"]
        
    def get_classification(self):
        """
        Return a string, the classification of this species
        """
        return self.species["classification"]

    @staticmethod
    def get_all_species():
        """
        Return an OrderedDict of all species, with their names as keys
               and their dicts of information as values
        """
        with open(relative_path + "/species.json") as data_file:
            info_dict = json.load(data_file, object_pairs_hook=OrderedDict)

        species = [Species(**info_dict[key]) for key in info_dict]

        return species

    @staticmethod
    def get_all_sorted_species(sort_by):
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
    def get_species(species):
        """
        Input the species name to retrieve
        Return an instance of this species
        """
        with open(relative_path + "/species.json") as data_file:
            info_dict = json.load(data_file, object_pairs_hook=OrderedDict)

        return Species(**info_dict[species])


db.create_all()