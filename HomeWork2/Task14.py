# Требуется вывести все целые степени двойки 
#(т.е. числа вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8

n = int(input('введите максимальное значение степени: '))
k = 1
for i in range(1, n):
    if k < n:
        print(k)
        k = 2 ** i
    else:
        break
