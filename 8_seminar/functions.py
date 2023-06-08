def show_data() -> None:
    """Выводит информацию из справочника"""
    with open('python_homework\8_seminar\\book.txt', 'r', encoding='utf-8') as book:
        print(book.read())


def add_data() -> None:
    """Добавляет информацию в справочник."""
    fio = input('Введите ФИО: ')
    phone_num = input('Введите номер телефона: ')
    with open('python_homework\8_seminar\\book.txt', 'a', encoding='utf-8') as book:
        book.write(f'\n{fio} | {phone_num}')


def search(book: str, info: str) -> list[str]:
    """Находит в списке записи по определенному критерию поиска"""
    book = book.split('\n')
    return list(filter(lambda contact: info.lower() in contact.lower(), book))

def find_data() -> None:
    """Печатает результат поиска по справочнику."""
    with open('python_homework\8_seminar\\book.txt', 'r', encoding='utf-8') as file:
        data = file.read()
    contact_to_find = input('Введите, что хотите найти: ')
    result = search(data, contact_to_find)
    print(result)

# мои жалкие попытки решить самой 
# def change_data() -> None:
#     with open('python_homework\8_seminar\\book.txt', 'r', encoding='utf-8') as file:
#         data = file.read()
#     contact_to_change = input('Введите, что хотите изменить: ')
#     result = list(enumerate(search(data, contact_to_change)))
#     print(result)
#     number_of_contact = int(input("Введите порядковый номер контакта, который хотите изменить: "))
#     fio = input("Введите ФИО: ")
#     phone = input("Введите номер телефона: ")
#     result[number_of_contact] = f"{fio} | {phone}"
#     with open('python_homework\8_seminar\\book.txt', 'w', encoding='utf-8') as file:
#         file.writelines(result)

#спасибо чатик gpt

def change_data() -> None:
    """Изменяет или удаляет данные в справочнике."""
    with open('python_homework\8_seminar\\book.txt', 'r', encoding='utf-8') as file:
        data = file.readlines()

    contact_to_change = input('Введите ФИО или номер телефона для изменения или удаления: ')

    matching_contacts = []
    for contact in data:
        if contact_to_change.lower() in contact.lower():
            matching_contacts.append(contact)

    if not matching_contacts:
        print('Контакт не найден')
        return

    print('Найденные контакты:')
    for i, contact in enumerate(matching_contacts):
        print(f'{i + 1}. {contact.strip()}')

    choice = input('Выберите номер контакта для изменения/удаления (или "отмена"): ')
    if choice.lower() == 'отмена':
        return

    try:
        index = None
        for i, contact in enumerate(data):
            if contact.strip() == matching_contacts[int(choice) - 1].strip():
                index = i
                break

        if index is None:
            raise ValueError('Выбранный контакт не найден')

        selected_contact = data[index].strip()
        print(f'Выбранный контакт: {selected_contact}')

        action = input('Выберите действие (изменить/удалить): ')
        if action.lower() == 'изменить':
            new_data = input('Введите новые данные: ')
            data[index] = new_data + '\n'
            print('Контакт успешно изменен.')
        elif action.lower() == 'удалить':
            del data[index]
            print('Контакт успешно удален.')
        else:
            print('Неверное действие.')
    except (ValueError, IndexError):
        print('Неверный выбор.')

    with open('python_homework\8_seminar\\book.txt', 'w', encoding='utf-8') as file:
        file.writelines(data)

