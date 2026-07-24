n = 50_000_000


#Функция генератора, ключевое слово yield
def gen(n):
    for i in range(n):
        yield i ** 2


# Созданиек класса итератора
class Iter:
    def __init__(self, n):
        self.n = n
        self.current = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        if self.current >= self.n:
            raise StopIteration()
        return self.current


iterator = Iter(5)

print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())