
list_name = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

name0 = list_name[0]
name1 = list_name[1].swapcase()
name2 = list_name[2].swapcase()
name3 = list_name[3]
index0 = name0.split(" ")
index1 = name1.split(" ")
index2 = name2.split(" ")
index3 = name3.split(" ")

print("Привет, " + index0[-1].capitalize()+ "!")
print("Привет, " + index1[-1].capitalize()+ "!")
print("Привет, " + index2[-1].capitalize()+ "!")
print("Привет, " + index3[-1].capitalize()+ "!")