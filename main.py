from user import *

class PersonalFinanceManager:
    def __init__(self):
        self.users_id = []
    def users_list(self):
        return self.users_id
    def create_user(self, user_id, username):
        new_user = User(user_id, username)
        self.users_id.append(new_user.get_user_id())
        return new_user

    def get_user(self, username):
        for user in self.users:
            if user.username == username:
                return user
        return None

    def add_transaction_to_user(self, username, transaction):
        user = self.get_user(username)
        if user:
            user.add_transaction(transaction)
        else:
            print(f"User '{username}' not found.")
# Creating a PersonalFinanceManager
pf_manager = PersonalFinanceManager()

# Creating a user
user1 = pf_manager.create_user(123, "HOvsep")
user2 = pf_manager.create_user(234, "Sona")
# Creating transactions
# income1 = Income(1000, "2023-01-01", "Salary", "Job")
# expense1 = Expense(500, "2023-01-05", "Groceries", "Food")
# one_time_purchase1 = OneTimePurchase(200, "2023-01-10", "New headphones", "Electronics")
# income2 = Income(10000, "2023-01-01", "Salary", "Job")
# expense2 = Expense(700, "2023-01-05", "Groceries", "Food")
# one_time_purchase2 = OneTimePurchase(900, "2023-01-10", "New headphones", "Electronics")


# # Adding transactions to the user1
# user1.add_transaction(income1)
# user1.add_transaction(expense1)
# user1.add_transaction(one_time_purchase1)

# # Adding transactions to the user2
# user2.add_transaction(income2)
# user2.add_transaction(expense2)
# user2.add_transaction(one_time_purchase2)
# # Getting all transactions for the user1
# all_transactions = user1.get_transactions()
# print("All Transactions for user1:")
# for transaction in all_transactions:
#     print(transaction.amount, transaction.date, transaction.description)

# # Getting total income, expenses, and savings for the user
# total_income = user1.get_total_income()
# total_expenses = user1.get_total_expenses()
# savings = user1.get_savings()

# print("\nTotal Income:", total_income)
# print("Total Expenses:", total_expenses)
# print("Savings:", savings)


# # Getting all transactions for the user2
# all_transactions = user2.get_transactions()
# print("All Transactions for user1:")
# for transaction in all_transactions:
#     print(transaction.amount, transaction.date, transaction.description)

# # Getting total income, expenses, and savings for the user
# total_income = user2.get_total_income()
# total_expenses = user2.get_total_expenses()
# savings = user2.get_savings()

# print("\nTotal Income:", total_income)
# print("Total Expenses:", total_expenses)
# print("Savings:", savings)
print(pf_manager.users_list())