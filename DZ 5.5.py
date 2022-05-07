src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = []

for i in src:
    if i not in result:
        result.append(i)
src = result
print (f"Updated list after removing duplicates = {result}")
