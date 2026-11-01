'''
Create a BankAccount class that manages a customer's bank account.
The account balance must be private, and users should interact with it through methods.

Requirements :

1. Initialize the account holder's name and opening balance.
2. Implement deposit(amount) to add money.
3. Implement withdraw(amount) to withdraw money if sufficient funds are available.
4. Implement get_balance() to return the current balance.
5. Reject deposits and withdrawals that are zero or negative.
6. Display appropriate messages for successful and unsuccessful transactions.
'''

class Bank_account:
    def __init__(self, acc_holder_name: str, acc_balance: int):
        self.name = acc_holder_name
        self.__balance = acc_balance

    # method for deposite:

    def deposite(self, dep_amount: int):
        if dep_amount <= 0:
            print("Invalid deposite amount")
        else:
            self.__balance += dep_amount
            print(f"Deposited amount is: {dep_amount}")

    # method for withdrawl:

    def withdraw(self, with_amount):
        if with_amount <= 0:
            print("Invalid withdraw amount")
        elif with_amount > self.__balance:
            print("Insufficent balance")
        else:
            self.__balance -= with_amount
            print(f"amount {with_amount} withdraw successfully")

    # method for balance check by getter:

    def get_balance(self):
        return self.__balance


# Instances

account = Bank_account("Brajesh Das", 1000)
account.deposite(1000)
account.withdraw(500)
print("Account holder name:", account.name)
print("Current Balance is:", account.get_balance())