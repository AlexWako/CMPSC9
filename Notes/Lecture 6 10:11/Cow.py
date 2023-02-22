#Cow.py

from Animal import Animal

# By using parenthesis next to the new object, the Cow class inherits all the
# methods of the class inside the parenthesis
class Cow(Animal):

    def __init__(self, species = None, name = None, sound = None):
        # Using super() we can reuse methdos from parent methods in the constructor
        super().__init__(species, name)
        self.sound = sound
        

    # Cow class method to set sound
    def setSound(self, sound):
        self.sound = sound

    # Redefining an inherited method without changing it on the original
    def getSound(self):
        return "{}".format(self.sound)
        # Using get sound from the animal method instead
        # s = Animal.getSound(self) + "\n"
        # or s = super().getSound()
        # or s = super(Cow,self).getSound()

