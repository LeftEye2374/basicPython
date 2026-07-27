import time
from functools import lru_cache
from contextlib import contextmanager

@lru_cache   # Встроенный декоратор из : from functools import lru_cache
def my_long_calc():
    time.sleep(3)
    return 42

print(my_long_calc()) # Первый вызов считала функция
print(my_long_calc()) # Вызов из оперативной памяти
print(my_long_calc()) # Вызов из оперативной памяти

@contextmanager
def ctx_manager():
    print('hello')
    yield
    print('end')

    
with ctx_manager() as man:
    print('123')