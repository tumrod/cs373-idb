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
        self.assertEqual(des, "Boba Fett was a Mandalorian warrior and bounty hunter. He was the only unaltered clone of the famed Jango Fett, created in 32 BBY as unit A0050, one of the first of many Fett replicas designed to become part of the Grand Army of the Republic, and was raised as Jango's son. Jango taught Boba much, training him to become a skilled bounty hunter as was his father-figure before him. In 22 BBY, Jango was killed at the Battle of Geonosis, which opened the Clone Wars. Just a boy, Boba was forced to grow up and took to traveling the galaxy. Later, he became a bounty hunter and took assignments from beings such as Jabba the Hutt, and achieved notoriety despite his young age.")
        self.assertEqual(image, "http:\/\/img4.wikia.nocookie.net\/__cb20130920001614\/starwars\/images\/thumb\/5\/58\/BobaFettMain2.jpg\/400px-BobaFettMain2.jpg")
        self.assertEqual(gender, "Male")
        self.assertEqual(birth, "31.5 BBY , Kamino")
        self.assertEqual(height, "1.83 meters")


    def test_get_all_characters_2(self) :
        characters = Character.get_all_characters()
        c = characters[0]
        name = c.get_name()
        planet = c.get_planet()
        species = c.get_species()
        des = c.get_description()
        image = c.get_image()
        gender = c.get_gender()
        birth = c.get_birth()
        height = c.get_height()

        self.assertEqual(name, "Ahsoka Tano")
        self.assertEqual(planet, "Shili")
        self.assertEqual(species, "Toqruta")
        self.assertEqual(des, "Ahsoka Tano, nicknamed Snips by her master, was a Togruta female from the planet Shili who trained as a Jedi apprentice during the Clone Wars, the conflict between the Galactic Republic and the Confederacy of Independent Systems. Tano was assigned to Jedi Knight Anakin Skywalker by Jedi Grand Master Yoda, and she demonstrated an eagerness to prove herself worthy to be his apprentice. Tano was involved in the defeat of the Separatist army on the planet Christophsis and was important to Republic efforts during the Battle of Teth. Along with Skywalker, Tano was instrumental in acquiring the Republic's safe passage through Hutt Space, due to her part in rescuing the son of Jabba the Hutt, which ensured an alliance between the Republic and the Hutt clans.")
        self.assertEqual(image, "http://img1.wikia.nocookie.net/__cb20121211040147/starwars/images/0/03/AhsokaHS-AFiN.png")
        self.assertEqual(gender, "Female")
        self.assertEqual(birth, "21 BBY ")
        self.assertEqual(height, "1.61 meters")

    def test_get_all_characters_3(self) :
        characters = Character.get_all_characters()
        c = characters[2]
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
        self.assertEqual(des, "Chewbacca (or \"Chewie\", as he was known by his friends) was a legendary Wookiee from Kashyyyk and co-pilot of Han Solo's ship, the Millennium Falcon. He was the son of Attichitcuk, the husband of Mallatobuck, and the father of Lumpawaroo. Chewbacca carried with him the name of an ancient Wookiee hero, the great Bacca, first of the great chieftains of Kashyyyk, and the creator of a sword that denoted leadership among the Wookiees. This name placed Chewbacca in a noble lineage, which was further supported by his role in the Battle of Kashyyyk during the Clone Wars and during the Galactic Civil War.")
        self.assertEqual(image, "http:\/\/img4.wikia.nocookie.net\/__cb20080815045819\/starwars\/images\/thumb\/7\/73\/Chewbaccaheadshot.jpg\/400px-Chewbaccaheadshot.jpg")
        self.assertEqual(gender, "Male")
        self.assertEqual(birth, "200 BBY, Kashyyyk")
        self.assertEqual(height, "2.28 meters")

    def test_get_all_characters_4(self) :
        characters = Character.get_all_characters()
        c = characters[3]
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
        self.assertEqual(des, "Anakin Skywalker was a Force-sensitive Human male who served the Galactic Republic as a Jedi Knight and later served the Galactic Empire as the Sith Lord Darth Vader. Born to the slave Shmi Skywalker in 41.9 BBY, Anakin was conceived by midi-chlorians, the symbiotic organisms that allowed individuals to touch the Force, and he and his mother were brought to the desert planet of Tatooine to be the slaves of Gardulla the Hutt. They soon ended up as the property of the Toydarian Watto, and Skywalker exhibited exceptional piloting skills and a reputation for being able to build and repair anything even at a young age. In 32 BBY, Skywalker encountered the Jedi Qui-Gon Jinn and Padme Amidala, and he helped them secure the parts they needed for their starship by winning the Boonta Eve Classic podracing event-only to learn that he had also won his freedom in doing so.")
        self.assertEqual(image, "http:\/\/img2.wikia.nocookie.net\/__cb20130621175844\/starwars\/images\/thumb\/6\/6f\/Anakin_Skywalker_RotS.png\/400px-Anakin_Skywalker_RotS.webp")
        self.assertEqual(gender, "Male")
        self.assertEqual(birth, "41.9 BBY ")
        self.assertEqual(height, "2.02 meters")

    def test_get_all_sorted_characters_1(self) :
        characters = Character.get_all_sorted_characters("name_^")
        c = characters[3]
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
        self.assertEqual(des, "Anakin Skywalker was a Force-sensitive Human male who served the Galactic Republic as a Jedi Knight and later served the Galactic Empire as the Sith Lord Darth Vader. Born to the slave Shmi Skywalker in 41.9 BBY, Anakin was conceived by midi-chlorians, the symbiotic organisms that allowed individuals to touch the Force, and he and his mother were brought to the desert planet of Tatooine to be the slaves of Gardulla the Hutt. They soon ended up as the property of the Toydarian Watto, and Skywalker exhibited exceptional piloting skills and a reputation for being able to build and repair anything even at a young age. In 32 BBY, Skywalker encountered the Jedi Qui-Gon Jinn and Padme Amidala, and he helped them secure the parts they needed for their starship by winning the Boonta Eve Classic podracing event-only to learn that he had also won his freedom in doing so.")
        self.assertEqual(image, "http:\/\/img2.wikia.nocookie.net\/__cb20130621175844\/starwars\/images\/thumb\/6\/6f\/Anakin_Skywalker_RotS.png\/400px-Anakin_Skywalker_RotS.webp")
        self.assertEqual(gender, "Male")
        self.assertEqual(birth, "41.9 BBY ")
        self.assertEqual(height, "2.02 meters")

    def test_get_all_sorted_characters_2(self) :
        characters = Character.get_all_sorted_characters("planet")
        c = characters[3]
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
        self.assertEqual(des, "Anakin Skywalker was a Force-sensitive Human male who served the Galactic Republic as a Jedi Knight and later served the Galactic Empire as the Sith Lord Darth Vader. Born to the slave Shmi Skywalker in 41.9 BBY, Anakin was conceived by midi-chlorians, the symbiotic organisms that allowed individuals to touch the Force, and he and his mother were brought to the desert planet of Tatooine to be the slaves of Gardulla the Hutt. They soon ended up as the property of the Toydarian Watto, and Skywalker exhibited exceptional piloting skills and a reputation for being able to build and repair anything even at a young age. In 32 BBY, Skywalker encountered the Jedi Qui-Gon Jinn and Padme Amidala, and he helped them secure the parts they needed for their starship by winning the Boonta Eve Classic podracing event-only to learn that he had also won his freedom in doing so.")
        self.assertEqual(image, "http:\/\/img2.wikia.nocookie.net\/__cb20130621175844\/starwars\/images\/thumb\/6\/6f\/Anakin_Skywalker_RotS.png\/400px-Anakin_Skywalker_RotS.webp")
        self.assertEqual(gender, "Male")
        self.assertEqual(birth, "41.9 BBY ")
        self.assertEqual(height, "2.02 meters")

    def test_get_all_sorted_characters_3(self) :
        characters = Character.get_all_sorted_characters("species")
        c = characters[1]
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
        self.assertEqual(des, "Anakin Skywalker was a Force-sensitive Human male who served the Galactic Republic as a Jedi Knight and later served the Galactic Empire as the Sith Lord Darth Vader. Born to the slave Shmi Skywalker in 41.9 BBY, Anakin was conceived by midi-chlorians, the symbiotic organisms that allowed individuals to touch the Force, and he and his mother were brought to the desert planet of Tatooine to be the slaves of Gardulla the Hutt. They soon ended up as the property of the Toydarian Watto, and Skywalker exhibited exceptional piloting skills and a reputation for being able to build and repair anything even at a young age. In 32 BBY, Skywalker encountered the Jedi Qui-Gon Jinn and Padme Amidala, and he helped them secure the parts they needed for their starship by winning the Boonta Eve Classic podracing event-only to learn that he had also won his freedom in doing so.")
        self.assertEqual(image, "http:\/\/img2.wikia.nocookie.net\/__cb20130621175844\/starwars\/images\/thumb\/6\/6f\/Anakin_Skywalker_RotS.png\/400px-Anakin_Skywalker_RotS.webp")
        self.assertEqual(gender, "Male")
        self.assertEqual(birth, "41.9 BBY ")
        self.assertEqual(height, "2.02 meters")

    def test_get_all_sorted_characters_4(self) :
        characters = Character.get_all_sorted_characters("height")
        c = characters[2]
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
        self.assertEqual(des, "Anakin Skywalker was a Force-sensitive Human male who served the Galactic Republic as a Jedi Knight and later served the Galactic Empire as the Sith Lord Darth Vader. Born to the slave Shmi Skywalker in 41.9 BBY, Anakin was conceived by midi-chlorians, the symbiotic organisms that allowed individuals to touch the Force, and he and his mother were brought to the desert planet of Tatooine to be the slaves of Gardulla the Hutt. They soon ended up as the property of the Toydarian Watto, and Skywalker exhibited exceptional piloting skills and a reputation for being able to build and repair anything even at a young age. In 32 BBY, Skywalker encountered the Jedi Qui-Gon Jinn and Padme Amidala, and he helped them secure the parts they needed for their starship by winning the Boonta Eve Classic podracing event-only to learn that he had also won his freedom in doing so.")
        self.assertEqual(image, "http:\/\/img2.wikia.nocookie.net\/__cb20130621175844\/starwars\/images\/thumb\/6\/6f\/Anakin_Skywalker_RotS.png\/400px-Anakin_Skywalker_RotS.webp")
        self.assertEqual(gender, "Male")
        self.assertEqual(birth, "41.9 BBY ")
        self.assertEqual(height, "2.02 meters")

    def test_get_character_1(self) :
        c = Character.get_character("Darth Vader")

        self.assertEqual(c.get_name(), "Darth Vader")
        self.assertEqual(c.get_planet(), "Tatooine")
        self.assertEqual(c.get_species(), "Human")
        self.assertEqual(c.get_description(), "Anakin Skywalker was a Force-sensitive Human male who served the Galactic Republic as a Jedi Knight and later served the Galactic Empire as the Sith Lord Darth Vader. Born to the slave Shmi Skywalker in 41.9 BBY, Anakin was conceived by midi-chlorians, the symbiotic organisms that allowed individuals to touch the Force, and he and his mother were brought to the desert planet of Tatooine to be the slaves of Gardulla the Hutt. They soon ended up as the property of the Toydarian Watto, and Skywalker exhibited exceptional piloting skills and a reputation for being able to build and repair anything even at a young age. In 32 BBY, Skywalker encountered the Jedi Qui-Gon Jinn and Padme Amidala, and he helped them secure the parts they needed for their starship by winning the Boonta Eve Classic podracing event-only to learn that he had also won his freedom in doing so.")
        self.assertEqual(c.get_image(), "http:\/\/img2.wikia.nocookie.net\/__cb20130621175844\/starwars\/images\/thumb\/6\/6f\/Anakin_Skywalker_RotS.png\/400px-Anakin_Skywalker_RotS.webp")
        self.assertEqual(c.get_gender(), "Male")
        self.assertEqual(c.get_birth(), "41.9 BBY ")
        self.assertEqual(c.get_height(), "2.02 meters")

    def test_get_character_2(self) :
        c = Character.get_character("Boba Fett")

        self.assertEqual(c.get_name(), "Boba Fett")
        self.assertEqual(c.get_planet(), "Kamino")
        self.assertEqual(c.get_species(), "Human")
        self.assertEqual(c.get_description(), "Boba Fett was a Mandalorian warrior and bounty hunter. He was the only unaltered clone of the famed Jango Fett, created in 32 BBY as unit A0050, one of the first of many Fett replicas designed to become part of the Grand Army of the Republic, and was raised as Jango's son. Jango taught Boba much, training him to become a skilled bounty hunter as was his father-figure before him. In 22 BBY, Jango was killed at the Battle of Geonosis, which opened the Clone Wars. Just a boy, Boba was forced to grow up and took to traveling the galaxy. Later, he became a bounty hunter and took assignments from beings such as Jabba the Hutt, and achieved notoriety despite his young age.")
        self.assertEqual(c.get_image(), "http:\/\/img4.wikia.nocookie.net\/__cb20130920001614\/starwars\/images\/thumb\/5\/58\/BobaFettMain2.jpg\/400px-BobaFettMain2.jpg")
        self.assertEqual(c.get_gender(), "Male")
        self.assertEqual(c.get_birth(), "31.5 BBY , Kamino")
        self.assertEqual(c.get_height(), "1.83 meters")

    def test_get_character_3(self) :
        c = Character.get_character("Chewbacca")

        self.assertEqual(c.get_name(), "Chewbacca")
        self.assertEqual(c.get_planet(), "Kashyyyk")
        self.assertEqual(c.get_species(), "Wookiee")
        self.assertEqual(c.get_description(), "Chewbacca (or \"Chewie\", as he was known by his friends) was a legendary Wookiee from Kashyyyk and co-pilot of Han Solo's ship, the Millennium Falcon. He was the son of Attichitcuk, the husband of Mallatobuck, and the father of Lumpawaroo. Chewbacca carried with him the name of an ancient Wookiee hero, the great Bacca, first of the great chieftains of Kashyyyk, and the creator of a sword that denoted leadership among the Wookiees. This name placed Chewbacca in a noble lineage, which was further supported by his role in the Battle of Kashyyyk during the Clone Wars and during the Galactic Civil War.")
        self.assertEqual(c.get_image(), "http:\/\/img4.wikia.nocookie.net\/__cb20080815045819\/starwars\/images\/thumb\/7\/73\/Chewbaccaheadshot.jpg\/400px-Chewbaccaheadshot.jpg")
        self.assertEqual(c.get_gender(), "Male")
        self.assertEqual(c.get_birth(), "200 BBY, Kashyyyk")
        self.assertEqual(c.get_height(), "2.28 meters")

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
        
    def test_get_all_planets_1(self) :
        planets = Planet.get_all_planets()
        p = planets[1]
        name = p.get_name()
        characters = p.get_characters()
        species = p.get_species()
        des = p.get_description()
        image = p.get_image()
        region = p.get_region()
        system = p.get_system()

        self.assertEqual(name, "Kamino")
        self.assertEqual(characters, ["Boba Fett"])
        self.assertEqual(species, "Human")
        self.assertEqual(des, "Kamino, also known as the Planet of Storms,[10] was the watery world where the Clone Army of the Galactic Republic was created, as well as the Kamino Home Fleet. It was inhabited by a race of tall, elegant beings called the Kaminoans, who kept to themselves and were known for their cloning technology. Kamino was located just south of the Rishi Maze, and was governed by the Ruling Council, headed by the Prime Minister.")
        self.assertEqual(image, "http:\/\/img2.wikia.nocookie.net\/__cb20090527045541\/starwars\/images\/thumb\/a\/a9\/Eaw_Kamino.jpg\/400px-Eaw_Kamino.jpg")
        self.assertEqual(region, "Wild Space")
        self.assertEqual(system, "Kamino system")


    def test_get_all_planets_2(self) :
        planets = Planet.get_all_planets()
        p = planets[2]
        name = p.get_name()
        characters = p.get_characters()
        species = p.get_species()
        des = p.get_description()
        image = p.get_image()
        region = p.get_region()
        system = p.get_system()

        self.assertEqual(name, "Kashyyyk")
        self.assertEqual(characters, ["Chewbacca"])
        self.assertEqual(species, "Wookiee")
        self.assertEqual(des, "Kashyyyk (see pronunciation), also known as Wookiee Planet C, Edean, G5-623, and Wookiee World, was a Mid Rim planet. It was the lush, wroshyr tree-filled home world of the Wookiees. It was a member of the Galactic Republic, endured enslavement under the Galactic Empire, and later joined the New Republic.")
        self.assertEqual(image, "http:\/\/img1.wikia.nocookie.net\/__cb20090327122712\/starwars\/images\/6\/69\/Kasyyykunleashed.jpg")
        self.assertEqual(region, "Mid Rim")
        self.assertEqual(system, "Kashyyyk system")

    def test_get_all_planets_3(self) :
        planets = Planet.get_all_planets()
        p = planets[0]
        name = p.get_name()
        characters = p.get_characters()
        species = p.get_species()
        des = p.get_description()
        image = p.get_image()
        region = p.get_region()
        system = p.get_system()

        self.assertEqual(name, "Coruscant")
        self.assertEqual(characters, [])
        self.assertEqual(species, "Human")
        self.assertEqual(des, "Coruscant, originally called Notron, also known as Imperial Center or the Queen of the Core, was a planet located in the Galactic Core. It was generally agreed that Coruscant was, during most of galactic history, the most politically important world in the galaxy. At various times, it was the capital of the Galactic Republic, the Galactic Empire, the New Republic, the Yuuzhan Vong empire, the Galactic Alliance, very briefly the Fel Empire, Darth Krayt's Galactic Empire, and the Galactic Federation Triumvirate. In controlling Coruscant, these governments controlled most of the galaxy in the process.")
        self.assertEqual(image, "http://img4.wikia.nocookie.net/__cb20100115192302/starwars/images/1/17/Coruscant-AoTCW.jpg")
        self.assertEqual(region, "Core Worlds")
        self.assertEqual(system, "Coruscant system")

    def test_get_all_planets_4(self) :
        planets = Planet.get_all_planets()
        p = planets[3]
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
        self.assertEqual(des, "Tatooine was a desert world and the first planet in the binary Tatoo star system. It was part of the Arkanis sector in the Outer Rim Territories. It was inhabited by poor locals who mostly farmed moisture for a living. Other activities included used equipment retailing and scrap dealing. The planet was on the 5709-DC Shipping Lane, a spur of the Triellus Trade Route, which itself connected to the Sisar Run. The planet was not far from the Corellian Run. It had its own navigation system. However, it would still play a role in galactic events, serving as the home of Anakin Skywalker. It was here that Jedi Master Qui-Gon Jinn recognized Anakin's potential to become a Jedi and where he introduced him to Obi-Wan Kenobi, his future master and mentor. Tatooine was also the home of Anakin's son, Luke, where he lived until his early adulthood. The planet acquired a bad reputation, often being viewed as the cesspool of the galaxy due to the large number of criminals who could be found there.")
        self.assertEqual(image, "http:\/\/img2.wikia.nocookie.net\/__cb20131019121937\/starwars\/images\/b\/b0\/Tatooine_TPM.png")
        self.assertEqual(region, "Outer Rim Territories")
        self.assertEqual(system, "Tatoo system")

    def test_get_all_sorted_planets_1(self) :
        planets = Planet.get_all_sorted_planets("name")
        p = planets[3]
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
        self.assertEqual(des, "Tatooine was a desert world and the first planet in the binary Tatoo star system. It was part of the Arkanis sector in the Outer Rim Territories. It was inhabited by poor locals who mostly farmed moisture for a living. Other activities included used equipment retailing and scrap dealing. The planet was on the 5709-DC Shipping Lane, a spur of the Triellus Trade Route, which itself connected to the Sisar Run. The planet was not far from the Corellian Run. It had its own navigation system. However, it would still play a role in galactic events, serving as the home of Anakin Skywalker. It was here that Jedi Master Qui-Gon Jinn recognized Anakin's potential to become a Jedi and where he introduced him to Obi-Wan Kenobi, his future master and mentor. Tatooine was also the home of Anakin's son, Luke, where he lived until his early adulthood. The planet acquired a bad reputation, often being viewed as the cesspool of the galaxy due to the large number of criminals who could be found there.")
        self.assertEqual(image, "http:\/\/img2.wikia.nocookie.net\/__cb20131019121937\/starwars\/images\/b\/b0\/Tatooine_TPM.png")
        self.assertEqual(region, "Outer Rim Territories")
        self.assertEqual(system, "Tatoo system")

    def test_get_all_sorted_planets_2(self) :
        planets = Planet.get_all_sorted_planets("region")
        p = planets[2]
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
        self.assertEqual(des, "Tatooine was a desert world and the first planet in the binary Tatoo star system. It was part of the Arkanis sector in the Outer Rim Territories. It was inhabited by poor locals who mostly farmed moisture for a living. Other activities included used equipment retailing and scrap dealing. The planet was on the 5709-DC Shipping Lane, a spur of the Triellus Trade Route, which itself connected to the Sisar Run. The planet was not far from the Corellian Run. It had its own navigation system. However, it would still play a role in galactic events, serving as the home of Anakin Skywalker. It was here that Jedi Master Qui-Gon Jinn recognized Anakin's potential to become a Jedi and where he introduced him to Obi-Wan Kenobi, his future master and mentor. Tatooine was also the home of Anakin's son, Luke, where he lived until his early adulthood. The planet acquired a bad reputation, often being viewed as the cesspool of the galaxy due to the large number of criminals who could be found there.")
        self.assertEqual(image, "http:\/\/img2.wikia.nocookie.net\/__cb20131019121937\/starwars\/images\/b\/b0\/Tatooine_TPM.png")
        self.assertEqual(region, "Outer Rim Territories")
        self.assertEqual(system, "Tatoo system")

    def test_get_all_sorted_planets_3(self) :
        planets = Planet.get_all_sorted_planets("system")
        p = planets[3]
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
        self.assertEqual(des, "Tatooine was a desert world and the first planet in the binary Tatoo star system. It was part of the Arkanis sector in the Outer Rim Territories. It was inhabited by poor locals who mostly farmed moisture for a living. Other activities included used equipment retailing and scrap dealing. The planet was on the 5709-DC Shipping Lane, a spur of the Triellus Trade Route, which itself connected to the Sisar Run. The planet was not far from the Corellian Run. It had its own navigation system. However, it would still play a role in galactic events, serving as the home of Anakin Skywalker. It was here that Jedi Master Qui-Gon Jinn recognized Anakin's potential to become a Jedi and where he introduced him to Obi-Wan Kenobi, his future master and mentor. Tatooine was also the home of Anakin's son, Luke, where he lived until his early adulthood. The planet acquired a bad reputation, often being viewed as the cesspool of the galaxy due to the large number of criminals who could be found there.")
        self.assertEqual(image, "http:\/\/img2.wikia.nocookie.net\/__cb20131019121937\/starwars\/images\/b\/b0\/Tatooine_TPM.png")
        self.assertEqual(region, "Outer Rim Territories")
        self.assertEqual(system, "Tatoo system")

    def test_get_planet_1(self) :
        p = Planet.get_planet("Kamino")
        name = p.get_name()
        characters = p.get_characters()
        species = p.get_species()
        des = p.get_description()
        image = p.get_image()
        region = p.get_region()
        system = p.get_system()

        self.assertEqual(name, "Kamino")
        self.assertEqual(characters, ["Boba Fett"])
        self.assertEqual(species, "Human")
        self.assertEqual(des, "Kamino, also known as the Planet of Storms,[10] was the watery world where the Clone Army of the Galactic Republic was created, as well as the Kamino Home Fleet. It was inhabited by a race of tall, elegant beings called the Kaminoans, who kept to themselves and were known for their cloning technology. Kamino was located just south of the Rishi Maze, and was governed by the Ruling Council, headed by the Prime Minister.")
        self.assertEqual(image, "http:\/\/img2.wikia.nocookie.net\/__cb20090527045541\/starwars\/images\/thumb\/a\/a9\/Eaw_Kamino.jpg\/400px-Eaw_Kamino.jpg")
        self.assertEqual(region, "Wild Space")
        self.assertEqual(system, "Kamino system")


    def test_get_planet_2(self) :
        p = Planet.get_planet("Kashyyyk")
        name = p.get_name()
        characters = p.get_characters()
        species = p.get_species()
        des = p.get_description()
        image = p.get_image()
        region = p.get_region()
        system = p.get_system()

        self.assertEqual(name, "Kashyyyk")
        self.assertEqual(characters, ["Chewbacca"])
        self.assertEqual(species, "Wookiee")
        self.assertEqual(des, "Kashyyyk (see pronunciation), also known as Wookiee Planet C, Edean, G5-623, and Wookiee World, was a Mid Rim planet. It was the lush, wroshyr tree-filled home world of the Wookiees. It was a member of the Galactic Republic, endured enslavement under the Galactic Empire, and later joined the New Republic.")
        self.assertEqual(image, "http:\/\/img1.wikia.nocookie.net\/__cb20090327122712\/starwars\/images\/6\/69\/Kasyyykunleashed.jpg")
        self.assertEqual(region, "Mid Rim")
        self.assertEqual(system, "Kashyyyk system")

    def test_get_planet_3(self) :
        p = Planet.get_planet("Coruscant")
        name = p.get_name()
        characters = p.get_characters()
        species = p.get_species()
        des = p.get_description()
        image = p.get_image()
        region = p.get_region()
        system = p.get_system()

        self.assertEqual(name, "Coruscant")
        self.assertEqual(characters, [])
        self.assertEqual(species, "Human")
        self.assertEqual(des, "Coruscant, originally called Notron, also known as Imperial Center or the Queen of the Core, was a planet located in the Galactic Core. It was generally agreed that Coruscant was, during most of galactic history, the most politically important world in the galaxy. At various times, it was the capital of the Galactic Republic, the Galactic Empire, the New Republic, the Yuuzhan Vong empire, the Galactic Alliance, very briefly the Fel Empire, Darth Krayt's Galactic Empire, and the Galactic Federation Triumvirate. In controlling Coruscant, these governments controlled most of the galaxy in the process.")
        self.assertEqual(image, "http://img4.wikia.nocookie.net/__cb20100115192302/starwars/images/1/17/Coruscant-AoTCW.jpg")
        self.assertEqual(region, "Core Worlds")
        self.assertEqual(system, "Coruscant system")

    def test_get_planet_4(self) :
        p = Planet.get_planet("Tatooine")
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
        self.assertEqual(des, "Tatooine was a desert world and the first planet in the binary Tatoo star system. It was part of the Arkanis sector in the Outer Rim Territories. It was inhabited by poor locals who mostly farmed moisture for a living. Other activities included used equipment retailing and scrap dealing. The planet was on the 5709-DC Shipping Lane, a spur of the Triellus Trade Route, which itself connected to the Sisar Run. The planet was not far from the Corellian Run. It had its own navigation system. However, it would still play a role in galactic events, serving as the home of Anakin Skywalker. It was here that Jedi Master Qui-Gon Jinn recognized Anakin's potential to become a Jedi and where he introduced him to Obi-Wan Kenobi, his future master and mentor. Tatooine was also the home of Anakin's son, Luke, where he lived until his early adulthood. The planet acquired a bad reputation, often being viewed as the cesspool of the galaxy due to the large number of criminals who could be found there.")
        self.assertEqual(image, "http:\/\/img2.wikia.nocookie.net\/__cb20131019121937\/starwars\/images\/b\/b0\/Tatooine_TPM.png")
        self.assertEqual(region, "Outer Rim Territories")
        self.assertEqual(system, "Tatoo system")

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

    def test_get_all_species_1 (self) :
        species = Species.get_all_species()
        s = species[0]
        name = s.get_name()
        characters = s.get_characters()
        planet = s.get_planet()
        des = s.get_description()
        image = s.get_image()
        language = s.get_language()
        classification = s.get_classification()

        self.assertEqual(name, "Bith")
        self.assertEqual(characters, [
            "Unaw Aharo",
            "Darth Tenebrous",
            "Thalleus Tharn",
            "Darth Venamis"
        ])
        self.assertEqual(planet, "Bith")
        self.assertEqual(des, "Large cranium\nAcute senses of smell and hearing")
        self.assertEqual(image, "http://img4.wikia.nocookie.net/__cb20060903181845/starwars/images/7/74/Bith_%28Doikk_Nats%29.jpg")
        self.assertEqual(language, "Bith")
        self.assertEqual(classification, "Craniopod")

    def test_get_all_species_2 (self) :
        species = Species.get_all_species()
        s = species[1]
        name = s.get_name()
        characters = s.get_characters()
        planet = s.get_planet()
        des = s.get_description()
        image = s.get_image()
        language = s.get_language()
        classification = s.get_classification()

        self.assertEqual(name, "Human")
        self.assertEqual(characters, ["Darth Vader", "Boba Fett"])
        self.assertEqual(planet, "Coruscant")
        self.assertEqual(des, "Humans, taxonomically referred to as Homo sapiens, were the galaxy's most numerous and politically dominant sentient species with millions of major and minor colonies galaxywide. Believed to have originated on the galactic capital of Coruscant, they could be found anywhere, engaged in many different pursuits: spacers, mercenaries, smugglers, merchants, soldiers, assassins, farmers, crime lords, laborers, slaves, slavers, and many others, including Jedi and Sith. Since Humans were the most common sentient species, they were often considered to be a standard or average to which the biology, psychology, and culture of other species were compared.")
        self.assertEqual(image, "http:\/\/img2.wikia.nocookie.net\/__cb20100628191857\/starwars\/images\/thumb\/5\/5d\/Humans-TESB30.jpg\/400px-Humans-TESB30.jpg")
        self.assertEqual(language, "Galactic Basic Standard")
        self.assertEqual(classification, "Mammal")

    def test_get_all_species_3 (self) :
        species = Species.get_all_species()
        s = species[2]
        name = s.get_name()
        characters = s.get_characters()
        planet = s.get_planet()
        des = s.get_description()
        image = s.get_image()
        language = s.get_language()
        classification = s.get_classification()

        self.assertEqual(name, "Omwati")
        self.assertEqual(characters, [
            "Aleema Finn",
            "Pillik",
            "Tannis",
            "Tiu Zax"
        ])
        self.assertEqual(planet, "Omwat")
        self.assertEqual(des, "Bird-like anthropoids")
        self.assertEqual(image, "http://img1.wikia.nocookie.net/__cb20070528041553/starwars/images/thumb/2/2f/Omwati.JPG/360px-Omwati.JPG")
        self.assertEqual(language, "Omwatese")
        self.assertEqual(classification, "Near-Human")

    def test_get_all_sorted_species_1 (self) :
        species = Species.get_all_sorted_species("name")
        s = species[0]
        name = s.get_name()
        characters = s.get_characters()
        planet = s.get_planet()
        des = s.get_description()
        image = s.get_image()
        language = s.get_language()
        classification = s.get_classification()

        self.assertEqual(name, "Bith")
        self.assertEqual(characters, [
            "Unaw Aharo",
            "Darth Tenebrous",
            "Thalleus Tharn",
            "Darth Venamis"
        ])
        self.assertEqual(planet, "Bith")
        self.assertEqual(des, "Large cranium\nAcute senses of smell and hearing")
        self.assertEqual(image, "http://img4.wikia.nocookie.net/__cb20060903181845/starwars/images/7/74/Bith_%28Doikk_Nats%29.jpg")
        self.assertEqual(language, "Bith")
        self.assertEqual(classification, "Craniopod")

    def test_get_all_sorted_species_2 (self) :
        species = Species.get_all_sorted_species("language")
        s = species[0]
        name = s.get_name()
        characters = s.get_characters()
        planet = s.get_planet()
        des = s.get_description()
        image = s.get_image()
        language = s.get_language()
        classification = s.get_classification()

        self.assertEqual(name, "Bith")
        self.assertEqual(characters, [
            "Unaw Aharo",
            "Darth Tenebrous",
            "Thalleus Tharn",
            "Darth Venamis"
        ])
        self.assertEqual(planet, "Bith")
        self.assertEqual(des, "Large cranium\nAcute senses of smell and hearing")
        self.assertEqual(image, "http://img4.wikia.nocookie.net/__cb20060903181845/starwars/images/7/74/Bith_%28Doikk_Nats%29.jpg")
        self.assertEqual(language, "Bith")
        self.assertEqual(classification, "Craniopod")

    def test_get_all_sorted_species_3 (self) :
        species = Species.get_all_sorted_species("classification")
        s = species[0]
        name = s.get_name()
        characters = s.get_characters()
        planet = s.get_planet()
        des = s.get_description()
        image = s.get_image()
        language = s.get_language()
        classification = s.get_classification()

        self.assertEqual(name, "Bith")
        self.assertEqual(characters, [
            "Unaw Aharo",
            "Darth Tenebrous",
            "Thalleus Tharn",
            "Darth Venamis"
        ])
        self.assertEqual(planet, "Bith")
        self.assertEqual(des, "Large cranium\nAcute senses of smell and hearing")
        self.assertEqual(image, "http://img4.wikia.nocookie.net/__cb20060903181845/starwars/images/7/74/Bith_%28Doikk_Nats%29.jpg")
        self.assertEqual(language, "Bith")
        self.assertEqual(classification, "Craniopod")

    def test_get_species_1 (self) :
        s = Species.get_species("Bith")
        name = s.get_name()
        characters = s.get_characters()
        planet = s.get_planet()
        des = s.get_description()
        image = s.get_image()
        language = s.get_language()
        classification = s.get_classification()

        self.assertEqual(name, "Bith")
        self.assertEqual(characters, [
            "Unaw Aharo",
            "Darth Tenebrous",
            "Thalleus Tharn",
            "Darth Venamis"
        ])
        self.assertEqual(planet, "Bith")
        self.assertEqual(des, "Large cranium\nAcute senses of smell and hearing")
        self.assertEqual(image, "http://img4.wikia.nocookie.net/__cb20060903181845/starwars/images/7/74/Bith_%28Doikk_Nats%29.jpg")
        self.assertEqual(language, "Bith")
        self.assertEqual(classification, "Craniopod")

    def test_get_species_2 (self) :
        s = Species.get_species("Human")
        name = s.get_name()
        characters = s.get_characters()
        planet = s.get_planet()
        des = s.get_description()
        image = s.get_image()
        language = s.get_language()
        classification = s.get_classification()

        self.assertEqual(name, "Human")
        self.assertEqual(characters, ["Darth Vader", "Boba Fett"])
        self.assertEqual(planet, "Coruscant")
        self.assertEqual(des, "Humans, taxonomically referred to as Homo sapiens, were the galaxy's most numerous and politically dominant sentient species with millions of major and minor colonies galaxywide. Believed to have originated on the galactic capital of Coruscant, they could be found anywhere, engaged in many different pursuits: spacers, mercenaries, smugglers, merchants, soldiers, assassins, farmers, crime lords, laborers, slaves, slavers, and many others, including Jedi and Sith. Since Humans were the most common sentient species, they were often considered to be a standard or average to which the biology, psychology, and culture of other species were compared.")
        self.assertEqual(image, "http:\/\/img2.wikia.nocookie.net\/__cb20100628191857\/starwars\/images\/thumb\/5\/5d\/Humans-TESB30.jpg\/400px-Humans-TESB30.jpg")
        self.assertEqual(language, "Galactic Basic Standard")
        self.assertEqual(classification, "Mammal")

    def test_species_3 (self) :
        s = Species.get_species("Omwati")
        name = s.get_name()
        characters = s.get_characters()
        planet = s.get_planet()
        des = s.get_description()
        image = s.get_image()
        language = s.get_language()
        classification = s.get_classification()

        self.assertEqual(name, "Omwati")
        self.assertEqual(characters, [
            "Aleema Finn",
            "Pillik",
            "Tannis",
            "Tiu Zax"
        ])
        self.assertEqual(planet, "Omwat")
        self.assertEqual(des, "Bird-like anthropoids")
        self.assertEqual(image, "http://img1.wikia.nocookie.net/__cb20070528041553/starwars/images/thumb/2/2f/Omwati.JPG/360px-Omwati.JPG")
        self.assertEqual(language, "Omwatese")
        self.assertEqual(classification, "Near-Human")

# ----
# main
# ----
if __name__ == "__main__" :
    main()



