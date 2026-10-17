class BankAccount:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount <= 0:
            print("Please enter a valid amount.")
        else:
            self.balance += amount
            self.transactions.append(f"Deposited: Rs. {amount:.2f}")
            print(f"Rs. {amount:.2f} deposited successfully.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Please enter a valid amount.")
        elif amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdrawn: Rs. {amount:.2f}")
            print(f"Rs. {amount:.2f} withdrawn successfully.")

    def check_balance(self):
        print(f"Current Balance: Rs. {self.balance:.2f}")

    def show_details(self):
        print("\n--- Account Details ---")
        print(f"Account Holder: {self.name}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: Rs. {self.balance:.2f}")

    def transaction_history(self):
        print("\n--- Transaction History ---")
        if not self.transactions:
            print("No transactions yet.")
        else:
            for transaction in self.transactions:
                print(transaction)


def main():
    print("===== BANK ACCOUNT SIMULATOR =====")

    name = input("Enter account holder name: ").strip()
    while not name:
        print("Name cannot be empty.")
        name = input("Enter account holder name: ").strip()

    account_number = input("Enter account number: ").strip()
    while not account_number:
        print("Account number cannot be empty.")
        account_number = input("Enter account number: ").strip()

    account = BankAccount(name, account_number)

    while True:
        print("\n========== MAIN MENU ==========")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Account Details")
        print("5. Transaction History")
        print("6. Exit")
        print("===============================")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            try:
                amount = float(input("Enter deposit amount (Rs.): "))
                account.deposit(amount)
            except ValueError:
                print("Invalid input! Please enter a numeric amount.")

        elif choice == "2":
            try:
                amount = float(input("Enter withdrawal amount (Rs.): "))
                account.withdraw(amount)
            except ValueError:
                print("Invalid input! Please enter a numeric amount.")

        elif choice == "3":
            account.check_balance()

        elif choice == "4":
            account.show_details()

        elif choice == "5":
            account.transaction_history()

        elif choice == "6":
            print("Thank you for using the Bank Account Simulator!")
            break

        else:
            print("Invalid choice! Please select an option from 1 to 6.")


if __name__ == "__main__":
    main()