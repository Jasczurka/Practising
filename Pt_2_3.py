num = int(input())
if num == sum(int(el) ** len(str(num)) for el in str(num)):
    print(f"Число {num} - число Армстронга")
else:
    print(f"Число {num} не является числом Армстронга")
