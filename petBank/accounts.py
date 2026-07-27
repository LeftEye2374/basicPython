import exceptions as ex

class Account:

    def __init__(self,owner, balance, account_number):
        self.owner = owner
        self.balance = balance
        self.account_number = account_number

    def transfer(self, amount, where_transfer, to_transfer):
        if where_transfer < amount:
            raise ex.InsufficientFundsError("Недостаточно средств на счете")
        elif where_transfer <= 0:
            raise ex.NegativeAmountError("Сумма не может быть отрицательной")
        elif amount < 1:
            raise ex.AccountNotFoundError("Аккаунт не найден")
        elif amount > 50_000:
            raise ex.OverdraftLimitExceededError("Превышен лимит овердрафта")
        else:
            where_transfer -= amount
            to_transfer += amount
            print('Перевод успешно совершен')

    def deposit(self):
        ...

    def withdraw(self):
        ...


    def get_owner(self):
        return self.owner
    def get_balance(self):
        return self.balance
    def get_account_number(self):
        return self.account_number
