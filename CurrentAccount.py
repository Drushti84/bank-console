from BankAccount import BankAccount

class CurrentAccount(BankAccount):
    def __init__(self, account_number, account_holder, initial_balance,withdrawal_fee):
        super().__init__(account_number,account_holder,initial_balance)
        self.withdrawal_fee = withdrawal_fee
        print(f"Withdrawal fee charged: {self.withdrawal_fee}. new balance: {self.current_balance}")

    def withdraw(self,amount):
        super().withdraw(amount)
        self.withdr()

    def withdr(self):
        self.current_balance = self.current_balance - self.withdrawal_fee
