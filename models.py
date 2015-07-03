#!/usr/bin/env python3

import json

class Character:

    def __init__(self, name, planet, species, description, image):
        self.character = {}
        self.character["name"] = name
        self.character["planet"] = planet
        self.character["species"] = species
        self.character["description"] = description
        self.character["image"] = image

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

    @staticmethod
    def get_all_characters():
        with open("characters.json") as data_file:
            info_dict = json.load(data_file)
        return info_dict


class Planet:

    def __init__(self, name, character_list, species_list, description, image):
        self.planet = {}
        self.planet["name"] = name
        self.planet["characters"] = character_list
        self.planet["species"] = species_list
        self.planet["description"] = description
        self.planet["image"] = image

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

    @staticmethod
    def get_all_planets():
        with open("planets.json") as data_file:
            info_dict = json.load(data_file)
        return info_dict

class Species:

    def __init__(self, name, character_list, planet_list, description, image):
        self.species = {}
        self.species["name"] = name
        self.species["characters"] = character_list
        self.species["planets"] = planet_list
        self.species["description"] = description
        self.species["image"] = image

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

    @staticmethod
    def get_all_species():
        with open("species.json") as data_file:
            info_dict = json.load(data_file)
        return info_dict


