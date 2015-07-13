#!/usr/bin/env python3

# -------
# imports
# -------

from unittest import main, TestCase
from models import Character, Planet, Species
from setupDB import create_db

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

    def test_planet_1(self):
        p = Planet.query.filter_by(name="Kamino")

        self.assertEqual(p[0].name, "Kamino")
        self.assertEqual(p[0].region, "Wild Space\nExtra-galactic")
        self.assertEqual(p[0].system, "Kamino system")

    def test_planet_2(self):
        p = Planet.query.filter_by(name="Kashyyyk")

        self.assertEqual(p[0].name, "Kashyyyk")
        self.assertEqual(p[0].region, "Mid Rim")
        self.assertEqual(p[0].system, "Kashyyyk system")

    def test_planet_3(self):
        p = Planet.query.filter_by(name="Tatooine")

        self.assertEqual(p[0].name, "Tatooine")
        self.assertEqual(p[0].region, "Outer Rim Territories")
        self.assertEqual(p[0].system, "Tatoo system")

    def test_get_all_planets(self):
        planets = Planet.get_all()
        char_name = [planets[i].name for i in range(len(planets))]
        expected = ['Kashyyyk', 'Tatooine', 'Ando', 'Rindao', 'Omwat', 'Ithor', 'Gamorr', 'Kubindi', 'Kiffex',
                    'Coruscant', 'Honoghr', 'Csilla', 'Anzat', 'Deyer', 'Corellia', 'Bakura', 'Chandrila',
                    'Nar Shaddaa', 'Dac', 'Kinyen', 'Wayland', 'Vinsoth', 'Toola', 'Firrerre', 'Kothlis', 'Ator',
                    'Yavin 4', 'Commenor', 'Ylix', 'Sullust', 'Chad', 'Alzoc III', 'Klatooine', 'Eriadu', 'Nal Hutta',
                    'Endor', 'Rodia', 'Stewjon', 'Devaron', 'Ryloth', 'Hapes', 'Dathomir', 'Gand', 'Alderaan',
                    'Trandosha', 'Khomm', 'Irmenu', "Clak'dor VII", 'Lwhekk', 'Kamino', 'Sriluur', 'Kowak', 'Naboo',
                    'Bespin', 'Socorro']

        # comparing the two list elements ignoring order
        result = not set(char_name).isdisjoint(expected)

        self.assertEqual(result, True)

    def test_get_planet_1(self):
        p = Planet.get("Kamino")
        self.assertEqual(p.name, "Kamino")
        self.assertEqual(p.region, "Wild Space\nExtra-galactic")
        self.assertEqual(p.system, "Kamino system")

    def test_get_planet_2(self):
        p = Planet.get("Kashyyyk")
        self.assertEqual(p.name, "Kashyyyk")
        self.assertEqual(p.region, "Mid Rim")
        self.assertEqual(p.system, "Kashyyyk system")

    def test_get_planet_3(self):
        p = Planet.get("Tatooine")
        self.assertEqual(p.name, "Tatooine")
        self.assertEqual(p.region, "Outer Rim Territories")
        self.assertEqual(p.system, "Tatoo system")

    def test_planet_get_species_1(self):
        p = Planet.get("Kamino")
        species = p.get_species()
        expected = ["Human"]

        # comparing the two list elements ignoring order
        result = not set(species).isdisjoint(expected)

        self.assertEqual(result, True)

    def test_planet_get_species_2(self):
        p = Planet.get("Kashyyyk")
        species = p.get_species()
        expected = ["Wookiee"]

        # comparing the two list elements ignoring order
        result = not set(species).isdisjoint(expected)

        self.assertEqual(result, True)

    def test_planet_get_species_3(self):
        p = Planet.get("Tatooine")
        species = p.get_species()
        expected = ["Jawa", "Human"]

        # comparing the two list elements ignoring order
        result = not set(species).isdisjoint(expected)

        self.assertEqual(result, True)

    def test_planet_get_characters_1(self):
        p = Planet.get("Kamino")
        characters = p.get_characters()
        char_name = [characters[i].name for i in range(len(characters))]
        expected = ["Boba Fett"]

        # comparing the two list elements ignoring order
        result = not set(char_name).isdisjoint(expected)

        self.assertEqual(result, True)

    def test_planet_get_characters_2(self):
        p = Planet.get("Kashyyyk")
        characters = p.get_characters()
        char_name = [characters[i].name for i in range(len(characters))]
        expected = ["Chewbacca", "Lowbacca"]

        # comparing the two list elements ignoring order
        result = not set(char_name).isdisjoint(expected)

        self.assertEqual(result, True)

    def test_planet_get_characters_3(self):
        p = Planet.get("Tatooine")
        characters = p.get_characters()
        char_name = [characters[i].name for i in range(len(characters))]
        expected = ["C-3PO", "Tusken Raiders", "Het Nkik", "Darth Vader", "Luke Skywalker", "Biggs Darklighter"]

        # comparing the two list elements ignoring order
        result = not set(char_name).isdisjoint(expected)

        self.assertEqual(result, True)

    # --------
    # species
    # --------

    def test_species_1 (self) :
        c = Species.query.filter_by(name="Wookiee")

        self.assertEqual(c[0].name, "Wookiee")
        self.assertEqual(c[0].planet, "Kashyyyk")
        self.assertEqual(c[0].language, "Shyriiwook\nXaczik\nThykarann")
        self.assertEqual(c[0].classification, "Mammal")

    def test_species_2 (self) :
        c = Species.query.filter_by(name="Hutt")

        self.assertEqual(c[0].name, "Hutt")
        self.assertEqual(c[0].planet, "Varl")
        self.assertEqual(c[0].language, "Huttese")
        self.assertEqual(c[0].classification, "Unknown")

    def test_species_3 (self) :
        c = Species.query.filter_by(name="Human")

        self.assertEqual(c[0].name, "Human")
        self.assertEqual(c[0].classification, "Mammal")

    def test_get_all_species_1(self) :
        species = Species.get_all()
        species_name = [species[i].name for i in range(len(species))]
        expected = ['Krevaaki', 'Jawa', 'Ewok', 'Rodian', 'Kiffar', 'Talz', 'Gand', 'Noghri', 'Aqualish', 'Bothan', 'Kubaz', 'Quarren', 'Sullustan', 'Ssi-ruuk', 'Chevin', 'Khommite', 'Hutt', 'Chadra-Fan', 'Bith', 'Kowakian monkey-lizard', 'Gran', 'Chiss', 'Trandoshan', 'Wookiee', "Twi'lek", 'Dathomirian', 'Omwati', 'Shistavanen', 'Klatooinian', 'Whiphid', 'Human', 'Firrerreo', 'Anzati', 'Ithorian', 'Devaronian', "Yoda's species", 'Rybet', 'Gamorrean']
        # comparing the two list elements ignoring order
        result = not set(species_name).isdisjoint(expected)

        self.assertEqual(result, True)

    def test_get_all_species_planets (self) :
        species = Species.get_all()
        species_planets = [species[i].planet for i in range(len(species))]
        expected = ['Kashyyyk', 'Coruscant', "Clak'dor VII", 'Omwat']

        # comparing the two list elements ignoring order
        result = not set(species_planets).isdisjoint(expected)

        self.assertEqual(result, True)

    def test_get_all_species_language (self) :
        species = Species.get_all()
        species_language = [species[i].language for i in range(len(species))]
        expected = ['Unknown', 'Jawaese', 'Ewokese', 'Rodese, Basic, Huttese', 'Unknown', 'Talzzi', 'Gand', 'Honoghran', 'Aqualish\nGalactic Basic Standard', 'Bothese \nBotha \nGalactic Basic Standard', 'Kubazian', 'Quarrenese', 'Sullustese', 'Ssi-ruuvi', 'Chevin', 'Galactic Basic Standard', 'Huttese', 'Chadra-Fan', 'Bith', 'Unknown', 'Gran', 'Cheunh\nSy Bisti\nMinnisiat\nOther trade languages', 'Dosh', 'Shyriiwook\nXaczik\nThykarann', "Twi'leki, Basic, Lekku", 'Galactic Basic Standard', 'Omwatese', 'Shistavanen \nBasic', 'Huttese\nKlatooinian', 'Whiphid', 'Galactic Basic Standard\nOthers', 'Unknown', 'Anzat language\nGalactic Basic Standard', 'Ithorese', 'Devaronese', 'Unknown', 'Rybese', 'Gamorrese']

        # comparing the two list elements ignoring order
        result = not set(species_language).isdisjoint(expected)

        self.assertEqual(result, True)

    def test_get_all_species_classification (self) :
        species = Species.get_all()
        species_classification = [species[i].classification for i in range(len(species))]
        expected = ['Unknown', 'Unknown', 'Unknown', 'Unknown', 'Unknown', 'Unknown', 'Insectoid', 'Unknown', 'Amphibian', 'Mammal', 'Mammalian', 'Unknown', 'Unknown', 'Unknown', 'Unknown', 'Unknown', 'Unknown', 'Unknown', 'Craniopod', 'Reptilian', 'Unknown', 'Unknown', 'Unknown', 'Mammal', 'Unknown', 'Unknown', 'Near-Human', 'Unknown', 'Unknown', 'Unknown', 'Mammal', 'Unknown', 'Humanoid', 'Unknown', 'Unknown', 'Unknown', 'Unknown', 'Unknown']

        # comparing the two list elements ignoring order
        result = not set(species_classification).isdisjoint(expected)

        self.assertEqual(result, True)

    def test_get_species_serialize_1 (self) :
        s = Species(name="Human", planet="Coruscant", description="some description", image="some url", language="Galactic Basic Standard", classification="Mammal")
        result_info = s.serialize
        expected_info = {'language': 'Galactic Basic Standard', 'classification': 'Mammal', 'characters': ['Darth Vader', 'Boba Fett'], 'numberofcharacters': 1, 'image': 'some url', 'description': 'some description', 'name': 'Human', 'planet': 'Coruscant'}

        bool_result = result_info["language"] == expected_info["language"] and \
                        result_info["classification"] == expected_info["classification"] and \
                        result_info["name"] == expected_info["name"] and \
                        result_info["planet"] == expected_info["planet"]

        self.assertEqual(bool_result, True)

    def test_get_species_serialize_2 (self) :
        s = Species(name="Wookiee", planet="Kashyyyk", description="some description", image="some url", language="Shyriiwook", classification="Mammal")
        result_info = s.serialize

        expected_info = {'name': 'Wookiee', 'classification': 'Mammal', 'language': 'Shyriiwook', 'image': 'some url', 'characters': 'Chewbacca', 'planet': 'Kashyyyk', 'numberofcharacters': 1, 'description': 'some description'}

        bool_result = result_info["language"] == expected_info["language"] and \
                        result_info["classification"] == expected_info["classification"] and \
                        result_info["name"] == expected_info["name"] and \
                        result_info["planet"] == expected_info["planet"]

        self.assertEqual(bool_result, True)

# ----
# main
# ----
if __name__ == "__main__":
    create_db()
    main()



