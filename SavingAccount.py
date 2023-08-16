from BankAccount import  BankAccount

class SavingAccount(BankAccount):
    def __init__(self,account_number, account_holder, initial_balance, interest_rate):
        super().__init__(account_number, account_holder, initial_balance)
        self.interest_rate=interest_rate

    def deposit(self,amount):
        super().deposit(amount)
        self.add_interest()

    def add_interest(self):
        interest_amount =self.current_balance*(self.interest_rate/100)
        self.current_balance += interest_amount
    