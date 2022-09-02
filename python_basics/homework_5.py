documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def whose_docs(docs):
    number = input('Введите номер документа: ')
    for num in docs:
        if num['number'] == number:
            return f"Владелец документа - {num['name']}\n"
    return 'Документ отсутствует.\n'


def doc_in_shelf(dirs):
    num_doc = input('Введите номер документа: ')
    for key, value in dirs.items():
        if num_doc in value:
            return f'Документ хранится на полке - {key}\n'
    return 'Документ отсутствует.\n'


def share_docs(docs):
    for doc in docs:
        print(', '.join(doc.values()))
    print()


def add_docs(docs, dirs):
    new_type = input("Документ: ")
    new_number = input("Номер: ")
    new_name = input("ФИО: ")
    shelf_num = input("Номер полки: ")
    for num in docs:
        if num['number'] == new_number:
            return f'Документ уже существует\n'
    if shelf_num in dirs.keys():
        new_doc = {"type": new_type, "number": new_number, "name": new_name}
        docs.append(new_doc)
        dirs[shelf_num].append(new_number)
        return 'Документ добавлен.\n'
    return 'Номер полки не существует.\n'


def del_doc(docs, dirs):
    num_doc = input('Введите номер документа: ')
    if any(num_doc in shelf for shelf in dirs.values()):
        for key in dirs.keys():
            if num_doc in dirs[key]:
                dirs[key].remove(num_doc)
        for doc in docs:
            if doc['number'] == num_doc:
                docs.remove(doc)
        return 'Удаление прошло успешно.\n'
    return 'Документ отсутствует.\n'


def mov_doc(docs, dirs):
    num_doc = input('Введите номер документа: ')
    num_shelf = input('Номер полки: ')
    if num_shelf not in dirs.keys():
        return 'Номер полки не существует.\n'
    elif not any(num_doc in shelf for shelf in dirs.values()):
        return 'Документ отсутствует.\n'
    else:
        for key in dirs.keys():
            if num_doc in dirs[key]:
                dirs[key].remove(num_doc)
                dirs[num_shelf].append(num_doc)
        return 'Документ перемещен на указанную полку.\n'


def new_shelf(dirs):
    num_shelf = input('Введите номер полки: ')
    if num_shelf not in dirs.keys():
        dirs.setdefault(num_shelf, [])
        return 'Полка успешно добавлена.\n'
    else:
        return 'Полка уже существует.\n'


def main_help():
    help_menu = [
        "help - список команд",
        "p - выводит имя человека, на которого оформлен документ",
        "s - выводит номер полки архива, на которой хранится документ",
        "l - выводит список всех документов в каталоге",
        "a - добавляет новый документ в каталог и на полку архива",
        "d - удаляет документ из каталога и архива",
        "m - переносит документ на указанную полку архива",
        "as - добавляет новую полку в архив",
        "q - выход"
    ]
    string = '\n'.join(help_menu)
    print(f"\n{string}\n")


def main():
    print('help - список команд', 'q - выход\n', sep='\n')

    while True:
        command = input('Введите команду: ')
        if command == 'p':
            print(f'\n{whose_docs(documents)}')
        elif command == 's':
            print(f'\n{doc_in_shelf(directories)}')
        elif command == 'l':
            share_docs(documents)
        elif command == 'a':
            print(f'\n{add_docs(documents, directories)}')
        elif command == 'd':
            print(f'\n{del_doc(documents, directories)}')
        elif command == 'm':
            print(f'\n{mov_doc(documents, directories)}')
        elif command == 'as':
            print(f'\n{new_shelf(directories)}')
        elif command == 'help':
            main_help()
        elif command == 'q':
            return 'Выход'


if __name__ == '__main__':
    print(main())
