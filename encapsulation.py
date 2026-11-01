class Bank:
    def __init__(self, acc_holder_name: str, balance: int):
        self.name = acc_holder_name
        self.__balance = balance

    def deposite(self, amount: int):
        self.__balance += amount
        print(f"amount deposited, current balance is {self.__balance}\n")

    def withdraw(self, amount: int):
        if amount > self.__balance:
            print("Not enough money to withdraw !")
        else:
            self.__balance -= amount
            print(f"Amount withdrawn, current balance is {self.__balance}\n")

    # setter method to see only the private data, but can not modified/access outside the class

    def get_balance(self):
        print(f"current balance is: {self.__balance}")

# instances

acc = Bank("Brajesh Das", 1000)
acc.deposite(4000)
acc.balance = 50000             # doesn't make any sense because, balance is now private and can't access outside the class
acc.withdraw(500)
acc.get_balance()
