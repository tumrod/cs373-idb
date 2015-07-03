#!/usr/bin/env python3

# -------
# imports
# -------

from io       import StringIO
from unittest import main, TestCase

from models import character, planet, species

# -----------
# 
# -----------

class TestModels (TestCase) :
    # ---------
    # character
    # ---------

    def test_character_1 (self) :
        c = character(name="Boba Fett", species="Human", planet="Kamino", description="some description", image="some url")
        name = c.__get_name__()
        planet = c.__get_planet__()
        species = c.__get_species__()
        des = c.__get_description__()
        image = c.__get_image__()
        self.assertEqual(name, "Boba Fett")
        self.assertEqual(planet, "Kamino")
        self.assertEqual(species, "Human")
        self.assertEqual(des, "some description")
        self.assertEqual(image, "some url")

    def test_character_2 (self) :
        c = character(name="Chewbacca", species="Wookiee", planet="Kashyyyk", description="some description", image="some url")
        name = c.__get_name__()
        planet = c.__get_planet__()
        species = c.__get_species__()
        des = c.__get_description__()
        image = c.__get_image__()
        
        self.assertEqual(name, "Chewbacca")
        self.assertEqual(planet, "Kashyyyk")
        self.assertEqual(species, "Wookiee")
        self.assertEqual(des, "some description")
        self.assertEqual(image, "some url")

    def test_character_3 (self) :
        c = character(name="Darth Vader", species="Human", planet="Tatooine", description="some description", image="some url")
        name = c.__get_name__()
        planet = c.__get_planet__()
        species = c.__get_species__()
        des = c.__get_description__()
        image = c.__get_image__()
        
        self.assertEqual(name, "Darth Vader")
        self.assertEqual(planet, "Tatooine")
        self.assertEqual(species, "Human")
        self.assertEqual(des, "some description")
        self.assertEqual(image, "some url")

    # ------
    # planet
    # ------

    def test_planet_1 (self) :
        p = planet(name="Tatooine", species_list=["Human"], character_list=["Darth Vader"], description="some description", image="some url")
        name = p.__get_name__()
        characters = p.__get_characters__()
        species = p.__get_species__()
        des = p.__get_description__()
        image = p.__get_image__()
        self.assertEqual(name, "Tatooine")
        self.assertEqual(characters, ["Darth Vader",])
        self.assertEqual(species, ["Human",])
        self.assertEqual(des, "some description")
        self.assertEqual(image, "some url")

    def test_planet_2 (self) :
        p = planet(name="Kamino", species_list=["Human"], character_list=["Boba Fett"], description="some description", image="some url")
        name = p.__get_name__()
        characters = p.__get_characters__()
        species = p.__get_species__()
        des = p.__get_description__()
        image = p.__get_image__()
        self.assertEqual(name, "Kamino")
        self.assertEqual(characters, ["Boba Fett",])
        self.assertEqual(species, ["Human",])
        self.assertEqual(des, "some description")
        self.assertEqual(image, "some url")

    def test_planet_3 (self) :
        p = planet(name="Kashyyyk", species_list=["Wookiee"], character_list=["Chewbacca"], description="some description", image="some url")
        name = p.__get_name__()
        characters = p.__get_characters__()
        species = p.__get_species__()
        des = p.__get_description__()
        image = p.__get_image__()
        self.assertEqual(name, "Kashyyyk")
        self.assertEqual(characters, ["Chewbacca",])
        self.assertEqual(species, ["Wookiee",])
        self.assertEqual(des, "some description")
        self.assertEqual(image, "some url")

    # --------
    # species
    # --------

    def test_species_1 (self) :
        s = species(name="Wookiee", planet_list=["Kashyyyk"], character_list=["Chewbacca"], description="some description", image="some url")
        name = s.__get_name__()
        characters = s.__get_characters__()
        planets = s.__get_planets__()
        des = s.__get_description__()
        image = s.__get_image__()
        self.assertEqual(name, "Wookiee")
        self.assertEqual(characters, ["Chewbacca",])
        self.assertEqual(planets, ["Kashyyyk",])
        self.assertEqual(des, "some description")
        self.assertEqual(image, "some url")

    def test_species_2 (self) :
        s = species(name="Human", planet_list=["Tatooine", "Kamino"], character_list=["Darth Vader", "Boba Fett"], description="some description", image="some url")
        name = s.__get_name__()
        characters = s.__get_characters__()
        planets = s.__get_planets__()
        des = s.__get_description__()
        image = s.__get_image__()
        self.assertEqual(name, "Human")
        self.assertEqual(characters, ["Darth Vader", "Boba Fett",])
        self.assertEqual(planets, ["Tatooine", "Kamino",])
        self.assertEqual(des, "some description")
        self.assertEqual(image, "some url")

# ----
# main
# ----
if __name__ == "__main__" :
    main()



