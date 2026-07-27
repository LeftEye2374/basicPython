from typing import Callable
import time
from functools import wraps
from typing import Coroutine
import asyncio

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

def parametrized_timer_deco(func : Callable):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(f"Исполнение заняло - {end-start}")
        return res
    return wrapper

def limit_calls_deco(limit : int):
    def wrapper(func : Callable):
        @wraps(func)
        def inner(*args, **kwargs):
            nonlocal limit # Используется в основном в декоратарах
            if limit == 0:
                print("Нельзя вызвать функцию")
            res = func(*args, **kwargs)
            limit -= 1
            return res
        return inner
    return wrapper

def async_function_deco(coroutine : Coroutine):
    async def wrapper(*args, **kwargs):
        res = await coroutine(*args, **kwargs)
        return res
    return wrapper


@async_function_deco
async def my_async_function():
    await asyncio.sleep(0.5)
    return 1

@limit_calls_deco(2)
def my_function(sleep_second : int):
    """Очень важный докстринг"""
    time.sleep(sleep_second)
    return 124

print(asyncio.run(my_async_function()))
