result_array = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
numbers =[]

for char in result_array:
    if char.isdigit():
        numbers.append(int(char))
b = ['"0{}"'.format(number) for number in numbers]


