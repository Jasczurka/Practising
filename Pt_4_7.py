import itertools

values = input("Введите элементы списка: ").split()
for el in itertools.permutations(values, len(values)):
    print(el)
