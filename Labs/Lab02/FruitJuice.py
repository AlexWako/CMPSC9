from Beverage import Beverage

class FruitJuice(Beverage):

    def __init__(self, ounces, price, fruits):
        super().__init__(ounces, price)
        self.fruits = fruits

    def getInfo(self):
        info = ""
        for fruit in self.fruits:
            if fruit == self.fruits[-1]:
                info += fruit + " "
                break
            info += fruit + "/"
        info += "Juice, " + Beverage.getInfo(self)
        return info
        
