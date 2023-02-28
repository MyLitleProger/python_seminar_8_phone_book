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
                            view.show(pb.get())
                        case 3:
                            """Добавить контакт"""
                            pb.add(view.add_user())
                        case 4:
                            """Изменить контакт"""
                            contact = view.change(pb.get())
                            pb.change(contact[0], contact[1])
                        case 5:
                            """Найти контакт"""
                            view.show(pb.search(view.search_contact()))
                        case 6:
                            """Удалить контакт"""
                            view.show(pb.get())
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
