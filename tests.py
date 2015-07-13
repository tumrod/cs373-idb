#!/usr/bin/env python3

# -------
# imports
# -------

from io       import StringIO
from unittest import main, TestCase
from models import *

# -----------
#
# -----------

class TestModels (TestCase) :
    # ---------
    # character
    # ---------

    def test_character_1 (self) :
        c = Character.query.filter_by(name="Boba Fett")

        self.assertEqual(c[0].name, "Boba Fett")
        self.assertEqual(c[0].planet, "Kamino")
        self.assertEqual(c[0].species, "Human")
        self.assertEqual(c[0].gender, "Male")
        self.assertEqual(c[0].birth, "31.5 BBY , Kamino")
        self.assertEqual(c[0].height, "1.83 meters")



    def test_character_2 (self) :
        c = Character.query.filter_by(name="Chewbacca")

        self.assertEqual(c[0].name, "Chewbacca")
        self.assertEqual(c[0].planet, "Kashyyyk")
        self.assertEqual(c[0].species, "Wookiee")
        self.assertEqual(c[0].gender, "Male")
        self.assertEqual(c[0].birth, "200 BBY, Kashyyyk")
        self.assertEqual(c[0].height, "2.28 meters")

    def test_character_3 (self) :
        c = Character.query.filter_by(name="Darth Vader")

        self.assertEqual(c[0].name, "Darth Vader")
        self.assertEqual(c[0].planet, "Tatooine")
        self.assertEqual(c[0].species, "Human")
        self.assertEqual(c[0].gender, "Male")
        self.assertEqual(c[0].birth, "41.9 BBY")
        self.assertEqual(c[0].height, "1.88 meters, later 2.02 in armor")

    def test_get_all_1(self) :
        characters = Character.get_all()
        char_name = [characters[i].name for i in range(len(characters))]
        expected = ['Greedo', 'Anakin Solo', 'Garindan', 'C-3PO', 'Dorsk 81', 'Ree-Yees', 'Lowbacca', 'Bossk', 'Hethrir', 'Dengar', 'Chewbacca', 'Tionne', 'Moruth Doole', 'Winter', 'Yoda', 'Lando Calrissian', 'Leia Organa Solo', 'Roganda Ismaren', 'Vima-Da-Boda', 'Wicket Wystri Warrick', 'Davin Felth', 'Owen Lars', 'Weequay', 'Grand Admiral Thrawn', 'Biggs Darklighter', 'Lak Sivrak', 'Emperor Palpatine', 'IG-88', 'Nien Nunb', 'Prince Isolder', 'Kyp Durron', 'Cindel Towani', 'Mako Spince', 'Momaw Nadon', 'Gaeriel Captison', '4-LOM', 'Admiral Daala', 'Mon Mothma', 'Ken', 'Tigris', 'Han Solo', 'Nichos Marr', 'Jabba the Hutt', 'Gallandro', 'Salla Zend', 'Mara Jade', 'Teneniel Djo', 'Nomi Sunrider', 'Luke Skywalker', 'Ponda Baba', 'Gethzerion', 'Obi-Wan Kenobi', 'Jacen Solo', 'General Jan Dodonna', 'Garm Bel Iblis', 'Pter Thanas', "Yarna D'al' Gargan", 'General Crix Madine', 'Callista', 'Qwi Xux', 'Grand Moff Tarkin', 'Bib Fortuna', 'Tenel Ka', 'Lobot', 'Labria', 'Triclops', "Emperor's Royal Guards", 'Tusken Raiders', 'Wedge Antilles', 'Shug Ninx', 'Brea Tonnika', "Elder Sh'tk'ith", "Joruus C'baoth", 'Dannik Jerriko', 'Barada', 'Tessek', 'Khabarakh', 'Rillao', 'Ephant Mon', 'Talon Karrde', 'Lady Valarian', 'Admiral Ackbar', 'Exar Kun', "Figrin D'an", 'Oola', 'Ulic Qel-Droma', "Borsk Fey'lya", 'Het Nkik', 'Kabe', 'Zuckuss', 'Captain Gilad Pellaeon', 'Darth Vader', 'Salacious Crumb', 'Bodo Baas', 'Bollux', 'Dev Sibwarra', 'Gartogg', 'Princess Kneesaa', 'Boba Fett', 'Muftak']

        # comparing the two list elements ignoring order
        result = not set(char_name).isdisjoint(expected)

        self.assertEqual(result, True)

    def test_get_character_1(self):
        c = Character.get("Chewbacca")
        self.assertEqual(c.name, "Chewbacca")
        self.assertEqual(c.planet, "Kashyyyk")
        self.assertEqual(c.species, "Wookiee")
        self.assertEqual(c.gender, "Male")
        self.assertEqual(c.birth, "200 BBY, Kashyyyk")
        self.assertEqual(c.height, "2.28 meters")

    def test_get_character_2(self):
        c = Character.get("Boba Fett")

        self.assertEqual(c.name, "Boba Fett")
        self.assertEqual(c.planet, "Kamino")
        self.assertEqual(c.species, "Human")
        self.assertEqual(c.gender, "Male")
        self.assertEqual(c.birth, "31.5 BBY , Kamino")
        self.assertEqual(c.height, "1.83 meters")

    def test_get_character_3(self):
        c = Character.get("Darth Vader")

        self.assertEqual(c.name, "Darth Vader")
        self.assertEqual(c.planet, "Tatooine")
        self.assertEqual(c.species, "Human")
        self.assertEqual(c.gender, "Male")
        self.assertEqual(c.birth, "41.9 BBY")
        self.assertEqual(c.height, "1.88 meters, later 2.02 in armor")

    # ------
    # planet
    # ------
    '''
    def test_planet_1 (self) :
        p = m.Planet(name="Tatooine", description="some description", image="some url", region="Outer Rim Territories", system="Tatoo system")
        name = p.name
        des = p.description
        image = p.image
        region = p.region
        system = p.system

        self.assertEqual(name, "Tatooine")
        self.assertEqual(des, "some description")
        self.assertEqual(image, "some url")
        self.assertEqual(region, "Outer Rim Territories")
        self.assertEqual(system, "Tatoo system")

    def test_planet_2 (self) :
        p = m.Planet(name="Kamino", description="some description", image="some url", region="Wild Space", system="Kamino system")
        name = p.name
        des = p.description
        image = p.image
        region = p.region
        system = p.system

        self.assertEqual(name, "Kamino")
        self.assertEqual(des, "some description")
        self.assertEqual(image, "some url")
        self.assertEqual(region, "Wild Space")
        self.assertEqual(system, "Kamino system")

    def test_planet_3 (self) :
        p = m.Planet(name="Kashyyyk", description="some description", image="some url", region="Mid Rim", system="Kashyyyk system")
        name = p.name
        des = p.description
        image = p.image
        region = p.region
        system = p.system

        self.assertEqual(name, "Kashyyyk")
        self.assertEqual(des, "some description")
        self.assertEqual(image, "some url")
        self.assertEqual(region, "Mid Rim")
        self.assertEqual(system, "Kashyyyk system")

    def test_get_all_planets_name(self) :
        planets = m.Planet.get_all()
        planet_name = [planets[i].name for i in range(len(planets))]
        expected = ['Tatooine', 'Kamino', 'Kashyyyk', 'Coruscant']

        # comparing the two list elements ignoring order
        result = not set(planet_name).isdisjoint(expected)

        self.assertEqual(result, True)

    def test_get_all_planets_characters(self) :
        planets = m.Planet.get_all()
        planet_char = [planets[i].characters for i in range(len(planets))]
        expected = ['0', '1', '2', '3', '4']

        result = not set(planet_char).isdisjoint(expected)

        self.assertEqual(result, True)


    def test_get_all_planets_species(self) :
        planets = m.Planet.get_all()
        planet_species = [planets[i].name for i in range(len(planets))]
        expected = ['Tatooine', 'Kamino', 'Kashyyyk', 'Coruscant']

        # comparing the two list elements ignoring order
        result = not set(planet_species).isdisjoint(expected)

        self.assertEqual(result, True)

    def test_get_all_planets_regions(self) :
        planets = m.Planet.get_all()
        planet_regions = [planets[i].region for i in range(len(planets))]
        expected = ['Outer Rim Territories', 'Wild Space', 'Mid Rim', 'Core Worlds']
        # comparing the two list elements ignoring order
        result = not set(planet_regions).isdisjoint(expected)

        self.assertEqual(result, True)

    def test_get_all_planets_systems(self) :
        planets = m.Planet.get_all()
        planet_systems = [planets[i].system for i in range(len(planets))]
        expected = ['Tatoo system', 'Kamino system', 'Kashyyyk system', 'Coruscant system']

        # comparing the two list elements ignoring order
        result = not set(planet_systems).isdisjoint(expected)

        self.assertEqual(result, True)

    def test_get_planet_1(self) :
        p = m.Planet.get("Kamino")
        name = p.name
        characters = p.get_characters()
        species = p.get_species()
        des = p.description
        image = p.image
        region = p.region
        system = p.system


        self.assertEqual(name, "Kamino")
        self.assertEqual(str(characters), "[<name Boba Fett>]")
        self.assertEqual(species, [])
        #self.assertEqual(des, "Kamino, also known as the Planet of Storms,[10] was the watery world where the Clone Army of the Galactic Republic was created, as well as the Kamino Home Fleet. It was inhabited by a race of tall, elegant beings called the Kaminoans, who kept to themselves and were known for their cloning technology. Kamino was located just south of the Rishi Maze, and was governed by the Ruling Council, headed by the Prime Minister.")
        self.assertEqual(image, "http://img2.wikia.nocookie.net/__cb20090527045541/starwars/images/thumb/a/a9/Eaw_Kamino.jpg/500px-Eaw_Kamino.jpg")
        self.assertEqual(region, "Wild Space\nExtra-galactic")
        self.assertEqual(system, "Kamino system")


    def test_get_planet_2(self) :
        p = m.Planet.get("Kashyyyk")
        name = p.name
        characters = p.get_characters()
        species = p.get_species()
        des = p.description
        image = p.image
        region = p.region
        system = p.system

        self.assertEqual(name, "Kashyyyk")
        self.assertEqual(str(characters), "[<name Chewbacca>, <name Lowbacca>]")
        self.assertEqual(str(species), '[<name Wookiee>]')
        #self.assertEqual(des, "Kashyyyk (see pronunciation), also known as Wookiee Planet C, Edean, G5-623, and Wookiee World, was a Mid Rim planet. It was the lush, wroshyr tree-filled home world of the Wookiees. It was a member of the Galactic Republic, endured enslavement under the Galactic Empire, and later joined the New Republic.")
        self.assertEqual(image, "http://img3.wikia.nocookie.net/__cb20130202022903/starwars/images/e/e8/Can-cell_kashyyyk.png")
        self.assertEqual(region, "Mid Rim")
        self.assertEqual(system, "Kashyyyk system")

    def test_get_planet_3(self) :
        p = m.Planet.get("Tatooine")
        name = p.name
        characters = p.get_characters()
        species = p.get_species()
        des = p.description
        image = p.image
        region = p.region
        system = p.system

        self.assertEqual(name, "Tatooine")
        self.assertEqual(str(characters), "[<name Biggs Darklighter>, <name Darth Vader>, <name Het Nkik>, <name C-3PO>, <name Tusken Raiders>, <name Luke Skywalker>]")
        self.assertEqual(str(species), "[<name Jawa>]")
        #self.assertEqual(des, "Tatooine was a desert world and the first planet in the binary Tatoo star system. It was part of the Arkanis sector in the Outer Rim Territories. It was inhabited by poor locals who mostly farmed moisture for a living. Other activities included used equipment retailing and scrap dealing. The planet was on the 5709-DC Shipping Lane, a spur of the Triellus Trade Route, which itself connected to the Sisar Run. The planet was not far from the Corellian Run. It had its own navigation system. However, it would still play a role in galactic events, serving as the home of Anakin Skywalker. It was here that Jedi Master Qui-Gon Jinn recognized Anakin's potential to become a Jedi and where he introduced him to Obi-Wan Kenobi, his future master and mentor. Tatooine was also the home of Anakin's son, Luke, where he lived until his early adulthood. The planet acquired a bad reputation, often being viewed as the cesspool of the galaxy due to the large number of criminals who could be found there.")
        self.assertEqual(image, "http://img2.wikia.nocookie.net/__cb20130226044533/starwars/images/thumb/1/18/Tatooine3.png/500px-Tatooine3.png")
        self.assertEqual(region, "Outer Rim Territories")
        self.assertEqual(system, "Tatoo system")

    def test_get_planet_serialize_1 (self) :
        p = m.Planet(name="Kashyyyk", description="some description", image="some url", region="Mid Rim", system="Kashyyyk system")
        result_info = p.serialize

        expected_info = {'description': 'some description', 'name': 'Kashyyyk', 'image': 'some url', 'region': 'Mid Rim', 'characters': ['Chewbacca'], 'species': 'Wookiee', 'system': 'Kashyyyk system'}
        bool_result = result_info["name"] == expected_info["name"] and \
                        result_info["region"] == expected_info["region"] and \
                        result_info["system"] == expected_info["system"] and \
                        result_info["description"] == expected_info["description"]

        self.assertEqual(bool_result, True)

    def test_get_planet_serialize_2 (self) :
        p = m.Planet(name="Kamino", description="some description", image="some url", region="Wild Space", system="Kamino system")
        result_info = p.serialize

        expected_info = {'characters': ['Boba Fett'], 'name': 'Kamino', 'image': 'some url', 'system': 'Kamino system', 'region': 'Wild Space', 'species': 'Human', 'description': 'some description'}
        bool_result = result_info["name"] == expected_info["name"] and \
                        result_info["region"] == expected_info["region"] and \
                        result_info["system"] == expected_info["system"] and \
                        result_info["description"] == expected_info["description"]

        self.assertEqual(bool_result, True)

    def test_get_planet_serialize_3 (self) :
        p = m.Planet(name="Tatooine", description="some description", image="some url", region="Outer Rim Territories", system="Tatoo system")
        result_info = p.serialize

        expected_info = {'description': 'some description', 'name': 'Tatooine', 'species': 'Human', 'system': 'Tatoo system', 'characters': ['Darth Vader'], 'image': 'some url', 'region': 'Outer Rim Territories'}
        bool_result = result_info["name"] == expected_info["name"] and \
                        result_info["region"] == expected_info["region"] and \
                        result_info["system"] == expected_info["system"] and \
                        result_info["description"] == expected_info["description"]

        self.assertEqual(bool_result, True)


    # --------
    # species
    # --------

    def test_species_1 (self) :
        s = m.Species(name="Wookiee", planet="Kashyyyk", description="some description", image="some url", language="Shyriiwook", classification="Mammal")
        name = s.name
        characters = s.get_characters()
        planet = s.planet
        des = s.description
        image = s.image
        language = s.language
        classification = s.classification

        self.assertEqual(name, "Wookiee")
        self.assertEqual(str(characters), "[<name Chewbacca>, <name Lowbacca>]")
        self.assertEqual(planet, "Kashyyyk")
        self.assertEqual(des, "some description")
        self.assertEqual(image, "some url")
        self.assertEqual(language, "Shyriiwook")
        self.assertEqual(classification, "Mammal")

    def test_species_2 (self) :
        s = m.Species(name="Human", planet="Coruscant", description="some description", image="some url", language="Galactic Basic Standard", classification="Mammal")
        name = s.name
        planet = s.planet
        des = s.description
        image = s.image
        language = s.language
        classification = s.classification

        self.assertEqual(name, "Human")
        self.assertEqual(planet, "Coruscant")
        self.assertEqual(des, "some description")
        self.assertEqual(image, "some url")
        self.assertEqual(language, "Galactic Basic Standard")
        self.assertEqual(classification, "Mammal")


    def test_get_all_species_name (self) :
        species = m.Species.get_all()

        species_name = [species[i].name for i in range(len(species))]
        expected = ['Wookiee', 'Human', 'Bith', 'Omwati']

        # comparing the two list elements ignoring order
        result = not set(species_name).isdisjoint(expected)

        self.assertEqual(result, True)

    def test_get_all_species_characters (self) :
        species = m.Species.get_all()
        species_char = [species[i].characters for i in range(len(species))]
        expected = [0, 1, 2, 3, 44]

        result = not set(species_char).isdisjoint(expected)

        self.assertEqual(result, True)

    def test_get_all_species_planets (self) :
        species = m.Species.get_all()
        species_planets = [species[i].planet for i in range(len(species))]
        expected = ['Kashyyyk', 'Coruscant', "Clak'dor VII", 'Omwat']

        # comparing the two list elements ignoring order
        result = not set(species_planets).isdisjoint(expected)

        self.assertEqual(result, True)

    def test_get_all_species_language (self) :
        species = m.Species.get_all()
        species_language = [species[i].language for i in range(len(species))]
        expected = ['Shyriiwook', 'Galactic Basic Standard', 'Bith', 'Omwatese']

        # comparing the two list elements ignoring order
        result = not set(species_language).isdisjoint(expected)

        self.assertEqual(result, True)

    def test_get_all_species_classification (self) :
        species = m.Species.get_all()
        species_classification = [species[i].classification for i in range(len(species))]
        expected = ['Mammal', 'Mammal', 'Craniopod', 'Near-Human']

        # comparing the two list elements ignoring order
        result = not set(species_classification).isdisjoint(expected)

        self.assertEqual(result, True)

    def test_get_species_1 (self) :
        s = m.Species.get("Wookiee")
        name = s.name
        characters = s.get_characters()
        planet = s.planet
        des = s.description
        image = s.image
        language = s.language
        classification = s.classification

        self.assertEqual(name, "Wookiee")
        self.assertEqual(str(characters), "[<name Chewbacca>, <name Lowbacca>]")
        self.assertEqual(planet, "Kashyyyk")
        self.assertEqual(language, "Shyriiwook\nXaczik\nThykarann")
        self.assertEqual(classification, "Mammal")

    def test_get_species_2 (self) :
        s = m.Species.get("Human")
        name = s.name
        planet = s.planet
        des = s.description
        image = s.image
        language = s.language
        classification = s.classification

        self.assertEqual(name, "Human")
        self.assertEqual(planet, "Coruscant")
        self.assertEqual(des, "Unknown")
        self.assertEqual(image, "http://img3.wikia.nocookie.net/__cb20100628191857/starwars/images/5/5d/Humans-TESB30.jpg")
        self.assertEqual(language, "Galactic Basic Standard\nOthers")
        self.assertEqual(classification, "Mammal")

    def test_get_species_3 (self) :
        s = m.Species.get("Hutt")
        name = s.name
        characters = s.get_characters()
        planet = s.planet
        des = s.description
        image = s.image
        language = s.language
        classification = s.classification

        self.assertEqual(name, "Hutt")
        self.assertEqual(str(characters), "[<name Jabba the Hutt>]")
        self.assertEqual(planet, "Varl")
        self.assertEqual(image, "http://img2.wikia.nocookie.net/__cb20130115030417/starwars/images/a/a7/HuttNEGAS.png")
        self.assertEqual(language, "Huttese")
        self.assertEqual(classification, "Unknown")

    def test_get_species_serialize_1 (self) :
        s = m.Species(name="Human", planet="Coruscant", description="some description", image="some url", language="Galactic Basic Standard", classification="Mammal")
        result_info = s.serialize
        expected_info = {'language': 'Galactic Basic Standard', 'classification': 'Mammal', 'characters': ['Darth Vader', 'Boba Fett'], 'numberofcharacters': 1, 'image': 'some url', 'description': 'some description', 'name': 'Human', 'planet': 'Coruscant'}

        bool_result = result_info["language"] == expected_info["language"] and \
                        result_info["classification"] == expected_info["classification"] and \
                        result_info["name"] == expected_info["name"] and \
                        result_info["planet"] == expected_info["planet"]

        self.assertEqual(bool_result, True)


    def test_get_species_serialize_2 (self) :
        s = m.Species(name="Wookiee", planet="Kashyyyk", description="some description", image="some url", language="Shyriiwook", classification="Mammal")
        result_info = s.serialize

        expected_info = {'name': 'Wookiee', 'classification': 'Mammal', 'language': 'Shyriiwook', 'image': 'some url', 'characters': 'Chewbacca', 'planet': 'Kashyyyk', 'numberofcharacters': 1, 'description': 'some description'}

        bool_result = result_info["language"] == expected_info["language"] and \
                        result_info["classification"] == expected_info["classification"] and \
                        result_info["name"] == expected_info["name"] and \
                        result_info["planet"] == expected_info["planet"]

        self.assertEqual(bool_result, True)

    '''


# ----
# main
# ----
if __name__ == "__main__" :
    main()



