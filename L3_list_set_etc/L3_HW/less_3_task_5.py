import random

SIZE = 10
MIN_ITEM = -10
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)
index = 0
max_el = array[0]

for i, el in enumerate(array[1:], 1):
    if el < 0:
        if max_el < el:
            max_el = el
            index = i

print(f'max el is {max_el}; index is {index}')
