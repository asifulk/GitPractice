class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.books_borrowed = []

    def borrow_book(self, book):
        if book.is_available:
            book.is_available = False
            self.books_borrowed.append(book)
            print(f"{self.name} has borrowed the book {book.title}")
        else:
            print(f"Sorry, the book {book.title} is not available for borrowing.")

    def return_book(self, book):
        if book in self.books_borrowed:
            book.is_available = True
            self.books_borrowed.remove(book)
            print(f"{self.name} has returned the book {book.title}")
        else:
            print(f"{self.name} did not borrow the book {book.title}")

    def display_info(self):
        print(f"Member Name: {self.name}\nMember ID: {self.member_id}")
        if self.books_borrowed:
            print("Books Borrowed:")
            for book in self.books_borrowed:
                print(f"- {book.title}")
        else:
            print("No books borrowed")

member1 = Member("Jonathan", "M0001")
member1.display_info()
