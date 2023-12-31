# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной

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
            # data = {name: num for name, num in line.split(
            #     '\t') for line in f.readlines() if line}
    else:
        with open(file_name, 'w') as f:
            pass

    while True:
        while True:
            print('1.Ввести данные')
            print('2.Поиск')
            print('3.Выход')
            user_choice = input('Введите выбор (1-3): ')
            if user_choice not in ['1', '2', '3']:
                print('Ошибка')
            else:
                break
        match user_choice:
            case '1':
                data = data_input(data)
            case '2':
                data_search(data)
            case '3':
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
        
if __name__ == '__main__':
    main()
