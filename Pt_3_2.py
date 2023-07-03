func = lambda x, y, z: [x] + func(y, x + y, z) if y <= z else [x]
n = int(input("Введите число: "))
print(func(0, 1, n))
