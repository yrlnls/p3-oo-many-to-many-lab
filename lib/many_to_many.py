class Author:
    all = []

    def __init__(self, name=""):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book: 'Book', date: str, royalties: int):
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        return sum([contract.royalties for contract in self.contracts()])    


class Book:
    all = []
    def __init__(self, title=str):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        return [contract.author for contract in self.contracts()]


class Contract:
    all = []
    def __init__(self, author,book, date, royalties):
        if not isinstance(author, Author):
            raise TypeError("Author must be an instance of Author class")
        
        if not isinstance(book, Book):
            raise TypeError("Book must be an instance of Book class")
        
        if not isinstance(date, str):
            raise TypeError("Date must be a string")
        
        if not isinstance(royalties, int):
            raise TypeError("Royalties must be an integer")
        
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)
    
    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in Contract.all if contract.date == date]