from book import Book

class LibraryBook(Book):
    def __init__(self, title, author, inventory):
        super().__init__(title, author)
        self.inventory = inventory
        self.borrowers = []

    def checkOut(self, name):
        if self.inventory < 1:
            print('Out of stock')
            return
        self.borrowers.append(name)
        self.inventory -= 1

    def __repr__(self):
        return self.title, self.inventory
