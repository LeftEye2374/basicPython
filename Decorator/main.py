from typing import Callable

# my_func = deco(my_function()) # Пример применения декоратора без @

# Декоратор - это паттерн программирования который позволяет
# добавлять новый функционал фукции, не видоизменяя эту функцию


def empty_deco(func : Callable):
    def wrapper():
        res = func()
        return res
    return wrapper

@empty_deco
def my_function():
    return 124

print(my_function())