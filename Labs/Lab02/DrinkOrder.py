from Beverage import Beverage

class DrinkOrder:

    def __init__(self):
        self.drinks = []

    def addBeverage(self, beverage):
        self.drinks.append(beverage)

    def getTotalOrder(self):
        order = "Order Items:\n"
        total_price = 0
        for drink in self.drinks:
            total_price += drink.price
            order += "* " + drink.getInfo() + "\n"
        order += "Total Price: ${:.2f}".format(total_price)
        return order
                
