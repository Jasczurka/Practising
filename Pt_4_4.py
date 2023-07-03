import itertools

nums = list(map(int, input("Введите числа: ").split()))
value = int(input("Введите число: "))
ans = []
for i in range(1, len(nums) + 1):
    for el in itertools.combinations(nums, i):
        if sum(el) == value:
            ans.append(sorted(el))
print(ans)
