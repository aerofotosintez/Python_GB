
import os

file_name = 'Телефонный справочнк.txt'


def main():
    data = {}
    if os.path.exists(file_name):
        with open(file_name) as f:
            for line in f.readlines():
                if line:
                    name, num = line.split('\t')
                    data[name] = num
    else:
        with open(file_name, 'w') as f:
            pass

    while True:
        while True:
            print('1.Ввести данные')
            print('2.Поиск')
            print('3.Изменить данные')
            print('4.Выход')
            user_choice = input('Введите выбор (1-3): ')
            if user_choice not in ['1', '2', '3', '4']:
                print('Ошибка')
            else:
                break
        match user_choice:
            case '1':
                data = data_input(data)
            case '2':
                data_search(data)
            case '3':
                update_delete_data(data)
            case '4':
                print('Досвидание')
                if not data:
                    return
                with open(file_name, 'w') as f:
                    for name in data:
                        print(f'{name}\t{data[name]}', file=f)
                return


def data_input(data):
    name = input('Введите ФИО: ')
    if name and len(name.split()) == 3:
        num = input('Введите телефон: ')
        if num and num.isdigit():
            data[name.replace('\t', ' ')] = num
            return data
    print('Неверный ввод ')
    return data


def data_search(data):
    user_input = input('Введите данные для поиска: ')
    while True:
        print('1.Найти фамилию ')
        print('2.Найти имя ')
        print('3.Найти отчество ')
        print('4.Найти номер тлф ')
        print('5.Вернуться в меню ')
        user_choice = input('Введите выбор (1-5): ')
        if user_choice not in ['1', '2', '3', '4', '5']:
            print('Ошибка')
        else:
            break
    match user_choice:
        case '1':
            for key in data:
                name1, name2, name3 = key.split()
                if name1 == user_input:
                    print(f"{key} {data[key]}")
        case '2':
            for key in data:
                name1, name2, name3 = key.split()
                if name2 == user_input:
                    print(f'{key} {data[key]}')
        case '3':
            for key in data:
                name1, name2, name3 = key.split()
                if name3 == user_input:
                    print(f'{key} {data[key]}')
        case '4':
            for key, value in data.items():
                if value == user_input():
                    print(f'{key} {data[key]}')
        case '5':
            print('Выход ')
            return
        

def update_delete_data(data):
    while True:
        print('1.Изменить данные ')
        print('2.Удалить данные ')
        print('3.Возврат в меню ')
        user_choice = input('Введите выбор (1-3): ')
        if user_choice not in ['1', '2', '3']:
                print('Ошибка')
        else:
            break
    if user_choice == '1':
        update_data(data)
    elif user_choice == '2':
        delete_data(data)
    elif user_choice == '3':
        print('Выход ')
        return
    

def update_data(data):
    user_input = input('Введите ФИО для изменения данных: ')
    if user_input in data:
        new_num = input('Введите новый номер')
        if new_num.isdigit():
            data[user_input] = new_num
            print('Номер изменен')
        else:
            print('Ошибка')
    else:
        print('Данных в справочнике нет')


def delete_data(data):
    user_input = input('Введите ФИО для удаления данных: ')
    if user_input in data:
        del data[user_input]
    else:
        print('Данных в справочнике нет')


def save_data(data):
    with open(file_name) as f:
        for name in data:
            print(f'{name}\t{data[name]}', file=f)
    

if __name__ == '__main__':
    main()