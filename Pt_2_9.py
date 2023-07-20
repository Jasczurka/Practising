n = input()
print("Порядковый номер максимальной цифры от начала числа:",
      n.index(str(max(map(int, list(n))))) + 1)
print("Порядковый номер максимальной цифры от конца числа:",
      n[::-1].index(str(max(map(int, list(n))))) + 1)
