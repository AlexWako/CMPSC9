from Pizza import Pizza

class CustomPizza(Pizza):
    def __init__(self, size):
        super().__init__(size)
        self.toppings = []
        if self.size == "S":
            self.price = 8.00
        if self.size == "M":
            self.price = 10.00
        if self.size == "L":
            self.price = 12.00
       
    def addTopping(self, topping):
        self.toppings.append(topping)
        if self.size == "S":
            self.price += 0.50
        if self.size == "M":
            self.price += 0.75
        if self.size == "L":
            self.price += 1.00

    def getPizzaDetails(self):
        returnString = f"CUSTOM PIZZA\nSize: {self.size}\nToppings:\n"
        for topping in self.toppings:
            returnString += "\t+ " + topping + "\n"
        return returnString + f"Price: ${self.price:.2f}\n"



