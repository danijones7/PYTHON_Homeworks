def search(book: str, info: str) -> list[str]:
    """Находит в списке записи по определенному критерию поиска"""
    book = book.split('\n')
    return list(filter(lambda contact: info.lower() in contact.lower(), book))


data = 'фио | номер телефона\n\
фио1 | номер телефона1\n\
Исаев Владислав Иванович | +814881481848\n\
Иванов Иван Иваныч | +16471845915'
# print(data)
# contact_to_find = input('Введите, что хотите найти: ')
# print(search(data, contact_to_find))


def change_data() -> None:
    # with open('python_homework\8_seminar\\book.txt', 'r', encoding='utf-8') as file:
    #     data = file.read()
    contact_to_change = input('Введите, что хотите изменить: ')
    result = list(enumerate(search(data, contact_to_change)))
    print(result[0])
    number_of_contact = int(input("Введите порядковый номер контакта, который хотите изменить: "))
    fio = input("Введите ФИО: ")
    phone = input("Введите номер телефона: ")
    result[number_of_contact] = f"{fio} | {phone}"
    # with open('python_homework\8_seminar\\book.txt', 'w', encoding='utf-8') as file:
    #     file.writelines(result)
    print(type(result))

