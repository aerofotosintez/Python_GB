# Требуется найти в массиве list_1 самый близкий 
# по величине элемент к заданному числу k и вывести его.

list_1 = [1, 2, 3, 4, 5]
k = int(input('введите число: '))
def nearest_value(list_1, k):
    return min(list_1, key = lambda x: abs(k - abs(x)))
print(nearest_value(list_1, k))
