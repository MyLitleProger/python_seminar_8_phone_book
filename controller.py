import view
import models

pb = models.PhoneBook()


def start():
    while True:
        item_first = view.first_menu()
        match item_first:
            case 1:
                """Открыть файл"""
                if pb.get_path():
                    pb.open_file()
                else:
                    pb.create()
                    pb.open_file()
                while True:
                    item_general = view.general_menu()
                    match item_general:
                        case 1:
                            """Сохранить файл"""
                            pb.save()
                        case 2:
                            """Показать контакты"""
                            data_file = pb.get()
                            view.show(data_file)
                        case 3:
                            """Добавить контакт"""
                            new_user = view.add_user()
                            pb.add(new_user)
                        case 4:
                            """Изменить контакт"""
                            data_file = pb.get()
                            view.show(data_file)
                            index = view.input_id()
                            contact = view.add_user()
                            pb.change(index, contact)
                        case 5:
                            """Найти контакт"""
                            search = view.search_contact()
                            result = pb.search(search)
                            view.show(result)
                        case 6:
                            """Удалить контакт"""
                            data_file = pb.get()
                            view.show(data_file)
                            index = view.input_id()
                            name = pb.get_name(index)
                            if view.confirm('удалить', name):
                                pb.delete(index)
                        case 7:
                            """Выход"""
                            if pb.check_changes():
                                if view.confirm_changes():
                                    pb.save()
                            exit()
            case 2:
                """Выход"""
                exit()
