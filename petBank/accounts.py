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
    def createAccount(self, owner_name):
        self.owner = owner_name
        self.balance = 0
        self.account_number = randint(1,9999)

