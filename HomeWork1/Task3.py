# Счастливый билет
n = 385916

sum1 = 0
sum2 = 0

for i in range(6):
    if i<3:
        sum1 += n // 10**i % 10
    else:
        sum2 += n // 10**i % 10
if sum1 == sum2:
    print('yes')
else:
    print('no')
