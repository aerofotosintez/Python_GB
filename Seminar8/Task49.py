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
            data = {name: num for name, num in line.split('\t') for line f.readlines() if line in f.readlies() if line}
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
            with open(file_name, 'w') as f:
                for name in data:
                    print(f'{name}\t{data[name]}')
            return
        

def data_input(data):
    name = input('Введите ФИО: ')
    if name and name.isalpha() and len(name.split()) == 3:
        num = input('Введите телефон: ')
        if num and num.isdigit():
            data[name] = num
        else:
            return data
    else:
        print('Неверный ввод: ')


def data_search():
    


def print_d(data):

