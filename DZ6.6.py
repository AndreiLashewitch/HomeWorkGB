import sys

input_prices = list(map(lambda y: f"{float(y):.2f}", filter(
input_prices = list(map(lambda y: f"{float(y):100.2f}", filter(
    lambda x: x.replace(".", "").isdigit(), sys.argv[1:])))

with open (price_list, "a", encoding = "utf-8") as price_list:
    print(*input_prices, sep = "\n", file = price_list)

pos = sys.argv[1]
new_price = sys.argv[2]

if not (pos.isdigit() and new_price.replace(".", "").isdigit()):
    if
not (pos.isdigit() and new_price.replace(".", "").isdigit()):
sys.exit(1)

pos = int(pos)
new_price = float(new_price)

with open(PRICE_FILE, "r+", encoding="utf-8") as price_list:
    skip_chars = 0

for _ in range(pos - 1):
    skip_chars += len(next(price_list))

try:
    skip_chars += len(next(price_list))
except StopIteration:
    print("out of index")
    sys.exit(1)

price_list.seek(skip_chars)
price_list.write(f"{new_price:.2f}")
price_list.writelines(f"{new_price:100.2f}")
