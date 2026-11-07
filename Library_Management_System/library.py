#  -----------------------------Library Management System --------------------------------------
import uuid

# --------------------------------------- Book Class --------------------------------------------------------

class Book:
    def __init__(self,title,author):
        
        if not isinstance(title,str):
            raise TypeError("Title must be a string")
        if not isinstance(author,str):
            raise TypeError("Author must be a string")
        
        self.book_id = str(uuid.uuid4()) 
        self.title = title
        self.author = author
        self.__is_available = True


    @property
    def is_available(self):
        return self.__is_available

    @is_available.setter
    def is_available(self,status):
        if  isinstance(status, bool):
            self.__is_available = status
        else:
            raise TypeError("Availability must be True or False")
        
    

        
    def display_details(self):
        return f"========== Book Details ======== \n Book ID : {self.book_id} \n Title : {self.title} \n Author : {self.author} \n Available : {self.__is_available}"



# --------------------------------------- Member Class --------------------------------------------------------
class Member:
    def __init__(self,name):
        self.member_id = str(uuid.uuid4())
        self.name = name
        self.borrowed_books = []
       

    def display_details(self):
        return f"============== Member Details ================ \n Member ID : {self.member_id} \n Name : {self.name} \n Borrowed Books : {self.borrowed_books}"


class StudentMember(Member):
    def __init__(self, name):
        super().__init__(name)
        self.borrowing_limit = 2

class RegularMember(Member):
    def __init__(self, name):
        super().__init__(name)
        self.borrowing_limit = 5

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
        if not isinstance(book, Book):
            raise TypeError("Only Book object are allowed !")
        self.books.append(book)
        return f"Book added !"

    
    # Searching a Book 
    def search_book(self,title):
        if not isinstance(title,str):
            raise TypeError("Book Title must be a string")
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        else:
            return f"No match found for {title}"

    # Removing a book

    def remove_book(self,title):
        if not isinstance(title,str):
            raise TypeError ("Book Title must be a String")
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                return f"Book removed from the list"

        else:
            return f"No match  found !"


    # Adding a Member
    def register_member(self,member):
        if not isinstance(member, Member):
            raise TypeError("Member must be a string")
        self.members.append(member)
        return f"Member Added !"
    
    # Deleting a member
    def remove_member(self,name):
        # Exception handling
        if not isinstance(name,str):
            raise TypeError("Name must be a string")
        
        for member in self.members:
            if member.name.lower() == name.lower():
                self.members.remove(member)
                return "Member Removed Successfully"
        else:
            return "No match Found !" 

    
  
    # Searching a member
    def search_member(self,name):
        if not isinstance(name,str):
            raise TypeError("Name must be a String")
        for member in self.members:
            if member.name.lower() == name.lower():
                return member
        else:
            return f"No match found "

    
    # Borrowing a book Functionality
    def borrow_book(self,member,book):
        # Exception Handling
        if not isinstance(member,Member):
            raise TypeError("Member must be a String")
        if not isinstance(book, Book):
            raise TypeError("Book must be an object")


        if not member in self.members:
            return "Sorry You are not registered in the library"
        elif not book in self.books:
            return "Sorry The book is not from our library"
        elif not book.is_available:
            return f"Book is not available"
        else:
            already_borrowed = len(member.borrowed_books)
            if already_borrowed >= member.borrowing_limit:
                return f"{member.name}, your limit of borrowing book has been reached. you can not borrow another book"
            member.borrowed_books.append(book)
            book.is_available = False
            return f"{member.name} borrowed the book successfully"

    # Returning a book

    def return_book(self,member,book):
         # Exception Handling
        if not isinstance(member,Member):
            raise TypeError("Member must be a String")
        if not isinstance(book, Book):
            raise TypeError("Book must be an object")
        


        
        if not book in member.borrowed_books:
            return f"{member.name} does not borrowed the book" 
        else:
            member.borrowed_books.remove(book)
            book.is_available = True
            return f"{member.name} returned the book Successfully"


# --------------------------------------- Displaying records --------------------------------------------------------


# Creating Books
try:
    book1 = Book("Python Basics", "John Smith")
    book2 = Book( "The Pragmatic Programmer", "Andy Hunt")
    book3 = Book( "Atomic Habits", "James")
    book4 = Book( "Rich Dad Poor Dad", "John")
except TypeError as error:
    print(error)


# Creating Members
try:
    member1 = StudentMember('Afzan')
    member2 = RegularMember('Zaid')
except TypeError as error:
    print(error)
# Creating Object Libraries

try:

    library = Library()

# Adding Book to library
    print(library.add_book(book1))
    print(library.add_book(book2))
    print(library.add_book(book3))
    print(library.add_book(book4))

# Registering a member into the library
    print(library.register_member(member1))

# Displaying the details of Added Book
    print(library.display_books())


# Searching a book
    print(library.search_book("python Basics").display_details())

# Searching a member
    print(library.search_member("afzan").display_details())


# Borrowing Book
    print(library.borrow_book(member1,book1))
    print(library.borrow_book(member1,book2))
    print(library.borrow_book(member1,book3))


# Returning a book
    print(library.return_book(member2,book1))
except TypeError as error:
    print(error)

