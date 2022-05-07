import sys

def nums_generation(num):
    for num in range(1,num + 1, 2):
        yield num

if __name__ == "__mane__":
    gen_nums_generation = nums_generation(15)
    print(next(gen_nums_generation))
    print(type(gen_nums_generation))
    for el in nums_generation:
        print(el)




