# Abstraction and Encapsulation in Python

class Library:
    def __init__(self, books):
        self.books = books

    def list_books(self):
        print("Available Books")
        for book in self.books:
            print(book)

    def borrow_book(self, borrow_book):
        if borrow_book in self.books:
            print("Get Your Book Now")
            self.books.remove(borrow_book)
        else:
            print("Book not Available")

    def receive_book(self, receive_book):
        print("You have returned the book")
        self.books.append(receive_book)


books = ['C', 'C++', 'Java','python']
o = Library(books)

msg = """
    1.Display Book
    2.Borrow Book
    3.Return Book
"""
while True:
    print(msg)
    ch = int(input("Enter Your Choice : "))
    if ch == 1:
        o.list_books()
    elif ch == 2:
        book = input("Enter Book Name To Borrow : ")
        o.borrow_book(book)
    elif ch == 3:
        book = input("Enter Book Name To Return : ")
        o.receive_book(book)
    else:
        print("Thank You come again")
        quit()
