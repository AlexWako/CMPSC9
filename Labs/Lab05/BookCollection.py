from Book import Book
from BookCollectionNode import BookCollectionNode

class BookCollection():
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def getNumberOfBooks(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count

    def insertBook(self, book):
        current = self.head
        previous = None
        stop = False
        new = BookCollectionNode(book)
        while current != None and not stop:
            if current.getData() > book:
                stop = True
            else:  
                previous = current
                current = current.getNext()
        if previous == None:
            new.setNext(self.head)
            self.head = new
        else: 
            new.setNext(current)
            previous.setNext(new)
    
    def getBooksByAuthor(self, author):
        current = self.head
        books = ""
        while current != None:
            if current.getData().getAuthor().lower() == author.lower():
                books += current.getData().getBookDetails() + "\n"
            current = current.getNext() 
        return books

    def getAllBooksInCollection(self):
        current = self.head
        books = ""
        while current != None:  
            books += current.getData().getBookDetails() + "\n"
            current = current.getNext()
        return books

    def removeAuthor(self, author):
        current = self.head
        previous = None
        while current != None:
            if current.getData().getAuthor().lower() == author.lower():
                if previous != None:
                    previous.setNext(current.getNext())
                else:
                    self.head = current.getNext()  
            else:
                previous = current
            current = current.getNext()
    

    def recursiveSearchTitle(self, title, bookNode):
        if bookNode == None:
            return False
        if bookNode.getData().getTitle().lower() == title.lower():
            return True
        return self.recursiveSearchTitle(title, bookNode.getNext())




