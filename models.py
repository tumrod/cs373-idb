#!/usr/bin/env python3

import json, os
from collections import OrderedDict

relative_path = os.path.dirname(os.path.realpath(__file__)) + '/db/'

class Character:
    """
    Character encapsulates a character dictionary containing its information
    """

    def __init__(self, name, planet, species, description, image, birth, gender, height):
        """
        Initialize the character to have a dictionary of its information
        Input strings of the character's name, planet, species, description, image, birth, gender, and height
        """
        self.character = {}
        self.character["name"] = name
        self.character["planet"] = planet
        self.character["species"] = species
        self.character["description"] = description
        self.character["image"] = image
        self.character["birth"] = birth
        self.character["gender"] = gender
        self.character["height"] = height

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

    def get_height(self):
        """
        Return a string, the height of this character
        """
        return self.character["height"]

    @staticmethod
    def get_all_characters():
        """
        Return an list of all character models
        """
        with open(relative_path + "characters.json") as data_file:
            info_dict = json.load(data_file, object_pairs_hook=OrderedDict)

        characters = [Character(**info_dict[key]) for key in info_dict]

        return characters

    @staticmethod
    def get_all_sorted_characters(sort_by):
        """
        Input the attribute by which to sort the characters
        Return an list of all character models, sorted by the given
               attribute
        """
        with open(relative_path + "characters.json") as data_file:
            info_dict = json.load(data_file, object_pairs_hook=OrderedDict)

        sorting_options = sort_by.split('_')
        info_dict = OrderedDict(sorted(info_dict.items(), key=lambda x: x[1][sorting_options[0]]))

        if sorting_options[1] != '^':
            temp = OrderedDict()
            reversed_items = list(reversed(sorted(info_dict.keys())))

            for item in reversed_items:
                temp[item] = info_dict[item]

            info_dict = temp

        characters = [Character(**info_dict[key]) for key in info_dict]

        return characters

    @staticmethod
    def get_character(character):
        """
        Input the character name to retrieve
        Return an instance of this character
        """
        with open(relative_path + "characters.json") as data_file:
            info_dict = json.load(data_file, object_pairs_hook=OrderedDict)

        return Character(info_dict[character])

class Planet:
    """
    Planet encapsulates a planet dictionary containing its information
    """

    def __init__(self, name, characters, species, description, image, region, system):
        """
        Initialize the planet to have a dictionary of its information
        Input strings of the planet's name, characters list, species list, description, image, region, and system
        """
        self.planet = {}
        self.planet["name"] = name
        self.planet["characters"] = characters
        self.planet["species"] = species
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
        Return an list of all planets models
        """
        with open(relative_path + "planets.json") as data_file:
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
        with open(relative_path + "planets.json") as data_file:
            info_dict = json.load(data_file, object_pairs_hook=OrderedDict)

        sorting_options = sort_by.split('_')
        info_dict = OrderedDict(sorted(info_dict.items(), key=lambda x: x[1][sorting_options[0]]))

        if sorting_options[1] != '^':
            temp = OrderedDict()
            reversed_items = list(reversed(sorted(info_dict.keys())))

            for item in reversed_items:
                temp[item] = info_dict[item]

            info_dict = temp

        planets = [Planet(**info_dict[key]) for key in info_dict]

        return planets

    @staticmethod
    def get_planet(planet):
        """
        Input the planet name to retrieve
        Return an instance of this planet
        """
        with open(relative_path + "planets.json") as data_file:
            info_dict = json.load(data_file, object_pairs_hook=OrderedDict)

        return Planet(info_dict[planet])

class Species:
    """
    Species encapsulates a species dictionary containing its information
    """

    def __init__(self, name, characters, planet, description, image, language, classification):
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
        with open(relative_path + "species.json") as data_file:
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
        with open(relative_path + "species.json") as data_file:
            info_dict = json.load(data_file, object_pairs_hook=OrderedDict)

        sorting_options = sort_by.split('_')
        info_dict = OrderedDict(sorted(info_dict.items(), key=lambda x: x[1][sorting_options[0]]))

        if sorting_options[1] != '^':
            temp = OrderedDict()
            reversed_items = list(reversed(sorted(info_dict.keys())))

            for item in reversed_items:
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
        with open(relative_path + "planets.json") as data_file:
            info_dict = json.load(data_file, object_pairs_hook=OrderedDict)

        return Species(info_dict[species])
