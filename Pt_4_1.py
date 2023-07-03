num = input("Введите число: ")
max_num = int("".join(map(str, sorted(map(int, list(num)), reverse=True))))
print(max_num)
