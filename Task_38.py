# Телефонный справочник.

# Показать контакт.
def show_data(filename, rec_id):
    with open(filename, 'r', encoding='utf-8') as data:
        for line in data:
            if rec_id == line.split()[0]:
                return line

# Показать все контакты.
def show_all(filename):
    with open(filename, 'r', encoding='utf-8') as data:
        for line in data:
            print(line, end='')
    print()

# Создать новый контакт.
def new_data(filename):
    with open(filename, 'r+', encoding='utf-8') as data:
        # Присвоение ID номера записи.
        rec_id = 0
        for line in data:
            if line != '':
                rec_id = line.split(' ', 1)[0]
        rec_id = str(int(rec_id) + 1)
        # Ввод данных.
        surname = input_data('Фамилия: ')
        name = input_data('Имя: ')
        patronymic = input_data('Отчество: ')
        phone_number = input_data('Номер телефона: ')
        # Запись данных.
        data.write(f'{rec_id} {surname} {name} {patronymic} {phone_number}\n')
    print(f'Контакт создан: {show_data(filename, rec_id)}')

# Ввод данных и проверка отсутствия пробела.
def input_data(parameter):
    space = True
    while space:
        text = input(parameter)
        if ' ' not in text:
            space = False
        else:
            print('Пробелы недопустимы!')
    return text

# Поиск контакта.
def find_data(filename):
    # Выбор параметра (индекса) для поиска.
    char = None
    while char not in (0, 1, 2, 3, 4):
        print('Поиск по: (ID - 0, Фамилия - 1, Имя - 2, Отчество - 3, Номер телефона - 4)')
        char = int(input('Выбор: '))
    # Поиск.
    desired = input('Поиск: ').lower() # Искомое преобразуется в нижний регистр.
    found = False # Успешный поиск.
    with open(filename, 'r', encoding='utf-8') as data:
        for line in data:
            # Сравнение искомого с параметром (по индексу) из разделенной строки (в нижнем регистре).
            if desired == line.split()[char].lower():
                print(line)
                found = True
    if not found:
        print('Не найдено.')

# Изменение контакта.
def change_data(filename):
    rec_id = select_data(filename) # Выбор ID контакта.
    if rec_id: # Если ID контакта существует.
        char = None
        while char not in (1, 2, 3, 4):
            print('Что изменить: (Фамилия - 1, Имя - 2, Отчество - 3, Номер телефона - 4)')
            char = int(input('Выбор: '))
        new_char = input('Введите новое: ') # Ввод новых данных.
        new_data = ''
        with open(filename, 'r', encoding='utf-8') as data:
            for line in data:
                new_data += line
                if rec_id == line.split()[0]:
                    new_data = new_data.replace(line.split()[char], new_char)
        with open(filename, 'w', encoding='utf-8') as data:
            data.write(new_data)
    print(f'Контакт изменен: {show_data(filename, rec_id)}')

# Удаление контакта.
def delete_data(filename):
    rec_id = select_data(filename) # Выбор ID контакта.
    if rec_id: # Если ID контакта существует.
        new_data = ''
        with open(filename, 'r', encoding='utf-8') as data:
            for line in data:
                new_data += line
                if rec_id == line.split()[0]:
                    new_data = new_data.replace(line, '')
        print(f'Контакт удален: {show_data(filename, rec_id)}')
        with open(filename, 'w', encoding='utf-8') as data:
            data.write(new_data)

# Выбор контакта для изменения или удаления.
def select_data(filename):
    rec_id = input('Введите ID контакта: ')
    with open(filename, 'r', encoding='utf-8') as data:
        for line in data:
            if rec_id == line.split()[0]:
                return rec_id
    print('Контакт не найден.')
    return False

# Новый файл, если не существует.
with open('data.txt', 'a', encoding='utf-8') as file:
    file.write('')
# Выбор действия.
mode = None
while mode != '0':
    print('Действия: (Показать все - 1, Создать новый - 2, Поиск - 3, Изменить - 4, Удалить - 5, Выход - 0)')
    mode = input('Выбор: ')
    if mode == '1':
        show_all('data.txt')
    elif mode == '2':
        new_data('data.txt')
    elif mode == '3':
        find_data('data.txt')
    elif mode == '4':
        change_data('data.txt')
    elif mode == '5':
        delete_data('data.txt')
print("Работа завершена.")
