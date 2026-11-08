#  -----------------------------Library Management System --------------------------------------
import uuid
import json

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
        return f"========== Book Details ======== \n BookID : {self.book_id} \n Title : {self.title} \n Author : {self.author} \n Available : {self.__is_available}"



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
        if not self.books:
            print("No books available in the library.")
            return

        for book in self.books:
            print(book.display_details())
           

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
         


        
        if not book in member.borrowed_books:
            return f"{member.name} does not borrowed the book" 
        else:
            member.borrowed_books.remove(book)
            book.is_available = True
            return f"{member.name} returned the book Successfully"





# ----------------- Menu interface ---------------------

def display():
    print("============================Please Enter your choice===========================================")
    print("Add a Book : 1")
    print("Remove a Book : 2")
    print("Search a Book : 3")
    print("Display all Books : 4")
    print("Borrow a Book : 5")
    print("Return a Book : 6")
    print("Register a member : 7")
    print("Search Member : 8")
    print("Exit : 9")
    print("=============================================================================================")

library = Library()

while True:

    display()
    inp = input("Enter a Choice : ")

    if inp == "1":
        title = input("Enter Book Title : ")
        author = input("Enter Book Author : ")
        try:
            book = Book(title,author)   
            print(library.add_book(book))

            for books in library.display_books:
                books_data = {
                    "book_id" : books.BookID,
                    "title": books.Title,
                    "author":books.Author,
                    "is_available":books.Available
                }

           
            
        except TypeError as error:
            print(error)

    elif inp == "2":
        title = input("Enter Book Title : ")

        try:
            print(library.remove_book(title))
            
        except TypeError as error:
            print(error)

    elif inp == "3":
        title = input("Enter Book Title : ")
        try:
            print(library.search_book(title))
        except TypeError as error:
            print(error)

    elif inp == "4":
        try:
            print(library.display_books())
            
        except TypeError as error:
            print(error)

    elif inp == "5":
            member_name = input("Enter Member Name : ")
            book_title = input("Enter Book Title : ")
            try:
                member = library.search_member(member_name)
                book = library.search_book(book_title)     
                print(library.borrow_book(member, book))
                
            except TypeError as error:
                print(error)
    
    elif inp == "6":
            member = input("Enter Member Name : ")
            title = input("Enter Book Title : ")
            try:
                print(library.return_book(member, title))
                
            except TypeError as error:
                print(error)
    
    elif inp == "7":
            Name = input("Enter Your Name : ")
            print("Choose Membership type : \n 1.Student Membership \n 2.Regular Membership")
            membership_type = input(" Choose Membership : ")

            if membership_type == "1":
                selected_member = StudentMember(Name)
            elif membership_type == "2":
                selected_member = RegularMember(Name)
            else :
                print("Invalid selection")
            try:
               
                print(library.register_member(selected_member))
                
            except TypeError as error:
                print(error)

    elif inp == "8":
            
            Name = input("Enter Your Name : ")        
            try:
                print(library.search_member(Name))
                
            except TypeError as error:  
                print(error)
    elif inp == "9":
        break

    else:
        print("Wrong Selection !")