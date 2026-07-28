import random
from accounts import Account
from bank import Bank



bank = Bank()
names = []
numbers = []

def start():
    print('Банк')
    print('Выберите опцию:')
    print('1. Все банковские счета')
    print('2. Перевести деньги')
    print('3. Положить на счет')
    print('4. Создать аккаунт')
    options = int(input())

    if options == 1:
       print('Список банковских счетов: ИМЯ / НОМЕР СЧЕТА ')
       for i in range(len(names)):
           print(f'{names[i]} / {numbers[i]}')
    elif options == 2:
        ...
    elif options == 3:
        print('Напишите номер счета на который хотите положить деньги: ')
        account_number = int(input())
        print('Напишите сумму: ')
        amount = float(input())
        print("Напишите номер счета с которого хотите перевести деньги: ")

    elif options == 4:
        print("Введите имя пользователя:")
        owner = input()
        account_number = random.randint(1, 1_000_000)
        account = Account(owner, 5, account_number)
        bank.accounts[account_number] = account
        names.append(account.get_owner())
        numbers.append(account.get_account_number())
while True:
    start()