import exceptions as ex
from decorators import Decorators

class Account:

    def __init__(self,owner, balance, account_number):
        self.owner = owner
        self.balance = balance
        self.account_number = account_number
        self._transactions = []

    """ Методы класса """

    @Decorators.log_transaction
    @Decorators.validate_positive_amount
    def deposit(self, amount):
        if amount < 0:
            raise ex.NegativeAmountError("Сумма не может быть отрицательной")
        self.balance += amount
        self._transactions.append((self.owner, self.balance, amount))

    @Decorators.log_transaction
    @Decorators.validate_positive_amount
    def withdraw(self, amount):
        if amount < 0:
            raise ex.NegativeAmountError("Сумма не может быть отрицательной")
        if self.balance < amount:
            raise ex.InsufficientFundsError("Не достаточно средств")
        self.balance -= amount
        self._transactions.append((self.owner, self.balance, amount))

    def transaction_history(self):
        yield from self._transactions




    """ Геттеры для работы с классом"""
    def get_owner(self):
        return self.owner
    def get_balance(self):
        return self.balance
    def get_account_number(self):
        return self.account_number


class SavingAccount(Account):

    def __init__(self, owner, balance, account_number):
        super().__init__(owner, balance, account_number)

    def apply_interest(self):
        ...

class CheckingAccount(Account):

    def __init__(self, owner, balance, account_number, overdraft_limit):
        super().__init__(owner, balance, account_number)
        self.overdraft_limit = overdraft_limit

    @Decorators.log_transaction
    @Decorators.validate_positive_amount
    def withdraw(self, amount):
        if amount < 0:
            raise ex.NegativeAmountError("Сумма не может быть отрицательной")
        if self.balance - amount < -self.overdraft_limit:
            raise ex.OverdraftLimitExceededError("Превышен лимит овердрафта")
        self.balance -= amount
        self._transactions.append((self.owner, self.balance, amount))
