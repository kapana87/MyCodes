class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError('На счете недостаточно средств')
        self._balance -= amount

    def transfer(self, account, amount):
        self.withdraw(amount)
        account.deposit(amount)


account = BankAccount()

print(account.get_balance())
account.deposit(100)
print(account.get_balance())
account.withdraw(50)
print(account.get_balance())

print()

account = BankAccount(100)

try:
    account.withdraw(150)
except ValueError as e:
    print(e)