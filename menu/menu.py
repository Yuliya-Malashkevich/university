

from start.start import Start


def menu():
    start = Start()
    while True:
        type = int(input('МЕНЮ ВЫБОРА:' '\n' '1. Авторизация' '\n' '2. Регистрация' '\n'  'Выберите пункт: '))
        if type == 1:
            start.authorization()
        elif type == 2:
            start.registration()
        elif type == 0:
            exit(0)
        else:
            print('Error')
            menu()

menu()