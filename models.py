from os import path
from copy import deepcopy

# глобальные переменные
data_file = []
old_data_file = []
name_file = 'phone_db.txt'


# получить переменную
def get():
    global data_file
    return data_file


# получить имя
def get_name(index: int):
    global data_file
    return data_file[index - 1].get('name')


# получить расположение файла
def get_path():
    global name_file
    return True if path.isfile(name_file) else False


# создание файла
def create():
    global name_file
    with open(name_file, 'w', encoding='utf-8') as file:
        file.write('')


# функция открытия файла
def open_file():
    global data_file
    global old_data_file
    global name_file
    with open(name_file, 'r', encoding='UTF-8') as file:
        data = file.readlines()
        for contact in data:
            new = contact.strip().split(';')
            new_contact = {'name': new[0],
                           'phone': new[1],
                           'comment': new[2]}
            data_file.append(new_contact)
    old_data_file = deepcopy(data_file)


# сохранение файла, запись данных из списка в файл
def save():
    global data_file
    global name_file
    data = []
    for contact in data_file:
        data.append(';'.join(contact.values()))
    data = '\n'.join(data)
    with open(name_file, 'w', encoding='utf-8') as file:
        file.write(data)


# добавление данный в файл
def add(new_contact: dict):
    global data_file
    data_file.append(new_contact)


# изменение данных в файле (недоделано: show ругается)
def change(index: int, contact: dict):
    global data_file
    data_file.pop(index - 1)
    data_file.insert(index - 1, contact)


# поиск в файле
def search(search_inp: str):
    global data_file
    all_find = []
    for contact in data_file:
        for element in contact.values():
            if search_inp.lower() in element.lower():
                all_find.append(contact)
    return all_find


# удаление данных из файла
def delete(index: int):
    global data_file
    data_file.pop(index - 1)


def check_changes():
    global data_file
    global old_data_file
    if data_file != old_data_file:
        return True
    return False
