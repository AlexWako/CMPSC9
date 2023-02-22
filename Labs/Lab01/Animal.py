# Create new animal object
class Animal:

    # Initializing the animal object
    def __init__(self, species=None, weight=None, age=None, name=None):
        if type(species) == str:
            self.species = species.upper()
        else:
            self.species = species
        self.weight = weight
        self.age = age
        if type(name) == str:
            self.name = name.upper()
        else:
            self.name = name
    
    # Creating setter for animal object attributes
    def setSpecies(self, species):
        self.species = species.upper()

    def setWeight(self, weight):
        self.weight = weight

    def setAge(self, age):
        self.age = age

    def setName(self, name):
        self.name = name.upper()

    # Print method to summarize the animal object being created
    def toString(self):
        return("Species: {}, Name: {}, Age: {}, Weight: {}".format(
            self.species, self.name, self.age, self.weight))




                                                                  
