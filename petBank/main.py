from bank import Bank
from exceptions import BankError

bank = Bank()

def start():
    print('Выберите опцию:')
    print('1. Все банковские счета')
    print('2. Перевести деньги')
    print('3. Положить на счет')
    print('4. Создать аккаунт')
    options = int(input())

    if options == 1:
       for number,account in bank.accounts.items():
           print(f"{account.get_owner()} / {account.get_account_number()}")
    elif options == 2:
        print("Введите номер счета откуда планируете перевести средства:")
        from_account = int(input())
        print("Введите номер счета куда планируете перевести средства:")
        to_account = int(input())
        print("Сумма: ")
        amount = int(input())
        try:
            bank.transfer(from_account, to_account, amount)
        except BankError as e:
            print(e.message())
    elif options == 3:
        print("Введите номер аккаунта: ")
        account_number = int(input())
        print("Введите сумму: ")
        amount = int(input())
        account = bank.accounts[account_number]
        account.deposit(amount)
    elif options == 4:
        print("Введите имя")
        owner = input()
        bank.open_account(owner)

print('Банк')
while True:
    start()