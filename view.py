def mask_phone(condition: str = '') -> str:
    """Добавляет телефон по маске"""
    while True:
        phone = input(f'Введите телефон состоящий из 11 или 6 цифр {condition}: ')
        if phone.isdigit() and len(phone) == 11:
            phone = phone[0] + '(' + phone[1:4] + ')' + phone[4:7] + '-' + phone[7:9] + '-' + phone[9:11]
            return phone
        elif phone.isdigit() and len(phone) == 6:
            phone = phone[0:2] + '-' + phone[2:4] + '-' + phone[4:6]
            return phone
        elif not phone:
            return phone


def first_menu() -> int:
    """Начальное меню"""
    print('''\n Меню:
    1. Открыть файл
    2. Выход''')
    while True:
        try:
            choice = input_int('Выберите пункт меню: ')
            if 0 < choice < 3:
                return choice
            else:
                print('Введите число от 1 до 2')
        except ValueError:
            print('Некорректный ввод!')


def general_menu() -> int:
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
                return choice
            else:
                print('Введите число от 1 до 7')
        except ValueError:
            print('Некорректный ввод!')


def show(data: list[dict]):
    """Показать контакты"""
    if data:
        for i, content in enumerate(data, 1):
            print(f'{i}. {content.get("name"):20} {content.get("phone"):<20} {content.get("comment"):<20}')
        input('\nНажмите Enter что бы продолжить\n')
    else:
        print('Файл пуст')
        input('\nНажмите Enter что бы продолжить\n')


def add_user() -> dict:
    """Добавить контакт"""
    name = input('Введите имя и фамилию: ')
    phone = mask_phone()
    comment = input('Введите комментарий: ')
    return {'name': name, 'phone': phone, 'comment': comment}


def change(data: list) -> tuple:
    """Изменяет контакт"""
    show(data)
    while True:
        try:
            choice = input_int('Выберите контакт, который хотите изменить: ')
            name = input('Введите новое имя или Enter оставить без изменений: ')
            phone = mask_phone('или Enter оставить без изменений')
            comment = input('Введите новый комментария или Enter оставить без изменений: ')
            return choice - 1, {'name': name if name else data[choice - 1].get('name'),
                                'phone': phone if phone else data[choice - 1].get('phone'),
                                'comment': comment if comment else data[choice - 1].get('comment')}
        except IndexError:
            print('Некорректный ввод')


def search_contact() -> str:
    """Поиск контакта"""
    find = input('Введите искомый элемент: ')
    return find


def input_int(message: str = '') -> int:
    while True:
        try:
            choice = int(input(message))
            return choice
        except ValueError:
            print('Некорректный ввод!')


def input_id() -> int:
    """Передает индекс контакта"""
    index = int(input('Введите индекс: '))
    return index


def confirm(condition: str = '', name: str = '') -> bool:
    """Подтверждение решения"""
    answer = input(f'Вы действительно хотите {condition} контакт {name}? (y/n): ')
    return True if answer == 'y' else False


def confirm_changes() -> bool:
    """Предупреждение о несохраненных данных"""
    answer = input('У вас есть несохраненные изменения, хотите их сохранить? (y/n): ')
    return True if answer == 'y' else False
