class Book:
    all = []

    def __init__(self, title):
        self.title = title
        self.all.append(self)

    def authors(self):
        return [contract.author for contract in self.contracts()]
    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

class Author:
    all = []

    def __init__(self, name):
        self.name = name
        self.all.append(self)
        self._contracts = None

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise Exception("Invalid book object")
        contract = Contract(self, book, date, royalties)
        return contract

    def total_royalties(self):
        total = 0
        for contract in self.contracts():
            total += contract.royalties
        return total

class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Invalid author object")
        if not isinstance(book, Book):
            raise Exception("Invalid book object")
        if not isinstance(date, str):
            raise Exception("Invalid date object")
        if not isinstance(royalties, int):
            raise Exception("Invalid royalties object")
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        self.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]