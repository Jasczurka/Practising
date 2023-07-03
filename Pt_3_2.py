func = lambda n, x=0, y=1: [x] + func(n, y, x + y) if y <= n else [x]
n = int(input("Введите число: "))
print(func(n))
