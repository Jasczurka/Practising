def is_simple(n):
    if n == 1:
        return 0
    k = 2
    while k ** 2 <= n:
        if n % k == 0:
            return 0
        k += 1
    return 1


left, right = map(int, input("Введите диапазон: ").split())
for i in range(left, right + 1):
    if is_simple(i):
        print(i)
