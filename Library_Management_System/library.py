#  -----------------------------Library Management System --------------------------------------
import uuid

# --------------------------------------- Book Class --------------------------------------------------------

class Book:
    def __init__(self,title,author):
        self.book_id = str(uuid.uuid4()) 
        self.title = title
        self.author = author
        self.is_available = True

    def display_details(self):
        return f"========== Book Details ======== \n Book ID : {self.book_id} \n Title : {self.title} \n Author : {self.author} \n Available : {self.is_available}"



# --------------------------------------- Member Class --------------------------------------------------------
class Member:
    def __init__(self,name):
        self.member_id = str(uuid.uuid4())
        self.name = name
        self.borrowed_books = []

    def display_details(self):
        return f"============== Member Details ================ \n Member ID : {self.member_id} \n Name : {self.name} \n Borrowed Books : {self.borrowed_books}"




# --------------------------------------- Library Class --------------------------------------------------------

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    # Displaying Books
    def display_books(self):
        all_books = []
        for book in self.books:
            all_books.append(book.display_details())     

        return all_books

    # Adding a Book
    def add_book(self,book):
        self.books.append(book)
        return f"Book added !"

    
    # Searching a Book 
    def search_book(self,title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        else:
            return f"No match found for {title}"

    # Removing a book

    def remove_book(self,title):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                return f"Book removed from the list"

        else:
            return f"No match  found !"


    # Adding a Member
    def register_member(self,member):
        self.members.append(member)
        return f"Member Added !"
    
    # Deleting a member
    def remove_member(self,name):
        for member in self.members:
            if member.name.lower() == name.lower():
                self.members.remove(member)
                return "Member Removed Successfully"
        else:
            return "No match Found !" 

    
  
    # Searching a member
    def search_member(self,name):
        for member in self.members:
            if member.name.lower() == name.lower():
                return member
        else:
            return f"No match found "
    

# --------------------------------------- Displaying records --------------------------------------------------------


# Creating Books
book1 = Book("Python Basics", "John Smith")
book2 = Book( "The Pragmatic Programmer", "Andy Hunt")

# Creating Members
member1 = Member('Afzan')
member2 = Member('Zaid')
# Creating Object Libraries
library = Library()

# Adding Book to library
print(library.add_book(book1))

# Registering a member into the library
print(library.register_member(member1))

# Displaying the details of Added Book
print(library.display_books())


# Searching a book
print(library.search_book("python Basics").display_details())

# deleting a book
print(library.remove_book('python basics'))


# Removing a member
print(library.remove_member('zaid`'))

# Searching a member
print(library.search_member("afzan").display_details())