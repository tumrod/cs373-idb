#!/usr/bin/env python3

import json, os
from collections import OrderedDict

relative_path = os.path.dirname(os.path.realpath(__file__)) + '/db/'

class Character:

    def __init__(self, name, planet, species, description, image, birth, gender):
        self.character = {}
        self.character["name"] = name
        self.character["planet"] = planet
        self.character["species"] = species
        self.character["description"] = description
        self.character["image"] = image
        self.character["birth"] = birth
        self.character["gender"] = gender

    def get_info(self):
        return self.character

    def get_name(self):
        return self.character["name"]

    def get_planet(self):
        return self.character["planet"]

    def get_species(self):
        return self.character["species"]

    def get_description(self):
        return self.character["description"]

    def get_image(self):
        return self.character["image"]
        
    def get_birth(self):
        return self.character["birth"]
        
    def get_gender(self):
        return self.character["gender"]

    @staticmethod
    def get_all_characters():
        with open(relative_path + "characters.json") as data_file:
            info_dict = json.load(data_file, object_pairs_hook=OrderedDict)
        return info_dict

    @staticmethod
    def get_all_sorted_characters(sort_by):
        with open(relative_path + "characters.json") as data_file:
            info_dict = json.load(data_file, object_pairs_hook=OrderedDict)

        if sort_by == 'name':
            info_dict = OrderedDict(sorted(info_dict.items(), key=lambda x: x[1]['name']))

        return info_dict


class Planet:

    def __init__(self, name, character_list, species_list, description, image, region, system):
        self.planet = {}
        self.planet["name"] = name
        self.planet["characters"] = character_list
        self.planet["species"] = species_list
        self.planet["description"] = description
        self.planet["image"] = image
        self.planet["region"] = region
        self.planet["system"] = system

    def get_info(self):
        return self.planet

    def get_name(self):
        return self.planet["name"]

    def get_characters(self):
        return self.planet["characters"]

    def get_species(self):
        return self.planet["species"]

    def get_description(self):
        return self.planet["description"]

    def get_image(self):
        return self.planet["image"]
        
    def get_region(self):
        return self.planet["region"]
        
    def get_system(self):
        return self.planet["system"]

    @staticmethod
    def get_all_planets():
        with open(relative_path + "planets.json") as data_file:
            info_dict = json.load(data_file, object_pairs_hook=OrderedDict)
        return info_dict

class Species:

    def __init__(self, name, character_list, planet_list, description, image, language, classification):
        self.species = {}
        self.species["name"] = name
        self.species["characters"] = character_list
        self.species["planets"] = planet_list
        self.species["description"] = description
        self.species["image"] = image
        self.species["language"] = language
        self.species["classification"] = classification

    def get_info(self):
        return self.species

    def get_name(self):
        return self.species["name"]

    def get_characters(self):
        return self.species["characters"]

    def get_planets(self):
        return self.species["planets"]

    def get_description(self):
        return self.species["description"]

    def get_image(self):
        return self.species["image"]
        
    def get_language(self):
        return self.species["resignation"]
        
    def get_classification(self):
        return self.species["classification"]

    @staticmethod
    def get_all_species():
        with open(relative_path + "species.json") as data_file:
            info_dict = json.load(data_file, object_pairs_hook=OrderedDict)
        return info_dict
