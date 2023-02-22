class PizzaOrder:
    def __init__(self, time):
        self.pizzas = []
        self.time = time

    def getTime(self):
        return self.time

    def setTime(self, time):
        self.time = time

    def addPizza(self, pizza):
        self.pizzas.append(pizza)

    def getOrderDescription(self):
        returnString = f"******\nOrder Time: {self.time}\n"
        price = 0
        for pizza in self.pizzas:
            returnString += pizza.getPizzaDetails() + "\n----\n"
            price += pizza.getPrice()
        return returnString + f"TOTAL ORDER PRICE: ${price:.2f}" + "\n******\n"
