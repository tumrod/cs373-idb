#!/usr/bin/env python3

class character():

    def __init__(self, name, planet, species, description, image):
        self.character = {}
        self.character["name"] = name
        self.character["planet"] = planet
        self.character["species"] = species
        self.character["description"] = description
        self.character["image"] = image

    def __get_info__(self):
        return self.character

    def __get_name__(self):
        return self.character["name"]

    def __get_planet__(self):
        return self.character["planet"]

    def __get_species__(self):
        return self.character["species"]

    def __get_description__(self):
        return self.character["description"]

    def __get_image__(self):
        return self.character["image"]

    def get_all_characters():
        with open("characters.json") as data_file:
            info_dict = json.load(data_file)
        return info_dict


class planet():

    def __init__(self, name, character_list, species_list, description, image):
        self.planet = {}
        self.planet["name"] = name
        self.planet["characters"] = character_list
        self.planet["species"] = species_list
        self.planet["description"] = description
        self.planet["image"] = image

    def __get_info__(self):
        return self.planet

    def __get_name__(self):
        return self.planet["name"]

    def __get_characters__(self):
        return self.planet["characters"]

    def __get_species__(self):
        return self.planet["species"]

    def __get_description__(self):
        return self.planet["description"]

    def __get_image__(self):
        return self.planet["image"]

    def get_all_planets():
        with open("planets.json") as data_file:
            info_dict = json.load(data_file)
        return info_dict

class species():

    def __init__(self, name, character_list, planet_list, description, image):
        self.species = {}
        self.species["name"] = name
        self.species["characters"] = character_list
        self.species["planets"] = planet_list
        self.species["description"] = description
        self.species["image"] = image

    def __get_info__(self):
        return self.species

    def __get_name__(self):
        return self.species["name"]

    def __get_characters__(self):
        return self.species["characters"]

    def __get_planets__(self):
        return self.species["planets"]

    def __get_description__(self):
        return self.species["description"]

    def __get_image__(self):
        return self.species["image"]

    def get_all_species():
        with open("species.json") as data_file:
            info_dict = json.load(data_file)
        return info_dict


