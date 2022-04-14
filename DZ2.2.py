result_array = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
numbers =[]

for char in result_array:
    if char.isdigit():
        if len(char) == 1:
            char = f"'{int(char):02}"
        elif len(char) == 2:
            char = f"'{int(char)}"
    elif char.find ('+') != -1 or char.find('-') != -1:
        if char.isdigit() < 10:
            char = f"'{char[0]}{int(char):02}'"
        else:
            char = f"'{char[0]}{int(char)}'"
    print(f'{char}', end=" ")


