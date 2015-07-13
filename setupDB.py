#!/usr/bin/env python3

import os
import json

from models import *

relative_path = os.path.dirname(os.path.realpath(__file__)) + '/db'

def create_characters():

    # loop through json
    with open(relative_path + "/all_characters.json") as data_file:
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

def create_species():

    # loop through json
    with open(relative_path + "/all_species.json") as data_file:
            info_dict = json.load(data_file)

    for k, v in info_dict.items():
        name = v["name"]
        planet = v["planet"]
        description = v["description"]
        image = v["image"]
        language = v["language"]
        classification = v["classification"]

        species = Species(name, planet, description, image, language, classification)
        db.session.add(species)
        db.session.commit()

def create_planets():

    # loop through json
    with open(relative_path + "/all_planets.json") as data_file:
            info_dict = json.load(data_file)

    for k, v in info_dict.items():
        name = v["name"]
        description = v["description"]
        image = v["image"]
        region = v["region"]
        system = v["system"]

        planet = Planet(name, description, image, region, system)
        db.session.add(planet)
        db.session.commit()


def create_db():
    db.session.commit()
    db.drop_all()
    db.create_all()
    create_characters()
    create_species()
    create_planets()
