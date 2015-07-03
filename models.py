class character():
	all_characters ={}

	def __init__(self, name, planet, species, description, image):
		self.character = {}
		self.character["name"] = name
		self.character["planet"] = planet
		self.character["species"] = species
		self.character["description"] = description
		self.character["image"] = image
		self.__add_to_dict__(name)

	def __get_info__(self):
		return self.character

	def __add_to_dict__(self, name):
		self.all_characters[str(name)] = self.character

	def __get_all_dict__(self):
		return self.all_characters


class planet():
	all_planets ={}

	def __init__(self, name, character_list, species_list, description, image):
		self.planet = {}
		self.planet["name"] = name
		self.planet["characters"] = character_list
		self.planet["species"] = species_list
		self.planet["description"] = description
		self.planet["image"] = image
		self.__add_to_dict__(name)

	def __get_info__(self):
		return self.planet

	def __add_to_dict__(self, name):
		self.all_planets[str(name)] = self.planet

	def __get_all_dict__(self):
		return self.all_planets

class species():
	all_species ={}

	def __init__(self, name, character_list, planet_list, description, image):
		self.species = {}
		self.species["name"] = name
		self.species["characters"] = character_list
		self.species["planets"] = planet_list
		self.species["description"] = description
		self.species["image"] = image
		self.__add_to_dict__(name)

	def __get_info__(self):
		return self.species

	def __add_to_dict__(self, name):
		self.all_species[str(name)] = self.species

	def __get_all_dict__(self):
		return self.all_species

x = species("Human", ["Darth Vader", "Boba Fett"],["Tatooine", "Kamino"], "something", "url image")
x = species("Wookiee", ["Chewbacca"], ["Kashyyyk"], "something", "url image")
print(x.__get_all_dict__())


