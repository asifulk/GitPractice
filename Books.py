class Book:
    def __init__(self, title, author, ISBN, num_pages):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.num_pages = num_pages
        self.is_available = True

    def display_info(self):
        print(f"Title: {self.title}\nAuthor: {self.author}\nISBN: {self.ISBN}\nPages: {self.num_pages}\nAvailable: {self.is_available}\n")

book1 = Book("Python Workshop", "XYZ", "123456789", 500)
book1.display_info()

book2 = Book("Advanced Python Workshop", "ABC", "0908456789", 100)
book2.display_info()
