#!/usr/bin/env python3

# -------
# imports
# -------

from io       import StringIO
from unittest import main, TestCase

import models as m

# -----------
# 
# -----------

class TestModels (TestCase) :
    # ---------
    # character
    # ---------

    def test_character_1 (self) :
        c = m.Character(name="Boba Fett", species="Human", planet="Kamino", description="some description", image="some url", gender="Male", birth="31.5 BBY", height="1.83 meters")
        name = c.name
        planet = c.planet
        species = c.species
        des = c.description
        image = c.image
        gender = c.gender
        birth = c.birth
        height = c.height
        
        self.assertEqual(name, "Boba Fett")
        self.assertEqual(planet, "Kamino")
        self.assertEqual(species, "Human")
        self.assertEqual(des, "some description")
        self.assertEqual(image, "some url")
        self.assertEqual(gender, "Male")
        self.assertEqual(birth, "31.5 BBY")
        self.assertEqual(height, "1.83 meters")

    def test_character_2 (self) :
        c = m.Character(name="Chewbacca", species="Wookiee", planet="Kashyyyk", description="some description", image="some url", gender="Male", birth="200 BBY", height="2.28 meters")
        name = c.name
        planet = c.planet
        species = c.species
        des = c.description
        image = c.image
        gender = c.gender
        birth = c.birth
        height = c.height
        
        self.assertEqual(name, "Chewbacca")
        self.assertEqual(planet, "Kashyyyk")
        self.assertEqual(species, "Wookiee")
        self.assertEqual(des, "some description")
        self.assertEqual(image, "some url")
        self.assertEqual(gender, "Male")
        self.assertEqual(birth, "200 BBY")
        self.assertEqual(height, "2.28 meters")

    def test_character_3 (self) :
        c = m.Character(name="Darth Vader", species="Human", planet="Tatooine", description="some description", image="some url", gender="Male", birth="41.9 BBY", height="2.02 meters")
        name = c.name
        planet = c.planet
        species = c.species
        des = c.description
        image = c.image
        gender = c.gender
        birth = c.birth
        height = c.height
        
        self.assertEqual(name, "Darth Vader")
        self.assertEqual(planet, "Tatooine")
        self.assertEqual(species, "Human")
        self.assertEqual(des, "some description")
        self.assertEqual(image, "some url")
        self.assertEqual(gender, "Male")
        self.assertEqual(birth, "41.9 BBY")
        self.assertEqual(height, "2.02 meters")

    def test_get_all_characters_name(self) :
        characters = m.Character.get_all()
        char_name = [characters[i].name for i in range(len(characters))]
        expected = ['Boba Fett', 'Chewbacca', 'Darth Vader', 'Ahsoka Tano']

        # comparing the two list elements ignoring order
        result = not set(char_name).isdisjoint(expected)

        self.assertEqual(result, True)

    def test_get_all_characters_planet(self) :
        characters = m.Character.get_all()
        char_planet = [characters[i].planet for i in range(len(characters))]
        expected = ['Kamino', 'Kashyyyk', 'Tatooine', 'Shili']

        # comparing the two list elements ignoring order
        result = not set(char_planet).isdisjoint(expected)

        self.assertEqual(result, True)

    def test_get_all_characters_species(self) :
        characters = m.Character.get_all()
        char_species = [characters[i].species for i in range(len(characters))]
        expected = ['Human', 'Wookiee', 'Human', 'Togruta']

        # comparing the two list elements ignoring order
        result = not set(char_species).isdisjoint(expected)

        self.assertEqual(result, True)

    def test_get_all_characters_gender(self) :
        characters = m.Character.get_all()
        char_genders = [characters[i].gender for i in range(len(characters))]
        expected = ['Male', 'Male', 'Male', 'Female']
    
        # comparing the two list elements ignoring order
        result = not set(char_genders).isdisjoint(expected)

        self.assertEqual(result, True)

    def test_get_all_characters_height(self) :
        characters = m.Character.get_all()
        char_height = [characters[i].height for i in range(len(characters))]
        expected = ['1.83 meters', '2.28 meters', '2.02 meters', '1.61 meters']
        
        # comparing the two list elements ignoring order
        result = not set(char_height).isdisjoint(expected)

        self.assertEqual(result, True)

    def test_get_character_2(self) :
        c = m.Character.get("Boba Fett")

        self.assertEqual(c.name, "Boba Fett")
        self.assertEqual(c.planet, "Kamino")
        self.assertEqual(c.species, "Human")
        self.assertEqual(c.description, "Boba Fett was a Mandalorian warrior and bounty hunter. He was the only unaltered clone of the famed Jango Fett, created in 32 BBY as unit A0050, one of the first of many Fett replicas designed to become part of the Grand Army of the Republic, and was raised as Jango's son. Jango taught Boba much, training him to become a skilled bounty hunter as was his father-figure before him. In 22 BBY, Jango was killed at the Battle of Geonosis, which opened the Clone Wars. Just a boy, Boba was forced to grow up and took to traveling the galaxy. Later, he became a bounty hunter and took assignments from beings such as Jabba the Hutt, and achieved notoriety despite his young age.")
        self.assertEqual(c.image, "http://img4.wikia.nocookie.net/__cb20130920001614/starwars/images/thumb/5/58/BobaFettMain2.jpg/400px-BobaFettMain2.jpg")
        self.assertEqual(c.gender, "Male")
        self.assertEqual(c.birth, "31.5 BBY , Kamino")
        self.assertEqual(c.height, "1.83 meters")

    def test_get_character_3(self) :
        c = m.Character.get("Chewbacca")

        self.assertEqual(c.name, "Chewbacca")
        self.assertEqual(c.planet, "Kashyyyk")
        self.assertEqual(c.species, "Wookiee")
        self.assertEqual(c.description, "Chewbacca (or \"Chewie\", as he was known by his friends) was a legendary Wookiee from Kashyyyk and co-pilot of Han Solo's ship, the Millennium Falcon. He was the son of Attichitcuk, the husband of Mallatobuck, and the father of Lumpawaroo. Chewbacca carried with him the name of an ancient Wookiee hero, the great Bacca, first of the great chieftains of Kashyyyk, and the creator of a sword that denoted leadership among the Wookiees. This name placed Chewbacca in a noble lineage, which was further supported by his role in the Battle of Kashyyyk during the Clone Wars and during the Galactic Civil War.")
        self.assertEqual(c.image, "http://img4.wikia.nocookie.net/__cb20080815045819/starwars/images/thumb/7/73/Chewbaccaheadshot.jpg/400px-Chewbaccaheadshot.jpg")
        self.assertEqual(c.gender, "Male")
        self.assertEqual(c.birth, "200 BBY, Kashyyyk")
        self.assertEqual(c.height, "2.28 meters")

    # ------
    # planet
    # ------

    def test_planet_1 (self) :
        p = m.Planet(name="Tatooine", description="some description", image="some url", region="Outer Rim Territories", system="Tatoo system")
        name = p.name
        characters = p.get_characters()
        species = p.get_species()
        des = p.description
        image = p.image
        region = p.region
        system = p.system
        
        self.assertEqual(name, "Tatooine")
        self.assertEqual(characters, ["Darth Vader",])
        self.assertEqual(species, "Human")
        self.assertEqual(des, "some description")
        self.assertEqual(image, "some url")
        self.assertEqual(region, "Outer Rim Territories")
        self.assertEqual(system, "Tatoo system")

    def test_planet_2 (self) :
        p = m.Planet(name="Kamino", description="some description", image="some url", region="Wild Space", system="Kamino system")
        name = p.name
        characters = p.get_characters()
        species = p.get_species()
        des = p.description
        image = p.image
        region = p.region
        system = p.system
        
        self.assertEqual(name, "Kamino")
        self.assertEqual(characters, ["Boba Fett",])
        self.assertEqual(species, "Human")
        self.assertEqual(des, "some description")
        self.assertEqual(image, "some url")
        self.assertEqual(region, "Wild Space")
        self.assertEqual(system, "Kamino system")

    def test_planet_3 (self) :
        p = m.Planet(name="Kashyyyk", description="some description", image="some url", region="Mid Rim", system="Kashyyyk system")
        name = p.name
        characters = p.get_characters()
        species = p.get_species()
        des = p.description
        image = p.image
        region = p.region
        system = p.system
        
        self.assertEqual(name, "Kashyyyk")
        self.assertEqual(characters, ["Chewbacca",])
        self.assertEqual(species, "Wookiee")
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

    def test_planet_1(self) :
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


    def test_planet_2(self) :
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
        self.assertEqual(str(species), '[]')
        #self.assertEqual(des, "Kashyyyk (see pronunciation), also known as Wookiee Planet C, Edean, G5-623, and Wookiee World, was a Mid Rim planet. It was the lush, wroshyr tree-filled home world of the Wookiees. It was a member of the Galactic Republic, endured enslavement under the Galactic Empire, and later joined the New Republic.")
        self.assertEqual(image, "http://img3.wikia.nocookie.net/__cb20130202022903/starwars/images/e/e8/Can-cell_kashyyyk.png")
        self.assertEqual(region, "Mid Rim")
        self.assertEqual(system, "Kashyyyk system")

    def test_planet_3(self) :
        p = m.Planet.get("Tatooine")
        name = p.name
        characters = p.get_characters()
        species = p.get_species()
        des = p.description
        image = p.image
        region = p.region
        system = p.system

        self.assertEqual(name, "Tatooine")
        self.assertEqual(str(characters), "[<name C-3PO>, <name Biggs Darklighter>, <name Darth Vader>, <name Het Nkik>, <name Tusken Raiders>, <name Luke Skywalker>]")
        self.assertEqual(str(species), "[<name Jawa>]")
        #self.assertEqual(des, "Tatooine was a desert world and the first planet in the binary Tatoo star system. It was part of the Arkanis sector in the Outer Rim Territories. It was inhabited by poor locals who mostly farmed moisture for a living. Other activities included used equipment retailing and scrap dealing. The planet was on the 5709-DC Shipping Lane, a spur of the Triellus Trade Route, which itself connected to the Sisar Run. The planet was not far from the Corellian Run. It had its own navigation system. However, it would still play a role in galactic events, serving as the home of Anakin Skywalker. It was here that Jedi Master Qui-Gon Jinn recognized Anakin's potential to become a Jedi and where he introduced him to Obi-Wan Kenobi, his future master and mentor. Tatooine was also the home of Anakin's son, Luke, where he lived until his early adulthood. The planet acquired a bad reputation, often being viewed as the cesspool of the galaxy due to the large number of criminals who could be found there.")
        self.assertEqual(image, "http://img2.wikia.nocookie.net/__cb20130226044533/starwars/images/thumb/1/18/Tatooine3.png/500px-Tatooine3.png")
        self.assertEqual(region, "Outer Rim Territories")
        self.assertEqual(system, "Tatoo system")

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
        self.assertEqual(characters, ["<name Chewbacca>", "<name Lowbacca>"])
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
        print(set(species_char))

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

    def test_species_1 (self) :
        s = m.Species.get("Wookiee")
        name = s.name
        characters = s.get_characters()
        planet = s.planet
        des = s.description
        image = s.image
        language = s.language
        classification = s.classification

        self.assertEqual(name, "Wookiee")
        self.assertEqual(str(characters), "[<name Chewbacca, <name Lowbacca>]")
        self.assertEqual(planet, "Kashyyyk")
        self.assertEqual(language, "Shyriiwook")
        self.assertEqual(classification, "Mammal")

    def test_species_2 (self) :
        s = m.Species.get("Human")
        name = s.name
        planet = s.planet
        des = s.description
        image = s.image
        language = s.language
        classification = s.classification

        self.assertEqual(name, "Human")
        self.assertEqual(planet, "Unknown, possibly Coruscant")
        self.assertEqual(des, "Humans, taxonomically referred to as Homo sapiens, were the galaxy's most numerous and politically dominant sentient species with millions of major and minor colonies galaxywide. Believed to have originated on the galactic capital of Coruscant, they could be found anywhere, engaged in many different pursuits: spacers, mercenaries, smugglers, merchants, soldiers, assassins, farmers, crime lords, laborers, slaves, slavers, and many others, including Jedi and Sith. Since Humans were the most common sentient species, they were often considered to be a standard or average to which the biology, psychology, and culture of other species were compared.")
        self.assertEqual(image, "http://img2.wikia.nocookie.net/__cb20100628191857/starwars/images/thumb/5/5d/Humans-TESB30.jpg/400px-Humans-TESB30.jpg")
        self.assertEqual(language, "Galactic Basic Standard")
        self.assertEqual(classification, "Mammal")

    def test_species_3 (self) :
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
        self.assertEqual(classification, "Sentient")


# ----
# main
# ----
if __name__ == "__main__" :
    main()



