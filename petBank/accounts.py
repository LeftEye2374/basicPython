from random import random
from random import randint

class Account:

    def __init__(self,owner, balance, account_number):
        self.owner = owner
        self.balance = balance
        self.account_number = account_number

    def deposit(self,amount : float):
        self.balance += amount

    @classmethod
    def create_account(cls,owner_name):
        account_number = randint(1,9999)
        account = Account(owner_name,account_number,account_number)
        return account



    def get_owner(self):
        print(self.owner)
    def get_balance(self):
        print(self.balance)
    def get_account_number(self):
        print(self.account_number)
