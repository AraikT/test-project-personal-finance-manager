import re
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def check_valid(f):
    def wrapper(self, *args, **kwargs):
        if self.is_valid_user():
            print(f'User {self.generate_username()} is valid')
            return f(self, *args, **kwargs)
        else:
            print(f'User is not valid. Access denied.')

    return wrapper

class User:
    def __init__(self, name, surname, age, phone_number, email, password):
        self.name = name
        self.surname = surname
        self.age = age
        self.phone_number = phone_number
        self.email = email
        self.password = password
        self.income = {'total_income': 0}
        self.expenses = {'total_expenses': 0}

    def is_valid_user(self):
        # Add additional validation logic as needed
        return self.is_valid_email(self.email) and self.is_valid_password(self.password)

    def is_valid_email(self, email):
        pattern = re.compile(r"[^@]+@[^@]+\.[^@]+")
        return bool(re.match(pattern, email))

    def is_valid_password(self, password):
        # Basic password validation (add  validation as needed)
        return password is not None

    def generate_username(self):
        return f"{self.name.lower()}_{self.surname.lower()}_{self.age}"

    @check_valid
    def add_income(self, amount):
        self.income['total_income'] += amount

    @check_valid
    def add_expense(self, category, amount):
        if category not in self.expenses:
            self.expenses[category] = 0
        self.expenses[category] += amount
        self.expenses['total_expenses'] += amount

   
    def calculate_total_income(self):
        return self.income['total_income']

    def calculate_total_expenses(self):
        return self.expenses['total_expenses']

    def calculate_savings(self):
        return self.income['total_income'] - self.expenses['total_expenses']

    def categorize_expenses(self):
        return {category: amount for category, amount in self.expenses.items() if category != 'total_expenses'}

# Example Usage:
user_name = input("Enter your name: ")
user_surname = input("Enter your surname: ")
user_age = int(input("Enter your age: "))
user_phone_number = input("Enter your phone number: ")
user_email = input("Enter your email address: ")
user_password = input("Enter your password: ")

try:
    user = User(user_name, user_surname, user_age, user_phone_number, user_email, user_password)
except ValueError as e:
    print(f"Error: {e}")
    exit()

# Now you can use `user` object to perform financial tasks
# ...

# Adding income
user.add_income(500)

# Adding expenses
user.add_expense('food', 50)
user.add_expense('clothes', 30)

# Displaying results
print(f'Total Income: {user.calculate_total_income()}')
print(f'Total Expenses: {user.calculate_total_expenses()}')
print(f'Savings: {user.calculate_savings()}')
print('Categorized Expenses:', user.categorize_expenses())

# Visualizing Expenses
expenses_data = user.categorize_expenses()
categories = list(expenses_data.keys())
amounts = list(expenses_data.values())

# Check if the lists are not empty before plotting
if categories and amounts:
    plt.figure(figsize=(10, 6))
    sns.barplot(x=categories, y=amounts)
    plt.title('Daily Expenses')
    plt.xlabel('Expense Categories')
    plt.ylabel('Amount Spent')
    plt.show()
else:
    print("No data to visualize.")

# Print generated user name for finance manager
print(f'Generated User Name for Finance Manager: {user.generate_username()}')
