# Найти сумму цыфр числа

n = 123
res = 0
while n:
    res += n % 10
    n //= 10
print(res)
