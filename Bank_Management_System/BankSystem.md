# Bank Management System – Python Project

## 1. Project Overview

I am developing a **Bank Management System** using Python. The primary objective of this project is to strengthen my understanding of Python, particularly Object-Oriented Programming (OOP), file handling, JSON serialization and deserialization, data management, list comprehensions, class methods, and exception handling.

The application provides a menu-driven interface through which users can create and manage their bank accounts.

All account information is stored in a `data.json` file to ensure data persistence between program executions.

## 2. Technologies and Modules

The following Python modules and libraries are being used:

- `random` – To generate random account numbers.
- `json` – To serialize and deserialize account data.
- `string` – To generate random alphabetic and numeric characters.
- `pathlib.Path` – To check whether the JSON data file exists and manage file paths.

## 3. Project Architecture

The project is developed using a class-based approach.

### Bank Class

The `Bank` class handles the application's main functionality.

**Class Attributes:**

- `database`: Stores the name of the JSON file (`data.json`).
- `data`: A Python list that holds all account records temporarily while the program is running.

**Class Methods:**

- `__update()`: Saves the updated account data into the JSON file.
- `__accountGenerate()`: Generates a random account number consisting of alphabetic characters, numeric characters, and a special character.

## 4. Development and Implemented Features

### Step 1: Menu-Driven Interface

The application provides users with six different options:

| Option | Functionality | Status |
|---|---|---|
| 1 | Create a new bank account | Implemented |
| 2 | Deposit money | Implemented |
| 3 | Withdraw money | Implemented |
| 4 | View account details | Implemented |
| 5 | Update account details | Implemented |
| 6 | Delete a bank account | Implemented |

### Step 2: Data Initialization and Persistence

A `data.json` file is used to store all bank account information.

Whenever the application starts:

1. Check whether `data.json` exists using `Path`.
2. If the file exists, open it in read mode.
3. Load the existing JSON data into a Python list using `json.loads()`.
4. If the file does not exist, display an appropriate message.
5. Use the Python list as temporary storage throughout the program's execution.

All account-related operations are performed on this Python list.

Whenever an operation modifies account information, the updated list is saved back into `data.json` using `json.dumps()`.

This ensures that account information remains available even after the program terminates.

### Step 3: Account Creation

Implemented the account creation functionality.

The application collects the following information from the user:

- Full name
- Age
- Email address
- Account number
- Four-digit PIN
- Initial balance

**Account Number Generation:**

A random account number is generated using:

- Three random alphabetic characters.
- Three random numeric characters.
- One special character.

The generated characters are shuffled to make the account number less predictable.

**Account Validation:**

Before creating an account, the application checks:

- The user must be at least 18 years old.
- The PIN must contain exactly four digits.

If the validation is successful:

1. A new account record is created as a Python dictionary.
2. The dictionary is appended to the main data list.
3. The updated data is saved into `data.json`.

### Step 4: Deposit Money

Implemented the money deposit functionality.

The application asks the user to provide:

- Account number
- PIN
- Deposit amount

**Process:**

1. Authenticate the user using their account number and PIN.
2. Find the corresponding account using list comprehension.
3. Validate the deposit amount.
4. Allow deposits greater than zero and up to 10,000.
5. Update the account balance.
6. Save the updated information into `data.json`.

### Step 5: Withdraw Money

Implemented the money withdrawal functionality.

The application asks the user to provide:

- Account number
- PIN
- Withdrawal amount

**Validation Rules:**

- The account must exist.
- The PIN must match.
- The account must have sufficient balance.
- The withdrawal amount must be at least 500.
- The withdrawal amount must be a multiple of 500.

If all conditions are satisfied:

1. Deduct the requested amount from the account balance.
2. Save the updated account information into `data.json`.
3. Display a successful withdrawal message.

### Step 6: View Account Details

Implemented the account details functionality.

Users can access their account information by providing:

- Account number
- PIN

The application searches for the matching account and displays its stored information, including name, age, email, account number, PIN, and current balance.

### Step 7: Update Account Details

Implemented the account update functionality.

Users can update the following information:

- Name
- Email address
- PIN

**Process:**

1. Authenticate the user using their account number and PIN.
2. Ask for the new information.
3. Allow users to leave a field unchanged by skipping it.
4. Preserve the existing account number, age, and balance.
5. Update the account information.
6. Save the modified data into `data.json`.

### Step 8: Delete Account

Implemented the account deletion functionality.

Users can delete their accounts by providing:

- Account number
- PIN

**Process:**

1. Authenticate the user.
2. Find the corresponding account.
3. Identify its index in the main data list.
4. Remove the account using `pop()`.
5. Save the updated list into `data.json`.
6. Display a confirmation message.

---

## 5. Python Concepts Practised

Through this project, I have practised the following concepts:

- Object-Oriented Programming (OOP)
- Classes and Objects
- Class Attributes and Class Methods
- Encapsulation fundamentals
- JSON Serialization and Deserialization
- File Handling
- List Comprehensions
- Lists and Dictionaries
- Random Number and Character Generation
- String Manipulation
- Conditional Statements
- Exception Handling
- Data Validation
- In-memory Data Management
- Data Persistence

## 6. Current Project Status

**Implemented:** All six primary banking operations.

The application currently supports account creation, deposits, withdrawals, viewing account details, updating account information, and deleting accounts.


## 8. Project Objective

The main goal of this project is not just to build a banking application but also to understand how different Python concepts work together in a practical, real-world-style application.