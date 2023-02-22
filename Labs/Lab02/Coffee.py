from Beverage import Beverage

class Coffee(Beverage):

    def __init__(self, ounces, price, style):
        super().__init__(ounces, price)
        self.style = style

    def getInfo(self):
        info = "{} Coffee, ".format(self.style)
        info += Beverage.getInfo(self)
        return info
        
        
