a = int(input())
b = int(input())
c = int(input())
print("Наибольшее число:", max(a, b, c))
print(max(a, b, c), a + b + c - max(a, b, c) - min(a, b, c), min(a, b, c))
