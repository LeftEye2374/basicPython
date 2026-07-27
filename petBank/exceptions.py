class BankError(Exception):

    def __init__(self, message):
        self.message = message


class InsufficientFundsError(BankError):

    def __init__(self, message):
        super().__init__(message)

class NegativeAmountError(BankError):
    def __init__(self, message):
        super().__init__(message)

class AccountNotFoundError(BankError):
    def __init__(self, message):
        super().__init__(message)

class OverdraftLimitExceededError(BankError):
    def __init__(self, message):
        super().__init__(message)