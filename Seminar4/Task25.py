# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию

sp = input('введите символ: ').split()
d = {}
for letter in sp:
    if letter not in d:
        count = 0
        d[letter] = count
        print(letter, end= ' ')
    else:
        d[letter] += 1
        print("{}_{}" .format(letter, d[letter]), end=" ")
