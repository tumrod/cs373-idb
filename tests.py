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
        c = Character(name="Boba Fett", species="Human", planet="Kamino", description="some description", image="some url", gender="Male", birth="31.5 BBY", height="1.83 meters")
        name = c.get_name()
        planet = c.get_planet()
        species = c.get_species()
        des = c.get_description()
        image = c.get_image()
        gender = c.get_gender()
        birth = c.get_birth()
        height = c.get_height()
        
        self.assertEqual(name, "Boba Fett")
        self.assertEqual(planet, "Kamino")
        self.assertEqual(species, "Human")
        self.assertEqual(des, "some description")
        self.assertEqual(image, "some url")
        self.assertEqual(gender, "Male")
        self.assertEqual(birth, "31.5 BBY")
        self.assertEqual(height, "1.83 meters")

    def test_character_2 (self) :
        c = Character(name="Chewbacca", species="Wookiee", planet="Kashyyyk", description="some description", image="some url", gender="Male", birth="200 BBY", height="2.28 meters")
        name = c.get_name()
        planet = c.get_planet()
        species = c.get_species()
        des = c.get_description()
        image = c.get_image()
        gender = c.get_gender()
        birth = c.get_birth()
        height = c.get_height()
        
        self.assertEqual(name, "Chewbacca")
        self.assertEqual(planet, "Kashyyyk")
        self.assertEqual(species, "Wookiee")
        self.assertEqual(des, "some description")
        self.assertEqual(image, "some url")
        self.assertEqual(gender, "Male")
        self.assertEqual(birth, "200 BBY")
        self.assertEqual(height, "2.28 meters")

    def test_character_3 (self) :
        c = Character(name="Darth Vader", species="Human", planet="Tatooine", description="some description", image="some url", gender="Male", birth="41.9 BBY", height="2.02 meters")
        name = c.get_name()
        planet = c.get_planet()
        species = c.get_species()
        des = c.get_description()
        image = c.get_image()
        gender = c.get_gender()
        birth = c.get_birth()
        height = c.get_height()
        
        self.assertEqual(name, "Darth Vader")
        self.assertEqual(planet, "Tatooine")
        self.assertEqual(species, "Human")
        self.assertEqual(des, "some description")
        self.assertEqual(image, "some url")
        self.assertEqual(gender, "Male")
        self.assertEqual(birth, "41.9 BBY")
        self.assertEqual(height, "2.02 meters")

    def test_get_all_characters_1(self) :
        characters = Character.get_all_characters()
        c = characters[1]

        self.assertEqual(c["name"], "Boba Fett")
        self.assertEqual(c["planet"], "Kamino")
        self.assertEqual(c["species"], "Human")
        self.assertEqual(c["description"], "Boba Fett was a Mandalorian warrior and bounty hunter. He was the only unaltered clone of the famed Jango Fett, created in 32 BBY as unit A0050, one of the first of many Fett replicas designed to become part of the Grand Army of the Republic, and was raised as Jango's son. Jango taught Boba much, training him to become a skilled bounty hunter as was his father-figure before him. In 22 BBY, Jango was killed at the Battle of Geonosis, which opened the Clone Wars. Just a boy, Boba was forced to grow up and took to traveling the galaxy. Later, he became a bounty hunter and took assignments from beings such as Jabba the Hutt, and achieved notoriety despite his young age.")
        self.assertEqual(c["image"], "http:\/\/img4.wikia.nocookie.net\/__cb20130920001614\/starwars\/images\/thumb\/5\/58\/BobaFettMain2.jpg\/400px-BobaFettMain2.jpg")
        self.assertEqual(c["gender"], "Male")
        self.assertEqual(c["birth"], "31.5 BBY , Kamino")
        self.assertEqual(c["height"], "1.83 meters")


    def test_get_all_characters_2(self) :
        characters = Character.get_all_characters()
        c = characters[0]

        self.assertEqual(c["name"], "Ahsoka Tano")
        self.assertEqual(c["planet"], "Shili")
        self.assertEqual(c["species"], "Toqruta")
        self.assertEqual(c["description"], "Ahsoka Tano, nicknamed Snips by her master, was a Togruta female from the planet Shili who trained as a Jedi apprentice during the Clone Wars, the conflict between the Galactic Republic and the Confederacy of Independent Systems. Tano was assigned to Jedi Knight Anakin Skywalker by Jedi Grand Master Yoda, and she demonstrated an eagerness to prove herself worthy to be his apprentice. Tano was involved in the defeat of the Separatist army on the planet Christophsis and was important to Republic efforts during the Battle of Teth. Along with Skywalker, Tano was instrumental in acquiring the Republic's safe passage through Hutt Space, due to her part in rescuing the son of Jabba the Hutt, which ensured an alliance between the Republic and the Hutt clans.")
        self.assertEqual(c["image"], "http://img1.wikia.nocookie.net/__cb20121211040147/starwars/images/0/03/AhsokaHS-AFiN.png")
        self.assertEqual(c["gender"], "Female")
        self.assertEqual(c["birth"], "21 BBY ")
        self.assertEqual(c["height"], "1.61 meters")

    def test_get_all_characters_3(self) :
        characters = Character.get_all_characters()
        c = characters[2]

        self.assertEqual(c["name"], "Chewbacca")
        self.assertEqual(c["planet"], "Kashyyyk")
        self.assertEqual(c["species"], "Wookiee")
        self.assertEqual(c["description"], "Chewbacca (or \"Chewie\", as he was known by his friends) was a legendary Wookiee from Kashyyyk and co-pilot of Han Solo's ship, the Millennium Falcon. He was the son of Attichitcuk, the husband of Mallatobuck, and the father of Lumpawaroo. Chewbacca carried with him the name of an ancient Wookiee hero, the great Bacca, first of the great chieftains of Kashyyyk, and the creator of a sword that denoted leadership among the Wookiees. This name placed Chewbacca in a noble lineage, which was further supported by his role in the Battle of Kashyyyk during the Clone Wars and during the Galactic Civil War.")
        self.assertEqual(c["image"], "http:\/\/img4.wikia.nocookie.net\/__cb20080815045819\/starwars\/images\/thumb\/7\/73\/Chewbaccaheadshot.jpg\/400px-Chewbaccaheadshot.jpg")
        self.assertEqual(c["gender"], "Male")
        self.assertEqual(c["birth"], "200 BBY, Kashyyyk")
        self.assertEqual(c["height"], "2.28 meters")

    def test_get_all_characters_4(self) :
        characters = Character.get_all_characters()
        c = characters[3]

        self.assertEqual(c["name"], "Darth Vader")
        self.assertEqual(c["planet"], "Tatooine")
        self.assertEqual(c["species"], "Human")
        self.assertEqual(c["description"], "Anakin Skywalker was a Force-sensitive Human male who served the Galactic Republic as a Jedi Knight and later served the Galactic Empire as the Sith Lord Darth Vader. Born to the slave Shmi Skywalker in 41.9 BBY, Anakin was conceived by midi-chlorians, the symbiotic organisms that allowed individuals to touch the Force, and he and his mother were brought to the desert planet of Tatooine to be the slaves of Gardulla the Hutt. They soon ended up as the property of the Toydarian Watto, and Skywalker exhibited exceptional piloting skills and a reputation for being able to build and repair anything even at a young age. In 32 BBY, Skywalker encountered the Jedi Qui-Gon Jinn and Padmé Amidala, and he helped them secure the parts they needed for their starship by winning the Boonta Eve Classic podracing event—only to learn that he had also won his freedom in doing so.")
        self.assertEqual(c["image"], "http:\/\/img2.wikia.nocookie.net\/__cb20130621175844\/starwars\/images\/thumb\/6\/6f\/Anakin_Skywalker_RotS.png\/400px-Anakin_Skywalker_RotS.webp")
        self.assertEqual(c["gender"], "Male")
        self.assertEqual(c["birth"], "41.9 BBY ")
        self.assertEqual(c["height"], "2.02 meters")

    # ------
    # planet
    # ------

    def test_planet_1 (self) :
        p = Planet(name="Tatooine", species="Human", characters=["Darth Vader"], description="some description", image="some url", region="Outer Rim Territories", system="Tatoo system")
        name = p.get_name()
        characters = p.get_characters()
        species = p.get_species()
        des = p.get_description()
        image = p.get_image()
        region = p.get_region()
        system = p.get_system()
        
        self.assertEqual(name, "Tatooine")
        self.assertEqual(characters, ["Darth Vader",])
        self.assertEqual(species, "Human")
        self.assertEqual(des, "some description")
        self.assertEqual(image, "some url")
        self.assertEqual(region, "Outer Rim Territories")
        self.assertEqual(system, "Tatoo system")

    def test_planet_2 (self) :
        p = Planet(name="Kamino", species="Human", characters=["Boba Fett"], description="some description", image="some url", region="Wild Space", system="Kamino system")
        name = p.get_name()
        characters = p.get_characters()
        species = p.get_species()
        des = p.get_description()
        image = p.get_image()
        region = p.get_region()
        system = p.get_system()
        
        self.assertEqual(name, "Kamino")
        self.assertEqual(characters, ["Boba Fett",])
        self.assertEqual(species, "Human")
        self.assertEqual(des, "some description")
        self.assertEqual(image, "some url")
        self.assertEqual(region, "Wild Space")
        self.assertEqual(system, "Kamino system")

    def test_planet_3 (self) :
        p = Planet(name="Kashyyyk", species="Wookiee", characters=["Chewbacca"], description="some description", image="some url", region="Mid Rim", system="Kashyyyk system")
        name = p.get_name()
        characters = p.get_characters()
        species = p.get_species()
        des = p.get_description()
        image = p.get_image()
        region = p.get_region()
        system = p.get_system()
        
        self.assertEqual(name, "Kashyyyk")
        self.assertEqual(characters, ["Chewbacca",])
        self.assertEqual(species, "Wookiee")
        self.assertEqual(des, "some description")
        self.assertEqual(image, "some url")
        self.assertEqual(region, "Mid Rim")
        self.assertEqual(system, "Kashyyyk system")

    # --------
    # species
    # --------

    def test_species_1 (self) :
        s = Species(name="Wookiee", planet="Kashyyyk", characters="Chewbacca", description="some description", image="some url", language="Shyriiwook", classification="Mammal")
        name = s.get_name()
        characters = s.get_characters()
        planet = s.get_planet()
        des = s.get_description()
        image = s.get_image()
        language = s.get_language()
        classification = s.get_classification()
        
        self.assertEqual(name, "Wookiee")
        self.assertEqual(characters, "Chewbacca")
        self.assertEqual(planet, "Kashyyyk")
        self.assertEqual(des, "some description")
        self.assertEqual(image, "some url")
        self.assertEqual(language, "Shyriiwook")
        self.assertEqual(classification, "Mammal")

    def test_species_2 (self) :
        s = Species(name="Human", planet="Coruscant", characters=["Darth Vader", "Boba Fett"], description="some description", image="some url", language="Galactic Basic Standard", classification="Mammal")
        name = s.get_name()
        characters = s.get_characters()
        planet = s.get_planet()
        des = s.get_description()
        image = s.get_image()
        language = s.get_language()
        classification = s.get_classification()
        
        self.assertEqual(name, "Human")
        self.assertEqual(characters, ["Darth Vader", "Boba Fett",])
        self.assertEqual(planet, "Coruscant")
        self.assertEqual(des, "some description")
        self.assertEqual(image, "some url")
        self.assertEqual(language, "Galactic Basic Standard")
        self.assertEqual(classification, "Mammal")

# ----
# main
# ----
if __name__ == "__main__" :
    main()



