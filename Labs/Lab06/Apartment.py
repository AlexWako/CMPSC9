class Apartment:
    def __init__(self, rent, metersFromUCSB, condition):
        self.rent = rent
        self.metersFromUCSB = metersFromUCSB
        self.condition = condition

    def getRent(self):
        return self.rent

    def getMetersFromUCSB(self):
        return self.metersFromUCSB

    def getCondition(self):
        return self.condition

    def getApartmentDetails(self):
        return "(Apartment) Rent: ${}, Distance From UCSB: {}m, Condition: {}".format(self.rent, self.metersFromUCSB, self.condition)

    def __lt__(self, rhs):
        if self.rent != rhs.rent:
            return self.rent < rhs.rent
        else:
            if self.metersFromUCSB != rhs.metersFromUCSB:
                return self.metersFromUCSB < rhs.metersFromUCSB
            else:
                if self.condition != rhs.condition:
                    return len(self.condition) > len(rhs.condition)
                else:
                    return False

    def __gt__(self, rhs):
        if self.rent != rhs.rent:
            return self.rent > rhs.rent
        else:
            if self.metersFromUCSB != rhs.metersFromUCSB:
                return self.metersFromUCSB > rhs.metersFromUCSB
            else:
                if self.condition != rhs.condition:
                    return len(self.condition) < len(rhs.condition)
                else:
                    return False

    def __eq__(self, rhs):
        return self.getRent() == rhs.getRent() and self.getMetersFromUCSB() == rhs.getMetersFromUCSB() and self.getCondition() == rhs.getCondition()

