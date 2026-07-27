class MyCustomException(Exception):

    def InsufficientFundsError(self):
        print('Недостаточно средств на счете')

    def NegativeAmountError(self):
        print('Сумма не может быть меньше 1')

    def AccountNotFoundError(self):
        print('Не найден аккаунт для перевода')

    def OverdraftLimitExceededError(self):
        print('Нельзя уйти глубже лимита овердрафта')