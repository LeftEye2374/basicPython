# Напишите декоратор котоырй логирует вызов функции с помощью print()
from functools import wraps
from typing import Callable

def log_func(func : Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'func: {func.__name__} args: {args} kwargs: {kwargs}')
        result = func(*args, **kwargs)
        return result
    return wrapper
