#  Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

data = [int(i) for i in input('введите числа через пробел: ').split()]
max_data = data[0]
min_data = data[0]
for i in range(1, len(data)):
    if data[i] > max_data:
        max_data = data[i]
    if data[i] < min_data:
        min_data = data[i]
print(min_data, max_data)