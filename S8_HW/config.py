phone_book = []


def open_contacts():
    with open('phone_book.txt', 'r', encoding='utf-8') as data:
        phone_book = data.readlines()
        print('Файл открыт')
        return phone_book


def save_contacts():
    with open('phone_book.txt', 'w', encoding='utf-8') as data:
        for i in phone_book:
            data.write(i)


def show_contacts():
    if len(phone_book) == 0:
        print('Откройте файл с контактами, либо контакты отсутствуют!')
    else:
        for i in phone_book:
            print(' '.join(i.split(';')))


def add_contacts():
    if len(phone_book) == 1:
        print('Откройте справочник!')
    else:
        user_info = input('Введите контактные данные')
        user_info = ';'.join(user_info.split(' '))
        phone_book.append('\n' + user_info)


def change_contacts():
    user_info = input('Введите имя контакта, который необходимо изменить: ')
    for i in range(len(phone_book)):
        if user_info in phone_book[i]:
            print(phone_book[i])
            print(i)
            new_user_info = input('Введите новые контактные данные: ')
            phone_book[i] = phone_book[i].replace(user_info, new_user_info)


def search_contacts():
    user_info = input('Введите имя контакта, по которому будем искать: ')
    for i in range(len(phone_book)):
        if user_info in phone_book[i]:
            print(phone_book[i])


def delete_contacts():
    user_info = input('Введите имя контакта, который необходимо удалить: ')
    for i in range(len(phone_book)):
        if user_info in phone_book[i]:
            print(phone_book[i])
            phone_book.pop[i]
            break


phone_book = open_contacts()