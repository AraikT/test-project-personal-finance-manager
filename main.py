from user import *

class PersonalFinanceManager:
    def __init__(self):
        self.users = []
        self.users_id = []

    @property
    def get_users_id(self):
        return self.users_id

    def create_user(self, user_id, username):
        new_user = User(user_id, username)
        self.users.append(new_user)
        self.users_id.append(new_user.get_user_id())
        return new_user

    def get_user(self, username):
        for user in self.users:
            if user.username == username:
                return user
        return None

    @property
    def get_users_transaction(self):
        # Return transactions for all users
        return [user.get_history_transactions() for user in self.users]

    def add_transaction_to_user(self, username, transaction):
        user = self.get_user(username)
        if user:
            user.add_transaction(transaction)
        else:
            print(f"User '{username}' not found.")

pf_manager = PersonalFinanceManager()
# Creating a user
hovsep = pf_manager.create_user(123, "Hovsep")
sona = pf_manager.create_user(234, "Sona")

# Creating transactions
income1 = Income(1000, "2023-01-01", "Salary")
expense1 = Expense(500, "2023-01-05", "Food")
one_time_purchase1 = OneTimePurchase(200, "2023-01-10", "Electronics")

income2 = Income(1200, "2023-01-01", "Salary")
expense2 = Expense(700, "2023-01-05", "Basseyn")
one_time_purchase2 = OneTimePurchase(600, "2023-01-10", "Clothes")

# Adding transactions to the hovsep and sona
hovsep.add_transaction(income1)
hovsep.add_transaction(expense1)
hovsep.add_transaction(one_time_purchase1)

pf_manager.add_transaction_to_user("Sona", income2)
pf_manager.add_transaction_to_user("Sona", expense2)
pf_manager.add_transaction_to_user("Sona", one_time_purchase2)
# Getting total income, expenses, and savings for the user
print("HOVSEP")
total_income = hovsep.get_total_income()
total_expenses = hovsep.get_total_expenses()
savings = hovsep.get_savings()
print("\nTotal Income:", total_income)
print("Total Expenses:", total_expenses)
print("Savings:", savings)

print("\n\nSONA")
total_income = sona.get_total_income()
total_expenses = sona.get_total_expenses()
savings = sona.get_savings()
print("\nTotal Income:", total_income)
print("Total Expenses:", total_expenses)
print("Savings:", savings)

# Accessing user transactions
transactions = pf_manager.get_users_transaction
id_s = pf_manager.get_users_id
print("\nUsers's ids: ", id_s)
print("Users transactions:",transactions)