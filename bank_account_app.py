class BankAccount:
    def __init__(self, account_number, holder, balance=0):
        self.__account_number = account_number
        self.__holder = holder
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposit of ${amount:.2f} successful!")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance.")
        elif amount > 0:
            self.__balance -= amount
            print(f"Withdrawal of ${amount:.2f} successful!")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        return self.__balance

def main():
    account = None
    while True:
        print("\n--------------------")
        print("Welcome to the Bank!")
        print("--------------------")
        print("Choose an option:")
        print("1. Create account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check balance")
        print("5. Exit")

        option = int(input("Enter your choice: "))

        if option == 1:
            account_number = int(input("Enter account number: "))
            holder = input("Enter account holder name: ")
            initial_balance = float(input("Enter initial balance: "))
            account = BankAccount(account_number, holder, initial_balance)
            print("Account created successfully!")

        elif option == 2:
            if account:
                amount = float(input("Enter deposit amount: "))
                account.deposit(amount)
            else:
                print("Create an account before making a deposit.")

        elif option == 3:
            if account:
                amount = float(input("Enter withdrawal amount: "))
                account.withdraw(amount)
            else:
                print("Create an account before making a withdrawal.")

        elif option == 4:
            if account:
                print(f"Current balance is: ${account.check_balance():.2f}")
            else:
                print("Create an account before checking the balance.")

        elif option == 5:
            print("Thank you for using our bank!")
            break

        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
