def is_composite(n):
    k = 2
    while k ** 2 <= n:
        if n % k == 0:
            return 1
        k += 1
    return 0


list_of_composite_nums = [i for i in range(1000) if is_composite(i)]
print(list_of_composite_nums)
