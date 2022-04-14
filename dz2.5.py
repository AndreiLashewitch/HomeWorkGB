from decimal import Decimal
price_list = [44.50, 85.60, 12.40, 58.60, 78.05, 697.12, 68.78, 79.63, 8921.53, 9798.23]
price_list1 = list(map(str, price_list))
#price_list_str = ','.join(price_list)
print(type(price_list1))

rub, cop = map(float, price_list1.split())
count = int(price_list1)
cop += rub * 100
answer = cop * count
rub = answer//100
cop = str(answer%100)
if len(cop) == 1: cop = '0'+cop

print(f' { rub } руб. { cop } коп.')
