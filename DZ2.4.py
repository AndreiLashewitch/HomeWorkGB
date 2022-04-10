
list_name = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

name0 = list_name[0]
name1 = list_name[1].swapcase()
name2 = list_name[2].swapcase()
name3 = list_name[3]

print("Привет, " + name0[20:25]+ "!")
print("Привет, " + name1[18:25].capitalize()+ "!")
print("Привет, " + name2[23:30].capitalize()+ "!")
print("Привет, " + name3[9:15].capitalize()+ "!")