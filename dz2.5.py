from decimal import Decimal
price_list = [44.50, 85.60, 12.40, 58.60, 78.05, 697.12, 68.78, 79.63, 8921.53, 9798.23]
members = float(price_list)


x = Decimal(price_list[0])
a = int(x)
b = int(100 * (x - a))
print(a, b)
a, b = map(int, price_list.split('.'))
print(a, b)