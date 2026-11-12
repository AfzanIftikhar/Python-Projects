# Python Learning Log — 7–12 November 2026

## Today's Focus

Continued developing a **Library Management System** in Python to practise Object-Oriented Programming (OOP), exception handling, menu-driven applications, and JSON file handling.

## What I Learned

### 1. Encapsulation with Properties

- Used a private attribute, `_is_available`, inside the `Book` class.
- Created a getter using `@property`.
- Created a setter using `@is_available.setter`.
- Added validation to ensure availability can only be a Boolean (`True` or `False`).

### 2. Inheritance

Created two member types:

- `StudentMember`, with a borrowing limit of 2 books.
- `RegularMember`, with a borrowing limit of 5 books.

Used `super().__init__()` to reuse the parent class constructor.

### 3. Polymorphism and Object-Oriented Design

Worked with separate classes:

- `Book` represents an individual physical book copy.
- `Member` represents a library member.
- `Library` manages books, members, borrowing and returning.

Each physical book copy receives a unique UUID.

### 4. Type Checking and Exception Handling

Practised:

- `isinstance()` to check object types.
- `raise TypeError` to reject invalid input types.
- `try-except` to handle exceptions without terminating the application unexpectedly.
- Understanding the difference between `TypeError` and `ValueError`.

### 5. Menu-Driven Applications

Implemented a terminal-based menu that allows users to interact with the library.

The menu includes:

- Adding and removing books.
- Searching and displaying books.
- Registering members.
- Searching members.
- Borrowing and returning books.
- Exiting the application.

Learned how to retrieve actual Python objects using search methods instead of passing user-input strings directly to methods that expect objects.

### 6. JSON Serialization

Learned how to convert Python objects into JSON-compatible dictionaries and lists.

Used:

- `json.dump()` to save data.
- `json.load()` to retrieve data.
- `open()` with file modes such as `"r"` and `"w"`.
- `indent=4` to make JSON files readable.

Created two files:

- `library.json` — stores book information.
- `members.json` — stores member information.

For books, I save:
- Book ID
- Title
- Author
- Availability

For members, I save:
- Member ID
- Name
- Membership type
- Borrowed book IDs

### 7. JSON Deserialization

Learned that loading JSON data does not automatically recreate Python objects.

I need to reconstruct objects from the dictionaries stored in JSON.

For example:

- Recreate a `Book` object using its saved properties.
- Recreate either a `StudentMember` or `RegularMember` using the saved membership type.
- Restore existing UUIDs instead of generating new ones.
- Reconnect borrowed book IDs to their corresponding Book objects.

Modified the `Member` constructor to accept an optional `member_id`, allowing existing member IDs to be restored.

## What I Implemented

My Library Management System currently includes:

- Book and Member classes.
- StudentMember and RegularMember subclasses.
- Encapsulated book availability.
- UUID generation for books and members.
- Adding, searching, displaying and removing books.
- Registering, searching and removing members.
- Borrowing and returning functionality.
- Borrowing limits based on membership type.
- Input validation and exception handling.
- Menu-driven terminal interface.
- Saving books and members in separate JSON files.
- Loading existing books when the program starts.
- Saving member borrowing history using book IDs.
- Loading members with their original IDs and membership types.
- Restoring borrowing limits through the appropriate subclass constructors.

## Testing Notes

During testing, I learned several important things:

- A book must exist in the library before it can be borrowed.
- A member must be registered before borrowing.
- A member cannot borrow an unavailable book.
- A member can only return a book they have actually borrowed.
- Book availability must change to `False` when borrowed and `True` when returned.
- Saving data to JSON allows it to persist after restarting the application.
- Books must be loaded before members because member borrowing histories refer to existing book IDs.
- When restoring objects, saved IDs should be reused rather than generating new ones.

## Remaining Tasks

1. **Complete and test JSON deserialization**
   - Finish restoring members and their borrowing histories.
   - Match saved book IDs with actual Book objects.
   - Verify borrowing history after restarting the application.

2. **Fix and test return persistence**
   - Ensure returning a book changes its availability to `True`.
   - Save the updated book and member data after a successful return.

3. **Synchronize book removal with JSON**
   - Ensure removing a book from the library also updates `library.json`.

4. **Final testing**
   - Test borrowing and returning after restarting the application.
   - Test adding and removing books.
   - Test member registration and borrowing limits.
   - Verify that all changes persist correctly.

## Today's Takeaway

This project has helped me move beyond simply understanding OOP concepts and start combining them into a practical application.

I have also started understanding how Python objects interact with external storage through JSON serialization and deserialization.

**Next session:** Finish JSON persistence, fix the remaining synchronization issues, and thoroughly test the Library Management System.
