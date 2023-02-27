from os import path
from copy import deepcopy


class PhoneBook:
    """Базовый класс телефонной книги
    :returns: имя файла, данный файла, начальные данные файла
    """
    def __init__(self, name_file: str = 'phone_db.txt'):
        self.name_file = name_file
        self.data_file = []
        self.old_data_file = []

    def get(self):
        """Получить переменную"""
        return self.data_file

    def get_name(self, index: int):
        """Получить имя"""
        return self.data_file[index - 1].get('name')

    def get_path(self) -> bool:
        """Получить расположение файла"""
        return True if path.isfile(self.name_file) else False

    def create(self):
        """Создание файла"""
        with open(self.name_file, 'w', encoding='utf-8') as file:
            file.write('')

    def open_file(self):
        """Функция открытия файла"""
        with open(self.name_file, 'r', encoding='UTF-8') as file:
            data = file.readlines()
            for contact in data:
                new = contact.strip().split(';')
                new_contact = {'name': new[0],
                               'phone': new[1],
                               'comment': new[2]}
                self.data_file.append(new_contact)
        self.old_data_file = deepcopy(self.data_file)

    def save(self):
        """ Сохранение файла, запись данных из списка в файл"""
        data = []
        for contact in self.data_file:
            data.append(';'.join(contact.values()))
        data = '\n'.join(data)
        with open(self.name_file, 'w', encoding='utf-8') as file:
            file.write(data)

    def add(self, new_contact: dict):
        """ Добавление данных в файл"""
        self.data_file.append(new_contact)

    def change(self, index: int, contact: dict):
        """ Изменение данных в файле """
        self.data_file.pop(index - 1)
        self.data_file.insert(index - 1, contact)

    def search(self, search_inp: str):
        """ Поиск в файле """
        all_find = []
        for contact in self.data_file:
            for element in contact.values():
                if search_inp.lower() in element.lower():
                    all_find.append(contact)
        return all_find

    def delete(self, index: int):
        """ Удаление данных из файла """
        self.data_file.pop(index - 1)

    def check_changes(self):
        """Проверка несохраненных данных"""
        return True if self.data_file != self.old_data_file else False
