rus_num = ["ноль", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять", "десять"]
eng_num = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
list(map(str.capitalize, eng_num))
list(map(str.capitalize, rus_num))

for rus, eng in zip(eng_num, rus_num):
     print(eng, rus)