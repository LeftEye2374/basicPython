from bank import Bank

bank_accounts = Bank.__init__()


def start():
    print('Банк')
    print('Выберите опцию:')
    print('1. Все банковские счета')
    print('2. Перевести деньги')
    print('3. Положить на счет')
    print('4. Создать аккаунт')
    options = int(input())

    if options == 1:
       print('Список банковских счетов: ФИО / НОМЕР СЧЕТА ')
       for i in range(bank_accounts.accounts.count()):
#            print(f'{} / {}')
        ...
    elif options == 2:
        ...
    elif options == 3:
        print('Напишите номер счета на который хотите положить деньги: ')
        account_number = int(input())
        print('Напишите сумму: ')
        amount = float(input())
        print("Напишите номер счета с которого хотите перевести деньги: ")

    elif options == 4:

      ...

while True:
    start()