def general_menu():
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
                return choice
            else:
                print('Введите число от 1 до 7')
        except ValueError:
            print('Некорректный ввод!')


def first_menu():
    print('''\n Меню:
    1. Открыть файл
    2. Выход''')
    while True:
        try:
            choice = int(input('Выберите пункт меню: '))
            if 0 < choice < 3:
                return choice
            else:
                print('Введите число от 1 до 2')
        except ValueError:
            print('Некорректный ввод!')


def show_content(data: list[dict]):
    if not data:
        print('Файл пуст')
    else:
        for i, content in enumerate(data, 1):
            name = content.get('name')
            phone = content.get('phone')
            comment = content.get('comment')
            print(f'{i}. {name:20} {phone:<15} {comment:<20}')
        input('\nНажмите любую кнопку что бы продолжить\n')


def add_user():
    name = input('Введите имя и фамилию: ')
    phone = input('Введите номер телефона: ')
    comment = input('Введите комментарий: ')
    new_user = {'name': name,
                'phone': phone,
                'comment': comment}
    return new_user


def search_content():
    find = input('Введите искомый элемент: ')
    return find


def input_id():
    index = int(input('Введите индекс: '))
    return index


def confirm(condition: str, name: str):
    answer = input(f'Вы действительно хотите {condition} контакт {name}? (y/n): ')
    return True if answer == 'y' else False


def confirm_changes():
    answer = input('У вас есть несохраненные изменения, хотите их сохранить? (y/n): ')
    return True if answer == 'y' else False
