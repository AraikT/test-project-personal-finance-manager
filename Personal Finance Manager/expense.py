from transactions import Transaction

class Expense(Transaction):
    def __init__(self, amount, date, description, category):
        super().__init__(amount, date, description)
        self.category = category

class OneTimePurchase(Expense):
    def __init__(self, amount, date, description, category):
        super().__init__(amount, date, description, category)


class Subscription(Expense):
    def __init__(self, amount, date, description, category):
        super().__init__(amount, date, description, category)