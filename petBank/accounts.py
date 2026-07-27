import exceptions as ex

class Account:

    def __init__(self,owner, balance, account_number):
        self.owner = owner
        self.balance = balance
        self.account_number = account_number

    def deposit(self, amount, where_transfer, to_transfer):
        if where_transfer >= amount:
            raise ex.MyCustomException.InsufficientFundsError(self.owner)
        elif where_transfer < amount:
            raise ex.MyCustomException.NegativeAmountError(self.owner)
        elif amount < 1:
            raise ex.MyCustomException.AccountNotFoundError(self.owner)
        elif amount > 50_000:
            raise ex.MyCustomException.OverdraftLimitExceededError(self.owner)
        else:
            where_transfer -= amount
            to_transfer += amount
            print('Перевод успешно совершен')



    def get_owner(self):
        print(self.owner)
    def get_balance(self):
        print(self.balance)
    def get_account_number(self):
        print(self.account_number)
