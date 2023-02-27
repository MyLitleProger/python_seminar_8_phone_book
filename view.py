def clear():
    """Очистка рабочей области экрана"""
    return print('\n' * 500)


def first_menu():
    """Начальное меню"""
    print('''\n Меню:
    1. Открыть файл
    2. Выход''')
    while True:
        try:
            choice = int(input('Выберите пункт меню: '))
            if 0 < choice < 3:
                clear()
                return choice
            else:
                print('Введите число от 1 до 2')
        except ValueError:
            print('Некорректный ввод!')


def general_menu():
    """Главное меню"""
    print('''\n Главное меню:
    1. Сохранить файл
    2. Показать контакты
    3. Добавить контакт
    4. Изменить контакт
    5. Найти контакт
    6. Удалить контакт
    7. Выход''')
    while True:
        try:
            choice = int(input('Выберите пункт меню: '))
            if 0 < choice < 8:
                clear()
                return choice
            else:
                print('Введите число от 1 до 7')
        except ValueError:
            print('Некорректный ввод!')


def show(data: list[dict]):
    """Показать контакты"""
    if data:
        for i, content in enumerate(data, 1):
            print(f'{i}. {content.get("name"):20} {content.get("phone"):<15} {content.get("comment"):<20}')
        input('\nНажмите Enter что бы продолжить\n')
        clear()
    else:
        print('Файл пуст')
        input('\nНажмите Enter что бы продолжить\n')
        clear()


def add_user():
    """Добавить контакт"""
    name = input('Введите имя и фамилию: ')
    phone = input('Введите номер телефона: ')
    comment = input('Введите комментарий: ')
    new_user = {'name': name,
                'phone': phone,
                'comment': comment}
    clear()
    return new_user


def search_contact():
    """Поиск контакта"""
    find = input('Введите искомый элемент: ')
    clear()
    return find


def input_id():
    """Передает индекс контакта"""
    index = int(input('Введите индекс: '))
    clear()
    return index


def confirm(condition: str, name: str):
    """Подтверждение решения"""
    answer = input(f'Вы действительно хотите {condition} контакт {name}? (y/n): ')
    clear()
    return True if answer == 'y' else False


def confirm_changes():
    """Предупреждение о несохраненных данных"""
    answer = input('У вас есть несохраненные изменения, хотите их сохранить? (y/n): ')
    clear()
    return True if answer == 'y' else False
