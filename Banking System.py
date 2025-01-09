import random
from datetime import datetime


class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.add_transaction(f"Deposited: ${amount}")
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        elif amount > 0:
            self.balance -= amount
            self.add_transaction(f"Withdrew: ${amount}")
        else:
            print("Withdrawal amount must be greater than zero.")

    def check_balance(self):
        return self.balance

    def add_transaction(self, description):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.transactions.append(f"{timestamp} - {description}")

    def print_statement(self):
        print(f"\nStatement for {self.account_holder} (Account {self.account_number}):")
        for transaction in self.transactions:
            print(transaction)
        print(f"Current Balance: ${self.balance}\n")


class Bank:
    def __init__(self):
        self.accounts = {}
        self.total_deposits = 0

    def generate_account_number(self):
        """Generate a unique 3-digit account number."""
        while True:
            account_number = random.randint(100, 999)
            if account_number not in self.accounts:
                return account_number

    def open_account(self, account_holder):
        account_number = self.generate_account_number()
        new_account = BankAccount(account_number, account_holder)
        self.accounts[account_number] = new_account
        print(f"Account created for {account_holder} with Account Number: {account_number}")

    def get_account_by_credentials(self, account_holder, account_number):
        account = self.accounts.get(account_number)
        if account and account.account_holder == account_holder:
            return account
        raise ValueError("Invalid account holder name or account number.")

    def transfer(self, sender_account, receiver_account_number, amount):
        try:
            receiver_account = self.accounts.get(receiver_account_number)
            if not receiver_account:
                raise ValueError(f"Account number {receiver_account_number} not found.")

            if sender_account.balance >= amount:
                sender_account.withdraw(amount)
                receiver_account.deposit(amount)
                sender_account.add_transaction(
                    f"Transferred ${amount} to Account {receiver_account_number}"
                )
                receiver_account.add_transaction(
                    f"Received ${amount} from Account {sender_account.account_number}"
                )
            else:
                print("Transfer failed: Insufficient balance in sender's account.")
        except ValueError as error:
            print(error)

    def admin_check_total_deposit(self):
        self.total_deposits = sum(account.check_balance() for account in self.accounts.values())
        return self.total_deposits

    def admin_check_total_accounts(self):
        return len(self.accounts)


def main():
    bank = Bank()

    while True:
        print("\nBanking System Menu:")
        print("1. Open Account")
        print("2. Log In")
        print("3. Admin: Check Total Deposits")
        print("4. Admin: Check Total Accounts")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            account_holder = input("Enter account holder name: ")
            bank.open_account(account_holder)
        elif choice == 2:
            account_holder = input("Enter account holder name: ")
            account_number = int(input("Enter account number: "))
            try:
                account = bank.get_account_by_credentials(account_holder, account_number)
                user_menu(bank, account)
            except ValueError as error:
                print(error)
        elif choice == 3:
            total_deposits = bank.admin_check_total_deposit()
            print(f"Total Deposits in the Bank: ${total_deposits}")
        elif choice == 4:
            total_accounts = bank.admin_check_total_accounts()
            print(f"Total Number of Accounts: {total_accounts}")
        elif choice == 5:
            print("Exiting the system. Have a great day!")
            break
        else:
            print("Invalid choice. Please try again.")


def user_menu(bank, account):
    while True:
        print(f"\nWelcome, {account.account_holder} (Account {account.account_number})")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Transfer Money")
        print("5. Print Statement")
        print("6. Log Out")

        user_choice = int(input("Enter your choice: "))

        if user_choice == 1:
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif user_choice == 2:
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif user_choice == 3:
            print(f"Your balance is: ${account.check_balance()}")
        elif user_choice == 4:
            receiver_account_number = int(input("Enter receiver's account number: "))
            amount = float(input("Enter amount to transfer: "))
            bank.transfer(account, receiver_account_number, amount)
        elif user_choice == 5:
            account.print_statement()
        elif user_choice == 6:
            print("Logging out. Have a great day!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
