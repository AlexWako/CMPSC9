from Beverage import Beverage
from Coffee import Coffee
from FruitJuice import FruitJuice
from DrinkOrder import DrinkOrder

a = Coffee(24, 10, "Latte")
b = FruitJuice(32, 15.5, ["Strawberry", "Banana"])

assert a.getInfo() == "Latte Coffee, 24 oz, $10.00"
assert b.getInfo() == "Strawberry/Banana Juice, 32 oz, $15.50"

a.updateOunces(16)
a.updatePrice(7.5)
assert a.getOunces() == 16
assert a.getPrice() == 7.5

b.updateOunces(40)
b.updatePrice(18)
assert b.getOunces() == 40
assert b.getPrice() == 18
    
c = Beverage(26, 12.155)
assert c.getInfo() == "26 oz, $12.15"

d = FruitJuice(12, 5.205, ["Grape"])
assert d.getInfo() == "Grape Juice, 12 oz, $5.21"

drinks = DrinkOrder()
drinks.addBeverage(a)
drinks.addBeverage(b)
drinks.addBeverage(c)
drinks.addBeverage(d)
assert drinks.getTotalOrder() == "Order Items:\n* Latte Coffee, 16 oz, $7.50\n* Strawberry/Banana Juice, 40 oz, $18.00\n* 26 oz, $12.15\n* Grape Juice, 12 oz, $5.21\nTotal Price: $42.86"

