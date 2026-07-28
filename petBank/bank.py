import random

from accounts import Account
from exceptions import AccountNotFoundError

class Bank:

    def __init__(self):
        self.accounts : dict[int, Account] = {}

    def open_account(self, owner):
        account_number = random.randint(1, 1_000_000)
        account = Account(owner,0, account_number)
        self.accounts[account_number] = account
        return account_number

    def get_account(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]
        else:
            raise AccountNotFoundError("Аккаунт не найден")

    def transfer(self, from_number, to_number, amount):
        from_account = self.get_account(from_number)
        to_account = self.get_account(to_number)
        from_account.withdraw(amount)
        to_account.deposit(amount)
        