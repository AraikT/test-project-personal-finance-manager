from transactions import Transaction

class Income(Transaction):
    def __init__(self, amount, date, description, source):
        super().__init__(amount, date, description)
        self.source = source

class OneTimePayment(Income):
    def __init__(self, amount, date, description, source):
        super().__init__(amount, date, description, source)


class Salary(Income):
    def __init__(self, amount, date, description, source):
        super().__init__(amount, date, description, source)