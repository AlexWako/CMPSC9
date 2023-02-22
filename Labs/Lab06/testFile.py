from Apartment import Apartment
from lab06 import *

a0 = Apartment(1000, 100, "bad")
a1 = Apartment(800, 200, "excellent")
a2 = Apartment(900, 300, "excellent")
a3 = Apartment(1000, 100, "bad")
a4 = Apartment(500, 50, "bad")
a5 = Apartment(800, 200, "average")
a6 = Apartment(1500, 0, "excellent")
a7 = Apartment(900, 100, "average")
apartmentList = [a0, a1, a2, a3, a4, a5, a6, a7]

assert (a0 < a1) == False
assert (a2 < a7) == False
assert (a1 < a5) == True
assert (a0 < a3) == False
assert (a6 < a6) == False

assert (a0 > a1) == True
assert (a2 > a7) == True
assert (a1 > a5) == False
assert (a0 > a3) == False
assert (a6 > a6) == False

assert (a0 == a1) == False
assert (a2 == a7) == False
assert (a1 == a5) == False
assert (a0 == a3) == True
assert (a6 == a6) == True

assert ensureSortedAscending(apartmentList) == False
mergesort(apartmentList)
assert ensureSortedAscending(apartmentList) == True

assert getBestApartment(apartmentList) == "(Apartment) Rent: $500, Distance From UCSB: 50m, Condition: bad"
assert getWorstApartment(apartmentList) == "(Apartment) Rent: $1500, Distance From UCSB: 0m, Condition: excellent"
assert getAffordableApartments(apartmentList, 300) == ""
assert getAffordableApartments(apartmentList, 1000) == "(Apartment) Rent: $500, Distance From UCSB: 50m, Condition: bad\n" +\
    "(Apartment) Rent: $800, Distance From UCSB: 200m, Condition: excellent\n" +\
        "(Apartment) Rent: $800, Distance From UCSB: 200m, Condition: average\n" +\
            "(Apartment) Rent: $900, Distance From UCSB: 100m, Condition: average\n" +\
                "(Apartment) Rent: $900, Distance From UCSB: 300m, Condition: excellent\n" +\
                    "(Apartment) Rent: $1000, Distance From UCSB: 100m, Condition: bad\n" +\
                        "(Apartment) Rent: $1000, Distance From UCSB: 100m, Condition: bad"

                     
