from Pizza import Pizza
from CustomPizza import CustomPizza
from SpecialtyPizza import SpecialtyPizza
from OrderQueue import OrderQueue
from PizzaOrder import PizzaOrder

cp1 = CustomPizza("M")
cp1.addTopping("Pepperoni")
cp2 = CustomPizza("L")
cp3 = CustomPizza("S")
cp3.addTopping("Sausage")
cp3.addTopping("Pepperoni")
sp1 = SpecialtyPizza("S", "House")
sp2 = SpecialtyPizza("M", "New York Style")
order1 = PizzaOrder(183000)
order1.addPizza(cp1)
order1.addPizza(cp2)
order2 = PizzaOrder(13000)
order2.addPizza(cp3)
order3 = PizzaOrder(123000)
order3.addPizza(sp1)
order3.addPizza(sp2)
queue1 = OrderQueue()
queue1.addOrder(order1)
queue1.addOrder(order2)
queue1.addOrder(order3)

# Test for getPizzaDetails()
assert cp1.getPizzaDetails() == "CUSTOM PIZZA\nSize: M\nToppings:\n\t+ Pepperoni\nPrice: $10.75\n"
assert cp2.getPizzaDetails() == "CUSTOM PIZZA\nSize: L\nToppings:\nPrice: $12.00\n"
assert cp3.getPizzaDetails() == "CUSTOM PIZZA\nSize: S\nToppings:\n\t+ Sausage\n" + "\t+ Pepperoni\nPrice: $9.00\n"
assert sp1.getPizzaDetails() == "SPECIALTY PIZZA\nSize: S\nName: House\nPrice: $12.00\n"
assert sp2.getPizzaDetails() == "SPECIALTY PIZZA\nSize: M\nName: New York Style\nPrice: $14.00\n"

# Test for getOrderDescription()
assert order1.getOrderDescription() == "******\nOrder Time: 183000\nCUSTOM PIZZA\nSize: M\nToppings:\n\
\t+ Pepperoni\nPrice: $10.75\n\n----\nCUSTOM PIZZA\nSize: L\nToppings:\nPrice: $12.00\n\n----\n\
TOTAL ORDER PRICE: $22.75\n******\n"
assert order2.getOrderDescription() == "******\nOrder Time: 13000\nCUSTOM PIZZA\nSize: S\nToppings:\n\
\t+ Sausage\n\t+ Pepperoni\nPrice: $9.00\n\n----\nTOTAL ORDER PRICE: $9.00\n******\n"
assert order3.getOrderDescription() == "******\nOrder Time: 123000\nSPECIALTY PIZZA\nSize: S\nName: House\nPrice: $12.00\n\n\
----\nSPECIALTY PIZZA\nSize: M\nName: New York Style\nPrice: $14.00\n\n----\nTOTAL ORDER PRICE: $26.00\n******\n"

# Test for processNextOrder()
assert queue1.processNextOrder() == "******\nOrder Time: 13000\nCUSTOM PIZZA\nSize: S\nToppings:\n\
\t+ Sausage\n\t+ Pepperoni\nPrice: $9.00\n\n----\nTOTAL ORDER PRICE: $9.00\n******\n"
assert queue1.processNextOrder() == "******\nOrder Time: 123000\nSPECIALTY PIZZA\nSize: S\nName: House\nPrice: $12.00\n\
\n----\nSPECIALTY PIZZA\nSize: M\nName: New York Style\nPrice: $14.00\n\n----\nTOTAL ORDER PRICE: $26.00\n******\n"
assert queue1.processNextOrder() == "******\nOrder Time: 183000\nCUSTOM PIZZA\nSize: M\nToppings:\n\
\t+ Pepperoni\nPrice: $10.75\n\n----\nCUSTOM PIZZA\nSize: L\nToppings:\nPrice: $12.00\n\n----\n\
TOTAL ORDER PRICE: $22.75\n******\n"