from Car import Car
from CarInventoryNode import CarInventoryNode
from CarInventory import CarInventory

garage = CarInventory()

car1 = Car("Mazda", "Mazda5", 2003, 5000)
car2 = Car("Mazda", "Mazda3", 2018, 15000)
car3 = Car("Toyota", "Camary", 2005, 6000)
car4 = Car("Honda", "Accord", 2021, 30000)
car5 = Car("Honda", "Accord", 2019, 25000)
car6 = Car("Toyota", "Corolla", 2012, 12500)
car7 = Car("Lamborghini", "Huracan", 2022, 200000)
car8 = Car("Toyota", "Corolla", 2012, 12500)

garage.addCar(car1)
garage.addCar(car2)
garage.addCar(car3)
garage.addCar(car4)
garage.addCar(car5)
garage.addCar(car6)

assert(car1 < car2) == False
assert(car2 < car3) == True
assert(car3 < car4) == False
assert(car4 < car5) == False

assert(car1 > car2) == True
assert(car2 > car3) == False
assert(car3 > car4) == True
assert(car4 > car5) == True

assert(car6 < car8) == None
assert(car6 > car8) == None
assert(car6 == car8) == True

assert str(car1) == "Make: MAZDA, Model: MAZDA5, Year: 2003, Price: $5000"
assert str(car3) == "Make: TOYOTA, Model: CAMARY, Year: 2005, Price: $6000"
assert str(car5) == "Make: HONDA, Model: ACCORD, Year: 2019, Price: $25000"
assert str(car7) == "Make: LAMBORGHINI, Model: HURACAN, Year: 2022, Price: $200000"

assert garage.doesCarExist(car1) == True
assert garage.doesCarExist(car3) == True
assert garage.doesCarExist(car5) == True
assert garage.doesCarExist(car7) == False

assert garage.inOrder() == "Make: HONDA, Model: ACCORD, Year: 2021, Price: $30000\n\
Make: HONDA, Model: ACCORD, Year: 2019, Price: $25000\n\
Make: MAZDA, Model: MAZDA3, Year: 2018, Price: $15000\n\
Make: MAZDA, Model: MAZDA5, Year: 2003, Price: $5000\n\
Make: TOYOTA, Model: CAMARY, Year: 2005, Price: $6000\n\
Make: TOYOTA, Model: COROLLA, Year: 2012, Price: $12500\n"

assert garage.preOrder() == "Make: MAZDA, Model: MAZDA5, Year: 2003, Price: $5000\n\
Make: MAZDA, Model: MAZDA3, Year: 2018, Price: $15000\n\
Make: HONDA, Model: ACCORD, Year: 2021, Price: $30000\n\
Make: HONDA, Model: ACCORD, Year: 2019, Price: $25000\n\
Make: TOYOTA, Model: CAMARY, Year: 2005, Price: $6000\n\
Make: TOYOTA, Model: COROLLA, Year: 2012, Price: $12500\n"

assert garage.postOrder() == "Make: HONDA, Model: ACCORD, Year: 2021, Price: $30000\n\
Make: HONDA, Model: ACCORD, Year: 2019, Price: $25000\n\
Make: MAZDA, Model: MAZDA3, Year: 2018, Price: $15000\n\
Make: TOYOTA, Model: COROLLA, Year: 2012, Price: $12500\n\
Make: TOYOTA, Model: CAMARY, Year: 2005, Price: $6000\n\
Make: MAZDA, Model: MAZDA5, Year: 2003, Price: $5000\n"


assert garage.getBestCar("Mazda", "Mazda5") == car1
assert garage.getBestCar("Honda", "Accord") == car4
assert garage.getBestCar("ToYoTa", "cAmArY") == car3

assert garage.getWorstCar("Mazda", "Mazda3") == car2
assert garage.getWorstCar("Honda", "Accord") == car5
assert garage.getWorstCar("ToYoTa", "CoRoLlA") == car6

assert garage.getTotalInventoryPrice() == 93500

# Adding new cars

car9 = Car("Toyota", "Camary", 2020, 30000)
car10 = Car("Mazda", "Mazda5", 2018, 20000)
car11 = Car("Lexus", "Ultima", 2020, 45000)
car12 = Car("Mazda", "Mazda7", 2022, 35000)

garage.addCar(car9)
garage.addCar(car10)
garage.addCar(car11)
garage.addCar(car12)


assert garage.getSuccessor("Mazda", "Mazda5").cars == [car12]
assert garage.getSuccessor("Mazda", "Mazda7").cars == [car3, car9]
assert garage.getSuccessor("Toyota", "Camary").cars == [car6]
assert garage.getSuccessor("Toyota", "Corolla") == None
assert garage.getSuccessor("Lamborgini", "Huracan") == None

garage.removeCar("Mazda", "Mazda5", 2003, 5000)
assert garage.preOrder() == "Make: MAZDA, Model: MAZDA5, Year: 2018, Price: $20000\n\
Make: MAZDA, Model: MAZDA3, Year: 2018, Price: $15000\n\
Make: HONDA, Model: ACCORD, Year: 2021, Price: $30000\n\
Make: HONDA, Model: ACCORD, Year: 2019, Price: $25000\n\
Make: LEXUS, Model: ULTIMA, Year: 2020, Price: $45000\n\
Make: TOYOTA, Model: CAMARY, Year: 2005, Price: $6000\n\
Make: TOYOTA, Model: CAMARY, Year: 2020, Price: $30000\n\
Make: MAZDA, Model: MAZDA7, Year: 2022, Price: $35000\n\
Make: TOYOTA, Model: COROLLA, Year: 2012, Price: $12500\n"

garage.removeCar("Toyota", "Corolla", 2012, 12500)
assert garage.preOrder() == "Make: MAZDA, Model: MAZDA5, Year: 2018, Price: $20000\n\
Make: MAZDA, Model: MAZDA3, Year: 2018, Price: $15000\n\
Make: HONDA, Model: ACCORD, Year: 2021, Price: $30000\n\
Make: HONDA, Model: ACCORD, Year: 2019, Price: $25000\n\
Make: LEXUS, Model: ULTIMA, Year: 2020, Price: $45000\n\
Make: TOYOTA, Model: CAMARY, Year: 2005, Price: $6000\n\
Make: TOYOTA, Model: CAMARY, Year: 2020, Price: $30000\n\
Make: MAZDA, Model: MAZDA7, Year: 2022, Price: $35000\n"

garage.removeCar("Toyota", "Camary", 2020, 30000)
garage.removeCar("Toyota", "Camary", 2005, 6000)
assert garage.postOrder() == "Make: LEXUS, Model: ULTIMA, Year: 2020, Price: $45000\n\
Make: HONDA, Model: ACCORD, Year: 2021, Price: $30000\n\
Make: HONDA, Model: ACCORD, Year: 2019, Price: $25000\n\
Make: MAZDA, Model: MAZDA3, Year: 2018, Price: $15000\n\
Make: MAZDA, Model: MAZDA7, Year: 2022, Price: $35000\n\
Make: MAZDA, Model: MAZDA5, Year: 2018, Price: $20000\n"

newGarage = CarInventory()
newGarage.addCar(car1)
newGarage.addCar(car2)
newGarage.addCar(car3)
newGarage.addCar(car4)
newGarage.addCar(car5)
newGarage.addCar(car6)
newGarage.addCar(car9)
newGarage.addCar(car10)
newGarage.addCar(car11)
newGarage.addCar(car12)

newGarage.removeCar("Mazda", "Mazda3", 2018, 15000)
assert newGarage.postOrder() == "Make: LEXUS, Model: ULTIMA, Year: 2020, Price: $45000\n\
Make: HONDA, Model: ACCORD, Year: 2021, Price: $30000\n\
Make: HONDA, Model: ACCORD, Year: 2019, Price: $25000\n\
Make: MAZDA, Model: MAZDA7, Year: 2022, Price: $35000\n\
Make: TOYOTA, Model: COROLLA, Year: 2012, Price: $12500\n\
Make: TOYOTA, Model: CAMARY, Year: 2005, Price: $6000\n\
Make: TOYOTA, Model: CAMARY, Year: 2020, Price: $30000\n\
Make: MAZDA, Model: MAZDA5, Year: 2003, Price: $5000\n\
Make: MAZDA, Model: MAZDA5, Year: 2018, Price: $20000\n"

newGarage.removeCar("Mazda", "Mazda5", 2003, 5000)
newGarage.removeCar("Mazda", "Mazda5", 2018, 20000)
assert newGarage.inOrder() == "Make: HONDA, Model: ACCORD, Year: 2021, Price: $30000\n\
Make: HONDA, Model: ACCORD, Year: 2019, Price: $25000\n\
Make: LEXUS, Model: ULTIMA, Year: 2020, Price: $45000\n\
Make: MAZDA, Model: MAZDA7, Year: 2022, Price: $35000\n\
Make: TOYOTA, Model: CAMARY, Year: 2005, Price: $6000\n\
Make: TOYOTA, Model: CAMARY, Year: 2020, Price: $30000\n\
Make: TOYOTA, Model: COROLLA, Year: 2012, Price: $12500\n"

newGarage.removeCar("Mazda", "Mazda7", 2022, 35000)
assert newGarage.inOrder() == "Make: HONDA, Model: ACCORD, Year: 2021, Price: $30000\n\
Make: HONDA, Model: ACCORD, Year: 2019, Price: $25000\n\
Make: LEXUS, Model: ULTIMA, Year: 2020, Price: $45000\n\
Make: TOYOTA, Model: CAMARY, Year: 2005, Price: $6000\n\
Make: TOYOTA, Model: CAMARY, Year: 2020, Price: $30000\n\
Make: TOYOTA, Model: COROLLA, Year: 2012, Price: $12500\n"