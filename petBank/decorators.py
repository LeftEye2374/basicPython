from functools import wraps
from typing import Callable
from exceptions import MyCustomException as ex

class Decorators:

    def log_transaction(func : Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f'func: {func.__name__} args: {args} kwargs: {kwargs}')
            result = func(*args, **kwargs)
            return result
        return wrapper


    def validate_positive_amount(amount : float):
        def wrapper(func : Callable):
            @wraps(func)
            def inner(*args, **kwargs):
                nonlocal amount
                if amount <= 0:
                    raise ex.NegativeAmountError(amount)
                res = func(*args, **kwargs)
                return res
            return inner
        return wrapper