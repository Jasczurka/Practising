string = input("Введите строку: ")
dictionary = dict([el, string.count(el)] for el in set("".join(string.strip().split())))
print(dictionary)
