from math import sqrt

a, b, c = map(int,
              input("Введите коэффиценты квадратного уравнения: ").split())
d = b ** 2 - 4 * a * c
if d < 0:
    print("Корней нет")
elif d == 0:
    print("x =", -b / (2 * a))
else:
    print("x1 =", (-b + sqrt(d)) / (2 * a))
    print("x2 =", (-b - sqrt(d)) / (2 * a))
