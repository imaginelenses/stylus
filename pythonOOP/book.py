class Book:
    def __init__(self, title, author=None):
        self.title = title
        self.author = author

    def printDetails(self):
        print(self.title + 'is written by ' + self.author)

    def __repr__(self):
        return self.title

