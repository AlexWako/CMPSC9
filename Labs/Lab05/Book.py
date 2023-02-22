class Book():
    def __init__(self, title = "", author = "", year = None):
        self.title = title
        self.author = author
        self.year = year

    def getTitle(self):
        return self.title

    def getAuthor(self):
        return self.author

    def getYear(self):
        return self.year

    def getBookDetails(self):
        return "Title: {}, Author: {}, Year: {}".format(self.title, self.author, self.year)

    def __gt__(self, rhs):
        return self.author + str(self.year) + self.title > rhs.author + str(rhs.year) + rhs.title
