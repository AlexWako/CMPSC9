from Car import Car
from CarInventoryNode import CarInventoryNode

class CarInventory:
    def __init__(self):
        self.root = None

    def addCar(self, car):
        if self.root != None:
            self._addCar(car, self.root)
        else:
            self.root = CarInventoryNode(car)

    def _addCar(self, car, currentNode):
        tempNode = CarInventoryNode(car)
        if car.make == currentNode.make and car.model == currentNode.model:
            currentNode.cars.append(car)  
        else:
            if car < currentNode.cars[0]:
                if currentNode.getLeft():
                    self._addCar(car, currentNode.getLeft())
                else:
                    currentNode.setLeft(tempNode)
                    tempNode.setParent(currentNode)
            else:
                if currentNode.getRight():
                    self._addCar(car, currentNode.getRight())
                else:
                    currentNode.setRight(tempNode)
                    tempNode.setParent(currentNode)
                    
    def doesCarExist(self, car):
        if self.root != None:
            return self._doesCarExist(car, self.root)
        else: 
            return False
        
    def _doesCarExist(self, car, currentNode):
        if currentNode == None:
            return False
        elif car in currentNode.cars:
            return True
        elif car < currentNode.cars[0]:
            return self._doesCarExist(car, currentNode.getLeft())
        else:
            return self._doesCarExist(car, currentNode.getRight())
        
    def inOrder(self): 
        return self._inOrder(self.root)

    def _inOrder(self, currentNode):
        returnStr = ""
        if currentNode != None:
            returnStr += str(self._inOrder(currentNode.getLeft()))
            returnStr += str(currentNode)
            returnStr += str(self._inOrder(currentNode.getRight()))
        return returnStr

    def preOrder(self):
        return self._preOrder(self.root)
    
    def _preOrder(self, currentNode):
        returnStr = ""
        if currentNode != None:
            returnStr += str(currentNode)
            returnStr += str(self._preOrder(currentNode.getLeft()))
            returnStr += str(self._preOrder(currentNode.getRight()))
        return returnStr
    
    def postOrder(self):
        return self._postOrder(self.root)
    
    def _postOrder(self, currentNode):
        returnStr = ""
        if currentNode != None:
            returnStr += str(self._postOrder(currentNode.getLeft()))
            returnStr += str(self._postOrder(currentNode.getRight()))
            returnStr += str(currentNode)
        return returnStr
    
    def getBestCar(self, make, model):
        make = make.upper()
        model = model.upper()
        if self.root != None:
            node = self._get(make, model, self.root)
            if node != None:
                best = node.cars[0]
                for car in node.cars:
                    if car > best:
                        best = car
                return best
            else:
                return None
        else:
            return None
    
    def getWorstCar(self, make, model):
        make = make.upper()
        model = model.upper()
        if self.root != None:
            node = self._get(make, model, self.root)
            if node != None:
                worst = node.cars[0]
                for car in node.cars:
                    if car < worst:
                        worst = car
                return worst
            else:
                return None
        else:
            return None

    def _get(self, make, model, currentNode):
        if currentNode == None:
            return None
        elif make.upper() == currentNode.getMake() and model.upper() == currentNode.getModel():
            return currentNode
        elif currentNode.make != make:
            if make < currentNode.make:
                return self._get(make, model, currentNode.getLeft())
            else:
                return self._get(make, model, currentNode.getRight())
        else:
            if model < currentNode.model:
                return self._get(make, model, currentNode.getLeft())
            else:
                return self._get(make, model, currentNode.getRight())
            
    def getTotalInventoryPrice(self):
        return self._getTotalInventoryPrice(self.root)
    
    def _getTotalInventoryPrice(self, currentNode):
        total = 0
        if currentNode != None:
            total += self._getTotalInventoryPrice(currentNode.getLeft())
            if len(currentNode.cars) > 1:
                for car in currentNode.cars:
                    total += car.price
            else:
                total += currentNode.cars[0].price
            total += self._getTotalInventoryPrice(currentNode.getRight())
        return total
        


        