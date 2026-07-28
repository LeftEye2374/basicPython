import random

from accounts import Account


class Bank:

    def __init__(self):
        self.accounts : dict[int, Account] = {}

    def open_account(self, owner):
        account_number = random.randint(1, 1_000_000)
        account = Account(owner,0, account_number)
        self.accounts[account_number] = account
        return account_number

    def get_account(self, account_number):
        return self.accounts[account_number]

    def deposit(self, from_number, to_number, amount):
        from_account = self.get_account(from_number)
        to_account = self.get_account(to_number)
        from_account.get_balance -= amount
        to_account.get_balance += amount
        