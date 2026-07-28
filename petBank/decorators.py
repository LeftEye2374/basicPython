from functools import wraps
from typing import Callable
import exceptions as ex

class Decorators:

    def log_transaction(func : Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f'func: {func.__name__} args: {args} kwargs: {kwargs}')
            result = func(*args, **kwargs)
            return result
        return wrapper



    def validate_positive_amount(func: Callable):
        @wraps(func)
        def inner(*args, **kwargs):
            # Сначала ищем именованный аргумент amount
            if "amount" in kwargs:
                amount = kwargs["amount"]
            else:
                # Предполагаем, что amount — первый позиционный аргумент
                amount = args[-1]

            if amount <= 0:
                raise ex.NegativeAmountError(amount)

            return func(*args, **kwargs)

        return inner