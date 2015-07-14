#!/usr/bin/env python3

# -------
# imports
# -------

from unittest import main, TestCase
from models import Character, Planet, Species
from setupDB import create_db
import requests

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


# ---------
# API Tests
# ---------

class APItest (TestCase) :

    # ----------
    # characters
    # ----------

    def test_get_all_characters_1(self) :
        req = requests.get('http://104.130.25.186/api/characters')
        self.assertEqual(req.status_code, 200)

    def test_get_all_characters_2(self) :
        req = requests.get('http://intergalacticdb.me/api/characters')
        self.assertEqual(req.status_code, 200)

    def test_get_character_1(self) :
        expected = {
            "birth": "31.5 BBY , Kamino",
            "description": "Boba Fett was a Mandalorian warrior and bounty hunter. He was the only unaltered clone of the famed Jango Fett, created in 32 BBY as unit A0050, one of the first of many Fett replicas designed to become part of the Grand Army of the Republic, and was raised as Jango's son. Jango taught Boba much, training him to become a skilled bounty hunter as was his father-figure before him. In 22 BBY, Jango was killed at the Battle of Geonosis, which opened the Clone Wars.",
            "gender": "Male",
            "height": "1.83 meters",
            "image": "http://img2.wikia.nocookie.net/__cb20130920001614/starwars/images/5/58/BobaFettMain2.jpg",
            "name": "Boba Fett",
            "planet": "Kamino",
            "species": "Human"
        }
        actual = requests.get("http://intergalacticdb.me/api/characters/Boba%20Fett").json()
        self.assertEqual(expected, actual)

    def test_get_character_2(self) :
        expected = {
            "birth": "200 BBY, Kashyyyk",
            "description": "Chewbacca (or \"Chewie\", as he was known by his friends) was a legendary Wookiee from Kashyyyk and co-pilot of Han Solo's ship, the Millennium Falcon. He was the son of Attichitcuk, the husband of Mallatobuck, and the father of Lumpawaroo. Chewbacca carried with him the name of an ancient Wookiee hero, the great Bacca, first of the great chieftains of Kashyyyk, and the creator of a sword that denoted leadership among the Wookiees. This name placed Chewbacca in a noble lineage.",
            "gender": "Male",
            "height": "2.28 meters",
            "image": "http://img4.wikia.nocookie.net/__cb20080815045819/starwars/images/thumb/7/73/Chewbaccaheadshot.jpg/500px-Chewbaccaheadshot.jpg",
            "name": "Chewbacca",
            "planet": "Kashyyyk",
            "species": "Wookiee"
        }

        actual = requests.get("http://intergalacticdb.me/api/characters/Chewbacca").json()
        self.assertEqual(expected, actual)

    def test_get_character_3(self) :
        req = requests.get('http://104.130.25.186/api/characters/foo')
        self.assertEqual(req.status_code, 404)

    # -------
    # species
    # -------
    def test_get_all_species_1(self) :
        req = requests.get('http://104.130.25.186/api/species')
        self.assertEqual(req.status_code, 200)

    def test_get_all_species_2(self) :
        req = requests.get('http://intergalacticdb.me/api/species')
        self.assertEqual(req.status_code, 200)

    def test_get_species_1(self) :
        expected = {
            "classification": "Mammal",
            "description": "Tall, hair covered, retractable climbing claws, long life spans",
            "image": "http://img2.wikia.nocookie.net/__cb20061128184734/starwars/images/5/57/ThreeWookieeAmigos-ROTSVD.jpg",
            "language": "Shyriiwook\nXaczik\nThykarann",
            "name": "Wookiee",
            "planet": "Kashyyyk"
        }
        actual = requests.get("http://intergalacticdb.me/api/species/Wookiee").json()
        self.assertEqual(expected, actual)

    def test_get_species_2(self) :
        expected = {
            "classification": "Mammal",
            "description": "Unknown",
            "image": "http://img3.wikia.nocookie.net/__cb20100628191857/starwars/images/5/5d/Humans-TESB30.jpg",
            "language": "Galactic Basic Standard\nOthers",
            "name": "Human",
            "planet": "Coruscant"
        }

        actual = requests.get("http://intergalacticdb.me/api/species/Human").json()
        self.assertEqual(expected, actual)

    def test_get_species_3(self) :
        req = requests.get('http://104.130.25.186/api/species/foo')
        self.assertEqual(req.status_code, 404)

    # -------
    # planets
    # -------

    def test_get_all_planets_1(self) :
        req = requests.get('http://104.130.25.186/api/species')
        self.assertEqual(req.status_code, 200)

    def test_get_all_planets_2(self) :
        req = requests.get('http://intergalacticdb.me/api/species')
        self.assertEqual(req.status_code, 200)

    def test_get_planet_1(self) :
        expected = {
            "description": "Tatooine (pronounced/t\u00e6tu'in/; Jawaese: Tah doo Een e) was a desert world and the first planet in the binary Tatoo star system. It was part of the Arkanis sector in the Outer Rim Territories. It was inhabited by poor locals who mostly farmed moisture for a living. Other activities included used equipment retailing and scrap dealing. The planet was on the 5709-DC Shipping Lane, a spur of the Triellus Trade Route, which itself connected to the Sisar Run.",
            "image": "http://img2.wikia.nocookie.net/__cb20130226044533/starwars/images/thumb/1/18/Tatooine3.png/500px-Tatooine3.png",
            "name": "Tatooine",
            "region": "Outer Rim Territories",
            "system": "Tatoo system"

        }
        actual = requests.get("http://intergalacticdb.me/api/planets/Tatooine").json()
        self.assertEqual(expected, actual)

    def test_get_planet_2(self) :
        expected = {
            "description": "Kamino (pronounced/k\u0259'mino\u028a/), also known as the Planet of Storms, was the watery world where the Clone Army of the Galactic Republic was created, as well as the Kamino Home Fleet. It was inhabited by a race of tall, elegant beings called the Kaminoans, who kept to themselves and were known for their cloning technology. Kamino was located just south of the Rishi Maze, and was governed by the Ruling Council, headed by the Prime Minister.",
            "image": "http://img2.wikia.nocookie.net/__cb20090527045541/starwars/images/thumb/a/a9/Eaw_Kamino.jpg/500px-Eaw_Kamino.jpg",
            "name": "Kamino",
            "region": "Wild Space\nExtra-galactic",
            "system": "Kamino system"
        }

        actual = requests.get("http://intergalacticdb.me/api/planets/Kamino").json()
        self.assertEqual(expected, actual)

    def test_get_planet_3(self) :
        req = requests.get('http://104.130.25.186/api/planets/foo')
        self.assertEqual(req.status_code, 404)

# ----
# main
# ----
if __name__ == "__main__":
    create_db()
    main()




