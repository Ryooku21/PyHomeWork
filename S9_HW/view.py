def menu() -> int:
    print('''\nГлавное меню:
    1. Открыть файл
    2. Сохранить файл
    3. Показать контакты
    4. Добавить контакт
    5. Найти контакт
    6. Изменить контакт
    7. Удалить контакт
    8. Выход''')
    while True:
        choice = input('Выберите пункт меню: ')
        if choice.isdigit() and 0 < int(choice) < 9:
            return int(choice)


def show_contacts(phone_book: list[dict]):
    print()
    if phone_book:
        for i, contact in enumerate(phone_book, 1):
            print(f'{i}. {contact.get("name"):<12} '
                  f'{contact.get("surname"):<12} '
                  f'{contact.get("phone"):<12} '
                  f'{contact.get("comment"):<12}')
        print()
    else:
        print('\nФайл телефонной книги не открыт или пуст\n')


def new_contact() -> dict:
    print()
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    phone = input('Введите номер телефона: ')
    comment = input('Введите комментарий: ')
    print()
    return {'name': name, 'surname': surname, 'phone': phone, 'comment': comment}


def change_contact(book: list) -> tuple:
    show_contacts(book)
    choice = int(input('Выберите номер контакта, который нужно изменить: '))
    name = input('Введите новую фамилию или Enter - оставить без изменений')
    surname = input('Введите новое имя или Enter - оставить без изменений')
    phone = input('Введите новоый телефон или Enter - оставить без изменений')
    comment = input('Введите новый комментарий или Enter - оставить без изменений')
    return choice - 1, {'name': name if name else book[choice - 1].get('name'),
                        'surname': surname if surname else book[choice - 1].get('surname'),
                        'phone': phone if phone else book[choice - 1].get('phone'),
                        'comment': comment if comment else book[choice - 1].get('comment')}


def select_to_delete(book: list):
    show_contacts(book)
    return int(input('Введите номер элемента, который нужно удалить: ')) - 1


def input_request(text: str) -> str:
    return input(f'Введите {text}: ')


def goodbye():
    print('Программа завершена')


def confirm_changes():
    answer = input('У вас есть несохраненные изменения, хотите их сохранить? (y/n)')
    return True if answer == 'y' else False
