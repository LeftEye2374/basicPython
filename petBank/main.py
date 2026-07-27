from accounts import Account

bank_accounts = []

def start():
    print('Банк')
    print('Выберите опцию:')
    print('1. Все банковские счета')
    print('2. Проверить банковский счет')
    print('3. Отправить деньги')
    print('4. Создать аккаунт')
    options = int(input())

    if options == 1:
        for i in bank_accounts:
            print(i.owner)
            print(i.balance)
            print(i.account_number)
            print('_____________')
    elif options == 2:
        ...
    elif options == 3:
        ...
    elif options == 4:
        print('Введите имя пользователя:')
        owner = str(input())
        account = Account.createAccount(owner)
        bank_accounts.append(account)

while True:
    start()