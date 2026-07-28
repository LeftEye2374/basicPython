from accounts import Account


class Bank:

    def __init__(self):
        self.accounts : dict[int, Account] = {}
        
