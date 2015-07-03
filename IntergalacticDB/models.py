class character():

    def __init__(self, name, planet, species, description, image):
        self.character = {}
        self.character["name"] = name
        self.character["planet"] = planet
        self.character["species"] = species
        self.character["description"] = description
        self.character["image"] = image

    def __get_info__(self):
        return self.character


class planet():

    def __init__(self, name, character_list, species_list, description, image):
        self.planet = {}
        self.planet["name"] = name
        self.planet["characters"] = character_list
        self.planet["species"] = species_list
        self.planet["description"] = description
        self.planet["image"] = image

    def __get_info__(self):
        return self.planet


class species():

    def __init__(self, name, character_list, planet_list, description, image):
        self.species = {}
        self.species["name"] = name
        self.species["characters"] = character_list
        self.species["planets"] = planet_list
        self.species["description"] = description
        self.species["image"] = image

    def __get_info__(self):
        return self.species
