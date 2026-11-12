#  -----------------------------Library Management System --------------------------------------
import uuid
import json

# --------------------------------------- Book Class --------------------------------------------------------

class Book:
    def __init__(self,title,author,book_id=None,is_available= True):
        
        if not isinstance(title,str):
            raise TypeError("Title must be a string")
        if not isinstance(author,str):
            raise TypeError("Author must be a string")

        if book_id is None:
            self.book_id = str(uuid.uuid4()) 
        else:
            self.book_id = book_id    
        self.title = title
        self.author = author
        self._is_available = is_available


    @property
    def is_available(self):
        return self._is_available

    @is_available.setter
    def is_available(self,status):
        if  isinstance(status, bool):
            self._is_available = status
        else:
            raise TypeError("Availability must be True or False")
        
    

        
    def display_details(self):
        return f"========== Book Details ======== \n BookID : {self.book_id} \n Title : {self.title} \n Author : {self.author} \n Available : {self._is_available}"



# --------------------------------------- Member Class --------------------------------------------------------
class Member:
    def __init__(self,name,member_id = None):
        if member_id is None:
            self.member_id = str(uuid.uuid4())
        else:
            self.member_id = member_id
        self.name = name
        self.borrowed_books = []
       

    def display_details(self):
        return f"============== Member Details ================ \n Member_ID : {self.member_id} \n Name : {self.name} \n Borrowed Books : {self.borrowed_books}"


class StudentMember(Member):
    def __init__(self, name,member_id=None):
        super().__init__(name,member_id)
        self.borrowing_limit = 2

class RegularMember(Member):
    def __init__(self, name,member_id=None):
        super().__init__(name,member_id)
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
            library.save_books()
            library.save_members()
            return f"{member.name} returned the book Successfully"

    def save_books(self):
        all_books = []

        for book in self.books:
            book_data = {
                "book_id": book.book_id,
                "title":book.title,
                "author" : book.author,
                "is_available":book.is_available
            }

            all_books.append(book_data)

        with open("library.json", "w") as file:
            json.dump(all_books,file,indent=4)

    def load_books(self):
        try:
            with open("library.json", "r") as file:
                content = json.load(file)
                for books in content:
                    book = Book(books["title"],books["author"],books["book_id"],books['is_available'])
                    self.books.append(book)
        except FileNotFoundError:
            print("file not found!")

    def save_members(self):
        saved_members = []
      

        for members in self.members:
            borrowed_books = []

            if isinstance(members,StudentMember):
                membership_type = "Student"
            elif isinstance(members,RegularMember):
                membership_type = "Regular"
                
            for borrow_book in members.borrowed_books:
                borrowed_books.append(borrow_book.book_id)


            member_data = {
                "member_id" : members.member_id,
                "name" : members.name,
                "membership_type" : membership_type ,
                "borrowed_books" : borrowed_books
            }
            saved_members.append(member_data)

        with open("members.json", "w") as file:
            json.dump(saved_members,file,indent=4)

    def load_members(self):
        try:
            with open("members.json", "r") as file:
                content = json.load(file)

                for members in content:
                    if members["membership_type"] == "Student":
                        member = StudentMember(
                        members["name"],
                        members["member_id"]
                    )

                    elif members["membership_type"] == "Regular":
                        member = RegularMember(
                        members["name"],
                        members["member_id"]
                    )

                    self.members.append(member)
        except FileNotFoundError:
            print("File not found !")

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
library.load_books()
library.load_members()

while True:

    display()
    inp = input("Enter a Choice : ")

    if inp == "1":
        title = input("Enter Book Title : ")
        author = input("Enter Book Author : ")
        try:
            book = Book(title,author)   
            print(library.add_book(book))
            library.save_books()
           
            
        except TypeError as error:
            print(error)

    elif inp == "2":
        title = input("Enter Book Title : ")

        try:
            print(library.remove_book(title))
            library.save_books()
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
            library.display_books()
            
        except TypeError as error:
            print(error)

    elif inp == "5":
            member_name = input("Enter Member Name : ")
            book_title = input("Enter Book Title : ")
            try:
                member = library.search_member(member_name)
                book = library.search_book(book_title)     
                result = library.borrow_book(member, book)
                print(result)
                print(member.borrowed_books)
                library.save_books()
                library.save_members()
                
            except TypeError as error:
                print(error)
    
    elif inp == "6":
            member_name = input("Enter Member Name : ")
            title = input("Enter Book Title : ")
            try:
                member = library.search_member(member_name) 
                book = library.search_book(title)
                print(library.return_book(member, book))
                
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
                library.save_members()
                
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