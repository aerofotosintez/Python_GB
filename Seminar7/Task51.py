# Напишите функцию same_by(characteristic, objects),
# которая проверяет, все ли объекты имеют одинаковое
# значение некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов,
# функция должна возвращать True. Аргумент 
# characteristic - это функция, которая принимает
# объект и вычисляет его характеристику.
# Ввод: Вывод:
# values = [0, 2, 10, 6] same
# if same_by(lambda x: x % 2, values):
# print(‘same’)
# else:
# print(‘different’)

def same_by(characteristic, objects):
    if not objects:   # if objects == []
        return True
    s0 = characteristic(objects[0])
    for object in objects[1:]:
        s = characteristic(object)
        if s != s0:
            return False
    return True


values = [0, 2, 10, 6]     #same
if same_by(lambda x: x % 3, values):
    print('same')
else:
    print('different')

# в одну строку
# return all([s == characteristic(objects[0]) if objects else True for s i map(characteristic, objects)])