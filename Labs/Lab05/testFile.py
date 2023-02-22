from Book import Book
from BookCollectionNode import BookCollectionNode
from BookCollection import BookCollection

b0 = Book("Book 1", "Alex, Wako", 2003)
b1 = Book("Book 2", "Alex, Wako", 2005)
b2 = Book("New Book 1", "Patrick, Han", 2005)
b3 = Book("New Book 1", "Ethan, Cheng", 2007)
b4 = Book("Remake Book 1", "Shota, Shimizu", 2011)
b5 = Book("Remake New Book 1", "Genta, Ueno", 2019)
bEmpty = Book()

bc = BookCollection()
bc.insertBook(b0)
bc.insertBook(b1)
bc.insertBook(b2)
bc.insertBook(b3)
bc.insertBook(b4)
bc.insertBook(b5)
bc.insertBook(bEmpty)

def BookTest():
    assert b1.getTitle() == "Book 2"
    assert b3.getTitle() == "New Book 1"
    assert bEmpty.getTitle() == ""

    assert b2.getAuthor() == "Patrick, Han"
    assert b5.getAuthor() == "Genta, Ueno"
    assert bEmpty.getAuthor() == ""

    assert b0.getYear() == 2003
    assert b4.getYear() == 2011
    assert bEmpty.getYear() == None

    assert b3.getBookDetails() == "Title: New Book 1, Author: Ethan, Cheng, Year: 2007"
    assert b4.getBookDetails() == "Title: Remake Book 1, Author: Shota, Shimizu, Year: 2011"
    assert b5.getBookDetails() == "Title: Remake New Book 1, Author: Genta, Ueno, Year: 2019"
    assert bEmpty.getBookDetails() == "Title: , Author: , Year: None"

def BookCollectionTest():
    assert bc.getNumberOfBooks() == 7

    assert bc.isEmpty() == False

    assert bc.getBooksByAuthor("Alex, Wako") == "Title: Book 1, Author: Alex, Wako, Year: 2003\n" +\
        "Title: Book 2, Author: Alex, Wako, Year: 2005\n"
    assert bc.getBooksByAuthor("Patrick, Han") == "Title: New Book 1, Author: Patrick, Han, Year: 2005\n"

    assert bc.getAllBooksInCollection() == "Title: Book 1, Author: Alex, Wako, Year: 2003\n"\
        "Title: Book 2, Author: Alex, Wako, Year: 2005\n"\
            "Title: New Book 1, Author: Ethan, Cheng, Year: 2007\n"\
                "Title: Remake New Book 1, Author: Genta, Ueno, Year: 2019\n"\
                    "Title: , Author: , Year: None\n"\
                        "Title: New Book 1, Author: Patrick, Han, Year: 2005\n"\
                            "Title: Remake Book 1, Author: Shota, Shimizu, Year: 2011\n"

    bc.removeAuthor("Alex, Wako")
    assert bc.getAllBooksInCollection() == "Title: New Book 1, Author: Ethan, Cheng, Year: 2007\n" +\
        "Title: Remake New Book 1, Author: Genta, Ueno, Year: 2019\n" +\
            "Title: , Author: , Year: None\n" +\
                "Title: New Book 1, Author: Patrick, Han, Year: 2005\n" +\
                    "Title: Remake Book 1, Author: Shota, Shimizu, Year: 2011\n"

    bc.removeAuthor("Shota, Shimizu")
    assert bc.getAllBooksInCollection() == "Title: New Book 1, Author: Ethan, Cheng, Year: 2007\n" +\
        "Title: Remake New Book 1, Author: Genta, Ueno, Year: 2019\n" +\
            "Title: , Author: , Year: None\n" +\
                "Title: New Book 1, Author: Patrick, Han, Year: 2005\n"
    
    assert bc.recursiveSearchTitle("New Book 1", bc.head) == True
    
    bc.removeAuthor("Ethan, Cheng")
    assert bc.recursiveSearchTitle("New Book 1", bc.head) == True

    bc.removeAuthor("Patrick, Han")
    assert bc.recursiveSearchTitle("New Book 1", bc.head) == False

    bc.removeAuthor("Genta, Ueno")
    bc.removeAuthor("")
    assert bc.isEmpty() == True

BookTest()
BookCollectionTest()
# Test for BookCollectionNode() is unnecessary as the methods are closely tied to BookCollectionTest()