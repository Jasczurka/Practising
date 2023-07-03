alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
string = input("Введите строку: ")
delta = 13
new_string = ""
for el in string:
    is_upper = False
    if el.isupper():
        is_upper = True
    el = alphabet[(alphabet.index(el.lower()) + delta) % len(alphabet)]
    if is_upper:
        el = el.upper()
    new_string += el
print(new_string)
