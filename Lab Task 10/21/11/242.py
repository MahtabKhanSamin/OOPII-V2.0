class InsufficientBalance(Exception):
    pass

class BankAccount:
    def __init__(self,a):
        self.balance=a
    def withdraw(self,a):
        if self.balance<a:
            raise InsufficientBalance
        else:
            print(self.balance - a)
            self.balance-=a
    def display(self):
        print("Current Balance: ",self.balance)
try:
    b=BankAccount(5000)
    b.withdraw(7000)
except InsufficientBalance:
    print("You don't enough money to withdraw you noob")