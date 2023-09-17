list_1 = [1, 2, 3, 3, 5]
k = 3

count = 0
for i in range(0, len(list_1)):
    if list_1[i] == list_1[k]:
        count += 1
print(count)
