tv_programs = ["Матч ТВ", "НТВ", "СПАС", "Пятница"]
print(*tv_programs, sep="\n")
name, pos = input("Введите название телепередачи и позицию, на которой она должна стоять в списке: ").split()
tv_programs = tv_programs[:int(pos) - 1] + [name] + tv_programs[int(pos) - 1:]
print(*tv_programs, sep="\n")
