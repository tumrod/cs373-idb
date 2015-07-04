#!/usr/bin/env python3

import json, os
from collections import OrderedDict

relative_path = os.path.dirname(os.path.realpath(__file__)) + '/db/'

class Character:
    """
    Character encapsulates a character dictionary containing its information
    """

    def __init__(self, name, planet, species, description, image, birth, gender):
        """
        Initialize the character to have a dictionary of its information
        Input strings of the character's name, planet, species, description, image, birth, and gender
        """
        self.character = {}
        self.character["name"] = name
        self.character["planet"] = planet
        self.character["species"] = species
        self.character["description"] = description
        self.character["image"] = image
        self.character["birth"] = birth
        self.character["gender"] = gender

    def get_info(self):
        """
        Return the dictionary of information on this character
        """
        return self.character

    def get_name(self):
        """
        Return a string, the name of this character
        """
        return self.character["name"]

    def get_planet(self):
        """
        Return a string, the planet homeworld of this character
        """
        return self.character["planet"]

    def get_species(self):
        """
        Return a string, the species of this character
        """
        return self.character["species"]

    def get_description(self):
        """
        Return a string, the summary of this character's description
        """
        return self.character["description"]

    def get_image(self):
        """
        Return a string, the url for an image of this character
        """
        return self.character["image"]

    def get_birth(self):
        """
        Return a string, the birth date of this character
        """
        return self.character["birth"]

    def get_gender(self):
        """
        Return a string, the gender of this character
        """
        return self.character["gender"]

    @staticmethod
    def get_all_characters():
        """
        Return an OrderedDict of all characters, with their names as keys
               and their dicts of information as values
        """
        with open(relative_path + "characters.json") as data_file:
            info_dict = json.load(data_file, object_pairs_hook=OrderedDict)
        return info_dict

    @staticmethod
    def get_all_sorted_characters(sort_by):
        """
        Input the attribute by which to sort the characters
        Return an OrderedDict of all characters, with their names as keys
               and their dicts of information as values, sorted by the given
               attribute
        """
        with open(relative_path + "characters.json") as data_file:
            info_dict = json.load(data_file, object_pairs_hook=OrderedDict)

        info_dict = OrderedDict(sorted(info_dict.items(), key=lambda x: x[1][sort_by]))

        return info_dict

class Planet:
    """
    Planet encapsulates a planet dictionary containing its information
    """

    def __init__(self, name, character_list, species_list, description, image, region, system):
        """
        Initialize the planet to have a dictionary of its information
        Input strings of the planet's name, characters list, species list, description, image, region, and system
        """
        self.planet = {}
        self.planet["name"] = name
        self.planet["characters"] = character_list
        self.planet["species"] = species_list
        self.planet["description"] = description
        self.planet["image"] = image
        self.planet["region"] = region
        self.planet["system"] = system

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
        Return an OrderedDict of all planets, with their names as keys
               and their dicts of information as values
        """
        with open(relative_path + "planets.json") as data_file:
            info_dict = json.load(data_file, object_pairs_hook=OrderedDict)
        return info_dict

class Species:
    """
    Species encapsulates a species dictionary containing its information
    """

    def __init__(self, name, character_list, planet_list, description, image, language, classification):
        """
        Initialize the species to have a dictionary of its information
        Input strings of the species's name, characters list, planet list, description, image, language, and classification
        """
        self.species = {}
        self.species["name"] = name
        self.species["characters"] = character_list
        self.species["planets"] = planet_list
        self.species["description"] = description
        self.species["image"] = image
        self.species["language"] = language
        self.species["classification"] = classification

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

    def get_planets(self):
        """
        Return a string, the list of planets of this species
        """
        return self.species["planets"]

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
        with open(relative_path + "species.json") as data_file:
            info_dict = json.load(data_file, object_pairs_hook=OrderedDict)
        return info_dict
