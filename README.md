Personal Expense Tracker:
This is a simple Python tool to help you track your expenses. Add expenses, view them in a neat list, or see a summary of your spending by category. Everything is saved in a local expenses.txt file.
Features

Add Expenses: Log date, amount, category, and description.
View Expenses: See all expenses in a clear table.
Category Summary: Check total spending per category.

Requirements:
Python: Python 3.10 or higher (download from python.org).
Operating System: Windows 10 or higher.

Setup:
Save the expense_tracker.py script to a folder.
No extra libraries needed—just Python!

How to Use:
Open your terminal and go to the script’s folder.
Run:python expense_tracker.py


Choose from the menu:
1. Add expense: Enter date (YYYY-MM-DD), amount, category, and description.
2. View expenses: See all expenses in a table.
3. Summary by category: View spending totals by category.
4. Exit: Quit the program.



Example:
Run the script, and you’ll see:
Personal Expense Tracker
1. Add expense
2. View expenses
3. Summary by category
4. Exit
Choose an option: 

Add an expense (option 1):
Date (YYYY-MM-DD): 2025-08-20
Amount: 15.99
Category: Snacks
Description: Coffee shop

Output: Expense added!
View expenses (option 2):
Date       | Amount  | Category   | Description
-----------------------------------------------
2025-08-20 | 15.99   | Snacks     | Coffee shop

Category summary (option 3):
Category-wise Expense Summary:
Snacks: 15.99

Notes:
Expenses are saved in expenses.txt in the same folder as the script.
If no expenses exist, you’ll get a message saying so.
Use valid inputs (e.g., numbers for amounts) to avoid errors.
