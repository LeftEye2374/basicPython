import exceptions as ex

class Account:

    def __init__(self,owner, balance, account_number):
        self.owner = owner
        self.balance = balance
        self.account_number = account_number

    """ Методы класса """

    def deposit(self, amount):
        if amount < 0:
            raise ex.NegativeAmountError("Сумма не может быть отрицательной")
        self.balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise ex.NegativeAmountError("Сумма не может быть отрицательной")
        if self.balance < amount:
            raise ex.InsufficientFundsError("Не достаточно средств")
        self.balance -= amount



    """ Геттеры для работы с классом"""
    def get_owner(self):
        return self.owner
    def get_balance(self):
        return self.balance
    def get_account_number(self):
        return self.account_number
