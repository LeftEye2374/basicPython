from typing import Callable
import time

# my_func = deco(my_function()) # Пример применения декоратора без @

# Декоратор - это паттерн программирования который позволяет
# добавлять новый функционал фукции, не видоизменяя эту функцию


def empty_deco(func : Callable):
    def wrapper():
        res = func()
        return res
    return wrapper

def timer_deco(func : Callable):
    def wrapper():
        start = time.time()
        res = func()
        time.sleep(3) # Просто чтобы добавить времени
        end = time.time()
        print(f"Исполнение заняло - {end-start}")
        return res
    return wrapper

@timer_deco
def my_function():
    return 124

print(my_function())