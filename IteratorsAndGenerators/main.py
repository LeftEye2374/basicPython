# первый вариант = генератор - список - список
n = 10000
z = []
x = list(range(n))

for i in x:
    z.append(i ** 2)
print(sum(z))


#вариант два генератор список итератор список
y = map(lambda val: val ** 2, x)
print(sum(y))

#вариант три генератор список иттератор
sum = 0

for i in x:
    sum += i ** 2
print(sum)
