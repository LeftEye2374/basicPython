n = 50_000_000


#Функция генератора, ключевое слово yield
def gen(n):
    for i in range(n):
        yield i ** 2

print(sum(gen(n)))
