# Expense Tracker

A command-line expense tracking application built with Python. It allows users to add, view, update, delete, and calculate expenses while storing the data permanently in a CSV file.

## Features

* Add new expenses
* Automatically assign unique expense IDs
* Store the date of each expense
* View all expenses in a formatted table
* Calculate total expenses
* Update an existing expense
* Delete an expense by ID
* Input validation for invalid values
* Save expenses to a CSV file
* Load saved expenses when the program starts
* Handle missing or invalid CSV data
* Persistent data across program restarts

## Technologies Used

* Python
* CSV
* File Handling
* Exception Handling
* Functions
* Lists and Dictionaries
* Input Validation

## How to Run

1. Make sure Python is installed.
2. Clone or download this repository.
3. Open the project folder in a terminal.
4. Run:

```bash
python expenses.py
```

## Data Storage

Expense data is stored in `expenses.csv`.

Example:

```text
id,date,category,amount
1,2026-08-12,Food,250
2,2026-08-12,Transport,100
3,2026-08-12,Movie,300
```

## Example

```text
========================================
          EXPENSE TRACKER
========================================

1. ADD EXPENSE
2. VIEW EXPENSES
3. TOTAL EXPENSES
4. UPDATE EXPENSE
5. DELETE EXPENSE
6. EXIT
```

The application provides a simple command-line interface for managing personal expenses.

## What I Learned

Through this project, I practiced:

* Python functions
* Lists and dictionaries
* Loops and conditional statements
* Exception handling
* CSV file reading and writing
* Data validation
* Persistent data storage
* Organizing a Python application
* Using Git and GitHub for project management
