# Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

a1 = int(input('введите первый элемент прогрессии: '))
d = int(input('введите разность прогрессии: '))
n = int(input('введите количество элементов прогрессии: '))
an = []
for i in range(n):
    an.append(a1 + (i - 1) * d)
print(an)