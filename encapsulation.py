class Account:
    def __init__(self, balance, account):
        self.balance = balance
        self.account = account

    def debit(self, amount):
        self.balance += amount

    def credit(self, amount):
        self.balance -= amount

ac1 = Account(1000200, 50701)
print(ac1.balance)
print(ac1.account)
ac1.debit(100)
print(ac1.balance)
ac1.credit(500)
print(ac1.balance,'\n',ac1.account)

