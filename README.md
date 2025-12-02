# Expense-Tracker

This is a basic Python Expense Tracker project built using simple concepts like loops, dictionaries, and user input. The purpose of this project is to help users record their daily expenses and get a quick summary directly from the terminal.

The program runs in a continuous loop until the user chooses the exit option. It displays a menu with four choices: adding an expense, viewing all expenses, calculating the total amount spent, and exiting the program.

When a user adds an expense, they are asked for the date, category, description, and amount. Each expense is stored as a dictionary, and all dictionaries are collected together so that they can be viewed and processed later.

The view option displays all the expenses that the user has added so far in a simple, numbered list. The calculate option goes through all stored expenses and adds up the total amount spent. This makes it easy for the user to track their spending without using any external tools.

This project is mainly for learning purposes. It helps beginners understand how to structure small programs, work with dictionaries, handle user inputs, and build simple menu-driven applications. There is a lot of room for improvement, such as saving expenses to a file, allowing modifications or deletions, generating reports, or even building a graphical interface later.

For now, it serves as a straightforward introduction to how expense tracking logic works in Python and gives a clear idea of how data can be handled inside a program without using any databases or external libraries.

If needed, this can be expanded further based on requirements.
THIS IS THE FORMAT OF OUTPUT:

======== MENU =======
1. Add Expense
2. View All Expenses
3. Calculate Total Amount Spent
4. EXIT

Enter your choice: 1
Enter date: 2025-11-26
Enter category of item: Food
Enter more details of item: Sandwich & juice
Enter the price: 120
Expense is added successfully!
