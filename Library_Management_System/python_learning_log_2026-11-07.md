# Python Learning Log --- 7 November 2026

## Today's Focus

Today I continued building a **Library Management System** in Python to
practise Object-Oriented Programming (OOP) and exception handling.

## What I Learned

### 1. Encapsulation with Properties

-   Used a private attribute, `__is_available`, inside the `Book` class.
-   Created a getter with `@property` to read the book's availability.
-   Created a setter with `@is_available.setter` to control changes to
    availability.
-   Added validation so availability can only be set to a Boolean value
    (`True` or `False`).

Example:

``` python
@property
def is_available(self):
    return self.__is_available

@is_available.setter
def is_available(self, status):
    if isinstance(status, bool):
        self.__is_available = status
    else:
        raise TypeError("Availability must be True or False")
```

### 2. Inheritance

Practised inheritance by creating two member types:

-   `StudentMember`, which inherits from `Member` and has a borrowing
    limit of 2 books.
-   `RegularMember`, which inherits from `Member` and has a borrowing
    limit of 5 books.

Used `super().__init__(name)` to reuse the parent class constructor.

### 3. Polymorphism and Object-Oriented Design

Continued working with separate classes and objects:

-   `Book` represents an individual physical book copy.
-   `Member` represents a library member.
-   `Library` manages books, members, borrowing and returning.

Each physical book copy receives its own UUID.

### 4. Type Checking with `isinstance()`

Learned that `isinstance(value, Class)` checks whether a value is an
instance of a class.

Examples:

``` python
isinstance(10, int)          # True
isinstance("hello", int)     # False
isinstance(student, Member)  # True if StudentMember inherits Member
```

`isinstance()` also recognises instances of subclasses.

### 5. Raising Exceptions with `raise`

Learned that `raise` deliberately generates an exception when an
operation receives invalid input.

Example:

``` python
if not isinstance(book, Book):
    raise TypeError("Only Book objects are allowed!")
```

-   `TypeError` is appropriate when the input has the wrong data type.
-   `ValueError` is generally used when the data type is correct but the
    value itself is invalid.

### 6. Handling Exceptions with `try-except`

Learned that `try-except` catches exceptions so the program can respond
instead of terminating unexpectedly.

Example:

``` python
try:
    library.add_book("Atomic Habits")

except TypeError as error:
    print("Error:", error)
```

Key points:

-   `try` contains code that might raise an exception.
-   `except` handles a matching exception.
-   `as error` stores the exception object so its message can be
    displayed.
-   When an exception occurs, the remaining statements in that `try`
    block are skipped.
-   `try-except` can be used around object creation if a constructor may
    raise an exception, as well as around method calls.

**Important design principle:** Keep input validation and `raise` inside
the relevant class methods. Handle exceptions around calls in the main
program or user interface.

## What I Implemented Today

I worked on these parts of the Library Management System:

-   `Book` class with title, author, UUID and availability.
-   Encapsulated book availability using a property and setter.
-   `Member` class with a UUID and a list of borrowed books.
-   `StudentMember` and `RegularMember` subclasses with different
    borrowing limits.
-   `Library` class to manage books and members.
-   Methods to add, search, remove and display books.
-   Methods to register, search and remove members.
-   Book borrowing with checks for registration, library ownership,
    availability and borrowing limits.
-   Book returning with a check that the member actually borrowed the
    book.
-   Type validation using `isinstance()`.
-   Exception generation using `raise TypeError`.
-   Exception handling using `try-except` in the main testing section.

## Testing Notes

While testing, I also learned to check the setup before interpreting the
output:

-   A book must be added to the library before it can be borrowed.
-   A member must be registered before borrowing.
-   A member can only return a book that appears in their own
    `borrowed_books` list.
-   If one statement raises an exception inside a `try` block, later
    statements in that same block are skipped.

## What I Will Do Tomorrow

I have deliberately left these tasks for tomorrow:

1.  **Menu-driven interface**
    -   Add a terminal menu with options such as adding books,
        registering members, searching, borrowing and returning.
    -   Let the user choose actions instead of manually calling methods.
2.  **Basic JSON file handling**
    -   Learn how to save library data in a JSON file.
    -   Load saved data when the program starts.
    -   Understand how Python objects can be represented as
        JSON-compatible data and recreated.

## Today's Takeaway

Today I strengthened my understanding of OOP, encapsulation,
inheritance, polymorphism, type checking and exception handling by
applying them to one practical Python project.

**Next session:** Finish the menu interface and begin basic JSON
persistence.
