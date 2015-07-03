#!/usr/bin/env python3

# -------
# imports
# -------

from io       import StringIO
from unittest import main, TestCase

from models import Character, Planet, Species

# -----------
# 
# -----------

class TestModels (TestCase) :
    # ---------
    # character
    # ---------

    def test_character_1 (self) :
        c = Character(name="Boba Fett", species="Human", planet="Kamino", description="some description", image="some url", gender="Male", birth="31.5 BBY")
        name = c.get_name()
        planet = c.get_planet()
        species = c.get_species()
        des = c.get_description()
        image = c.get_image()
        gender = c.get_gender()
        birth = c.get_birth()
        
        self.assertEqual(name, "Boba Fett")
        self.assertEqual(planet, "Kamino")
        self.assertEqual(species, "Human")
        self.assertEqual(des, "some description")
        self.assertEqual(image, "some url")
        self.assertEqual(gender, "Male")
        self.assertEqual(birth, "31.5 BBY")

    def test_character_2 (self) :
        c = Character(name="Chewbacca", species="Wookiee", planet="Kashyyyk", description="some description", image="some url", gender="Male", birth="200 BBY")
        name = c.get_name()
        planet = c.get_planet()
        species = c.get_species()
        des = c.get_description()
        image = c.get_image()
        gender = c.get_gender()
        birth = c.get_birth()
        
        self.assertEqual(name, "Chewbacca")
        self.assertEqual(planet, "Kashyyyk")
        self.assertEqual(species, "Wookiee")
        self.assertEqual(des, "some description")
        self.assertEqual(image, "some url")
        self.assertEqual(gender, "Male")
        self.assertEqual(birth, "200 BBY")

    def test_character_3 (self) :
        c = Character(name="Darth Vader", species="Human", planet="Tatooine", description="some description", image="some url", gender="Male", birth="41.9 BBY")
        name = c.get_name()
        planet = c.get_planet()
        species = c.get_species()
        des = c.get_description()
        image = c.get_image()
        gender = c.get_gender()
        birth = c.get_birth()
        
        self.assertEqual(name, "Darth Vader")
        self.assertEqual(planet, "Tatooine")
        self.assertEqual(species, "Human")
        self.assertEqual(des, "some description")
        self.assertEqual(image, "some url")
        self.assertEqual(gender, "Male")
        self.assertEqual(birth, "41.9 BBY")

    # ------
    # planet
    # ------

    def test_planet_1 (self) :
        p = Planet(name="Tatooine", species_list=["Human"], character_list=["Darth Vader"], description="some description", image="some url", region="Outer Rim Territories", system="Tatoo system")
        name = p.get_name()
        characters = p.get_characters()
        species = p.get_species()
        des = p.get_description()
        image = p.get_image()
        region = p.get_region()
        system = p.get_system()
        
        self.assertEqual(name, "Tatooine")
        self.assertEqual(characters, ["Darth Vader",])
        self.assertEqual(species, ["Human",])
        self.assertEqual(des, "some description")
        self.assertEqual(image, "some url")
        self.assertEqual(region, "Outer Rim Territories")
        self.assertEqual(system, "Tatoo system")

    def test_planet_2 (self) :
        p = Planet(name="Kamino", species_list=["Human"], character_list=["Boba Fett"], description="some description", image="some url", region="Wild Space", system="Kamino system")
        name = p.get_name()
        characters = p.get_characters()
        species = p.get_species()
        des = p.get_description()
        image = p.get_image()
        region = p.get_region()
        system = p.get_system()
        
        self.assertEqual(name, "Kamino")
        self.assertEqual(characters, ["Boba Fett",])
        self.assertEqual(species, ["Human",])
        self.assertEqual(des, "some description")
        self.assertEqual(image, "some url")
        self.assertEqual(region, "Wild Space")
        self.assertEqual(system, "Kamino system")

    def test_planet_3 (self) :
        p = Planet(name="Kashyyyk", species_list=["Wookiee"], character_list=["Chewbacca"], description="some description", image="some url", region="Mid Rim", system="Kashyyyk system")
        name = p.get_name()
        characters = p.get_characters()
        species = p.get_species()
        des = p.get_description()
        image = p.get_image()
        region = p.get_region()
        system = p.get_system()
        
        self.assertEqual(name, "Kashyyyk")
        self.assertEqual(characters, ["Chewbacca",])
        self.assertEqual(species, ["Wookiee",])
        self.assertEqual(des, "some description")
        self.assertEqual(image, "some url")
        self.assertEqual(region, "Mid Rim")
        self.assertEqual(system, "Kashyyyk system")

    # --------
    # species
    # --------

    def test_species_1 (self) :
        s = Species(name="Wookiee", planet_list=["Kashyyyk"], character_list=["Chewbacca"], description="some description", image="some url", language="Shyriiwook", classification="Mammal")
        name = s.get_name()
        characters = s.get_characters()
        planets = s.get_planets()
        des = s.get_description()
        image = s.get_image()
        language = s.get_language()
        classification = s.get_classification()
        
        self.assertEqual(name, "Wookiee")
        self.assertEqual(characters, ["Chewbacca",])
        self.assertEqual(planets, ["Kashyyyk",])
        self.assertEqual(des, "some description")
        self.assertEqual(image, "some url")
        self.assertEqual(language, "Shyriiwook")
        self.assertEqual(classification, "Mammal")

    def test_species_2 (self) :
        s = Species(name="Human", planet_list=["Tatooine", "Kamino"], character_list=["Darth Vader", "Boba Fett"], description="some description", image="some url", language="Galactic Basic Standard", classification="Mammal")
        name = s.get_name()
        characters = s.get_characters()
        planets = s.get_planets()
        des = s.get_description()
        image = s.get_image()
        language = s.get_language()
        classification = s.get_classification()
        
        self.assertEqual(name, "Human")
        self.assertEqual(characters, ["Darth Vader", "Boba Fett",])
        self.assertEqual(planets, ["Tatooine", "Kamino",])
        self.assertEqual(des, "some description")
        self.assertEqual(image, "some url")
        self.assertEqual(language, "Galactic Basic Standard")
        self.assertEqual(classification, "Mammal")

# ----
# main
# ----
if __name__ == "__main__" :
    main()



