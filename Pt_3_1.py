func = lambda x: sum(x) / len(x)
nums = list(map(int, input("Введите числа: ").split()))
print(func(nums))
