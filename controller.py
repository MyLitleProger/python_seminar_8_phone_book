import view
import models


def start():
    while True:
        item_first = view.first_menu()
        match item_first:
            # open
            case 1:
                if models.get_path():
                    models.open_file()
                else:
                    models.create()
                    models.open_file()
                while True:
                    item_general = view.general_menu()
                    match item_general:
                        # save
                        case 1:
                            models.save()
                        # show
                        case 2:
                            data_file = models.get()
                            view.show_content(data_file)
                        # add
                        case 3:
                            new_user = view.add_user()
                            models.add(new_user)
                        # change
                        case 4:
                            data_file = models.get()
                            view.show_content(data_file)
                            index = view.input_id()
                            contact = view.add_user()
                            models.change(index, contact)
                        # search
                        case 5:
                            search = view.search_content()
                            result = models.search(search)
                            view.show_content(result)
                        # delete
                        case 6:
                            data_file = models.get()
                            view.show_content(data_file)
                            index = view.input_id()
                            name = models.get_name(index)
                            if view.confirm('удалить', name):
                                models.delete(index)
                        # exit
                        case 7:
                            if models.check_changes():
                                if view.confirm_changes():
                                    models.save()
                            exit()
            # exit
            case 2:
                exit()
