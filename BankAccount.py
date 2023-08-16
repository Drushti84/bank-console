class BankAccount:
    def __init__(self,account_number,account_holder,initial_balance):
        self.account_number= account_number
        self.account_holder = account_holder
        self.current_balance=initial_balance
    def deposit(self, amount):
        if amount>0:
            self.current_balance +=amount
            print(f"Deposited {amount} into {self.account_holder}'s account. New balance: {self.current_balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self,amount):
        if 0<amount<=self.current_balance:
            self.current_balance -=amount
            print(f"Withdraw {amount} from {self.account_holder}'s account. New balance: {self.current_balance}")
        else:
            print("Insufficient balance or invalid withdrawal amount.")

    def check_balance(self):
        print(f"Current balance for {self.account_holder}'s account:{self.current_balance}")

    def transfer(self, amount, target_account):
        if 0<amount <= self.current_balance:
            self.current_balance -= amount
            target_account.deposit(amount)
            print(f"Transferred {amount} to {target_account.account_holder}'s account.")
            return 0
        else:
            print("Insufficient balance or invalid transfer amount. ")

