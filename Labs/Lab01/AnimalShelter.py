# Creates new AnimalShelter object
class AnimalShelter:

    # Constructor initializing values for AnimalShelter
    def __init__(self):
        self.AnimalShelter = {}

    # Create methods to manipulate the dictionary
    def addAnimal(self, animal):
        if self.AnimalShelter.get(animal.species) == None:
            self.AnimalShelter[animal.species] = [animal]   
        elif animal not in self.AnimalShelter[animal.species]:
            self.AnimalShelter[animal.species].append(animal)
            

    def removeAnimal(self, animal):
        if animal in self.AnimalShelter[animal.species]:
            self.AnimalShelter[animal.species].remove(animal)

    def removeSpecies(self, species):
        species = species.upper()
        if species in self.AnimalShelter:
            self.AnimalShelter[species] = []

    def getAnimalsBySpecies(self, species):
        species = species.upper()
        animal_string = ""
        if species in self.AnimalShelter:
            if self.AnimalShelter[species] == []:
                return animal_string
            else:
                for a in self.AnimalShelter[species]:
                    if self.AnimalShelter[species].index(a) == len(self.AnimalShelter[species]) - 1:
                        animal_string += a.toString()
                        return animal_string
                    animal_string += a.toString() + "\n"
        else:
            return animal_string

    def doesAnimalExist(self, animal):
        if animal.species not in self.AnimalShelter:
            return False
        else:
            if animal in self.AnimalShelter[animal.species]:
                return True
            else:
                return False
    
