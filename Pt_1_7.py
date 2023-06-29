string = input()
new_string = ""
for el in string:
    if el.isupper():
        new_string += el.lower()
    elif el.islower():
        new_string += el.upper()
    else:
        new_string += el
print(new_string)
