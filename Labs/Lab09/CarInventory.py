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
        make = make.upper()
        model = model.upper()
        if currentNode == None:
            return None
        elif make == currentNode.getMake() and model == currentNode.getModel():
            return currentNode
        elif make != currentNode.getMake():
            if make < currentNode.getMake():
                return self._get(make, model, currentNode.getLeft())
            else:
                return self._get(make, model, currentNode.getRight())
        else:
            if model < currentNode.getModel():
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
        
    def getSuccessor(self, make, model):
        nodeToFind = self._get(make, model, self.root)
        successor = None
        if nodeToFind != None:
            successor = self._getSuccessor(nodeToFind)
        return successor 
    
    def _getSuccessor(self, node):
        if node.getRight() != None:
            return self.findMin(node.getRight())    
        successor = node.getParent()
        while node.getParent() != None:
            if node != successor.getRight():
                break
            node = successor
            successor = successor.getParent()
        return successor

    def findMin(self, node):
        currentNode = node
        while currentNode.getLeft() != None:
            currentNode = currentNode.getLeft()
        return currentNode

    def removeCar(self, make, model, year, price):
        nodeToRemove = self._get(make, model, self.root)
        if nodeToRemove != None and len(nodeToRemove.cars) > 1:
            toRemove = Car(make, model, year, price)
            if toRemove in nodeToRemove.cars:
                nodeToRemove.cars.remove(toRemove)
                return True
            else:
                return False
        elif nodeToRemove != None and len(nodeToRemove.cars) == 1:
            if self.root.getLeft() == None and self.root.getRight() == None and self.root == nodeToRemove:
                if self.root.cars[0] == Car(make, model, year, price):
                    self.root = None
                    return True
                else:
                    return False
            elif self.root.getLeft() != None or self.root.getRight() != None:
                self._removeCar(nodeToRemove)
                return True
            else:
                return False
        else:
            return False

    def _removeCar(self, currentNode):
        if currentNode.getLeft() == None and currentNode.getRight() == None:
            if currentNode == currentNode.parent.getLeft():
                currentNode.parent.left = None
            else:
                currentNode.parent.right = None
        elif currentNode.getLeft() != None and currentNode.getRight() != None:
            succ = self.getSuccessor(currentNode.getMake(), currentNode.getModel())
            self.spliceOut(succ)
            currentNode.make = succ.make
            currentNode.model = succ.model
            currentNode.cars = succ.cars
        else:
            if currentNode.getLeft() != None:
                if currentNode.getParent() != None and currentNode == currentNode.parent.left:
                    currentNode.left.parent = currentNode.getParent()
                    currentNode.parent.left = currentNode.getLeft()
                elif currentNode.getParent() != None and currentNode == currentNode.parent.right:
                    currentNode.left.parent = currentNode.getParent()
                    currentNode.parent.right = currentNode.getLeft()
                else:
                    currentNode.make = currentNode.left.getMake()
                    currentNode.model = currentNode.left.getModel()
                    currentNode.cars = currentNode.left.getCars()
                    currentNode.right = currentNode.left.getRight()
                    currentNode.left = currentNode.left.getLeft()

            else:
                if currentNode.getParent() != None and currentNode == currentNode.parent.left:
                    currentNode.right.parent = currentNode.getParent()
                    currentNode.parent.left = currentNode.getRight()
                elif currentNode.getParent() != None and currentNode == currentNode.parent.right:
                    currentNode.right.parent = currentNode.getParent()
                    currentNode.parent.right = currentNode.getRight()
                else:
                    currentNode.make = currentNode.right.getMake()
                    currentNode.model = currentNode.right.getModel()
                    currentNode.cars = currentNode.right.getCars()
                    currentNode.left = currentNode.right.getLeft()
                    currentNode.right = currentNode.right.getRight()

    def spliceOut(self, successor):
        if successor.getLeft() == None and  successor.getRight() == None:
            if successor == successor.parent.left:
                successor.parent.left = None
            else:
                successor.parent.right = None
        else:
            if successor.getRight() != None:
                if successor == successor.parent.left:
                    successor.parent.left = successor.right
                else:
                    successor.parent.right = successor.right
                successor.right.parent = successor.parent