from BankAccount import BankAccount
from SavingAccount import SavingAccount
from CurrentAccount import CurrentAccount

class BankingApp:
    def __init__(self):
        self.accounts={}
        self.run()


    def create_bank_account(self):

        try:
            account_number = input("Enter Account number ")
            account_holder = input("Enter Account holder name")
            initial_balance = float(input(" Enter initial balance: "))
            account_type = input("Enter Account type (savings/current)")

            if account_type =="savings":
                interest_rate=float(input("Enter Interest rate:  "))
                account = SavingAccount(account_number, account_holder, initial_balance,interest_rate)
            elif account_type == "current":
                withdrawal_fee = float(input("Enter withdrawal fee: "))
                account =CurrentAccount(account_number,account_holder,initial_balance,withdrawal_fee)
            else:
                print("Invalid account type.")
                return

            self.accounts[account_number]=account
            print("Account created successfully. ")
        except ValueError:
            print("Invalid input . please enter valid data")


    def perform_transaction(self):
        try:
            sender_account_number = input("Enter sender account number ")
            if sender_account_number not in self.accounts:
                print("Sender not found")
                return

            recipient_account_number= input("Enter recipient account number")
            if recipient_account_number not in self.accounts:
                print("Recipient account not found.")
                return

            amount = float(input("Enter amount: "))
            sender_account= self.accounts[sender_account_number]
            recipient_account = self.accounts[recipient_account_number]

            if sender_account.transfer(amount,recipient_account) == 0:
                print("Transaction successful. ")
            else:
                print("Transaction failed")
        except ValueError:
            print("Invalid input Please enter valid data. ")

    def show_balance(self):
        try:
            account_number = input("Enter account number")
            if account_number in self.accounts:
                account = self.accounts[account_number]
                account.check_balance()
            else:
                print("Account not found")
        except ValueError:
            print("Invalid inoput please enter valid input")

    def perform_banking_operation(self):
        try:
            accont_number = input("Enter account number")

            if accont_number not in self.accounts:
                print("Account not found. ")
                return

            account = self.accounts[accont_number]
            print("1. Deposit")
            print("2. Withdraw")

            choice = input("Enter Your choice")

            if choice == "1":
                amount = float(input("Enter Deposit amount"))
                account.deposit(amount)
                print("Successfully Deposited")
            elif choice == "2":
                amount = float(input("Enter Withdraw amount "))
                account.withdraw(amount)
                print("Successfully withdraw")
            else:
                print("Invalid input please inter valid data")
        except ValueError:
            print("Invalid input  PLease enter valid Input")


    def run(self):
        while True:
            print("\nMenu: ")
            print("1. Create Bank Account")
            print("2. Perform Transaction")
            print("3. Banking Operation (Deposit/withdraw)")
            print("4. Check Balance")
            print("5. Exit")

            choice = input("Enter your choice")

            if choice =="1":
                self.create_bank_account()
            elif choice == "2":
                self.perform_transaction()
            elif choice == "3":
                self.perform_banking_operation()
            elif choice == "4":
                self.show_balance()
            elif choice == "5":
                break
            else:
                print("Invalid choice Please try again")


if __name__ == "__main__":
    app = BankingApp()