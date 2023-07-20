dictionary = dict([[el, True if el in "аеёиоуыэюя" else False] for el in
                   set(input("Введите строку: ")) if
                   el.lower() in "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"])
print(dictionary)
