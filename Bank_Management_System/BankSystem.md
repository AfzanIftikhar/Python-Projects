# Bank Management System – Python Project

## Project Overview

I am developing a **Bank Management System** using Python. The primary objective of this project is to strengthen my understanding of Python concepts, particularly Object-Oriented Programming (OOP), file handling, JSON serialization and deserialization, data management, and exception handling.

The application will provide a menu-driven interface through which users can create and manage their bank accounts. All account information will be stored in a `data.json` file to ensure data persistence between program executions.

## Technologies and Modules

The following Python modules and libraries will be used:

- `random` – To generate random values where required.
- `json` – To serialize and deserialize account data.
- `string` – To work with letters and characters when generating account-related identifiers.
- `pathlib.Path` – To check whether the JSON data file exists and manage file paths.

---

## Development Roadmap

### Step 1: Menu System and Data Initialization

The first step is to create a menu-driven interface that allows users to interact with the banking system.

The application will provide the following options:

| Option | Functionality |
|---|---|
| 1 | Create a new bank account |
| 2 | Deposit money |
| 3 | Withdraw money |
| 4 | View account details |
| 5 | Update account details |
| 6 | Delete a bank account |

#### Data Persistence and Initialization

I will use a `data.json` file to store all bank account information.

Whenever the program starts, the following process will take place:

1. Check whether `data.json` exists using `Path`.
2. If the file exists, open it in read mode.
3. Load the existing JSON data into a Python list using `json.load()`.
4. If the file does not exist, initialize an empty Python list.
5. Use this Python list as temporary storage (in-memory data) throughout the program's execution.

#### Data Modification and Saving

All account-related operations will initially be performed on the Python list rather than directly modifying the JSON file.

For example:

- Creating an account will add a new record to the list.
- Depositing money will update the account balance in the list.
- Withdrawing money will deduct the requested amount from the account balance.
- Updating details will modify the relevant account information.
- Deleting an account will remove the corresponding record from the list.

After making the required changes, the updated Python list will be saved back into `data.json` using `json.dump()`.

This approach will maintain a clear separation between in-memory data management and permanent file storage.

### Step 2: Account Creation

After completing the menu system and data initialization, I will implement the account creation functionality.

Further implementation details will be documented as development progresses.

---

## Project Status

- **Current Stage:** Step 1 – Menu System and Data Initialization.
- **Next Goal:** Implement the bank account creation functionality.

## Learning Objectives

Through this project, I aim to practise:

- Python Object-Oriented Programming.
- File handling and data persistence.
- JSON serialization and deserialization.
- Working with lists and dictionaries.
- Data validation and exception handling.
- Implementing real-world banking operations.
- Writing clean and maintainable Python code.