# Телефонный справочник:
# 1. Открыть файл
# 2. Сохранить файл
# 3. Показать контакты
# 4. Добавить контакт
# 5. Изменить контакт
# 6. Найти контакт
# 7. Удалить контакт
# 8. Выход


import config


def print_menu():
    print('Выберите действие: \n'
          '1. Открыть файл \n'
          '2. Сохранить файл \n'
          '3. Показать контакты \n'
          '4. Добавить контакт \n'
          '5. Изменить контакт \n'
          '6. Найти контакт \n'
          '7. Удалить контакт \n'
          '8. Выход')
    data = int(input('Введите номер из списка: '))
    return data


while True:
    user_choice = print_menu()
    match user_choice:
        case 1:
            config.open_contacts()
        case 2:
            config.save_contacts()
        case 3:
            config.show_contacts()
        case 4:
            config.add_contacts()
        case 5:
            config.change_contacts()
        case 6:
            config.search_contacts()
        case 7:
            config.delete_contacts()
        case 8:
            print('Выход')
            break
