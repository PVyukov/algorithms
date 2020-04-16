# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random

SIZE = 10
MIN_ITEM = -10
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(array)


min_index = max_index = 0
min_ = max_ = array[0]
# print(f'0\t{min_}__{max_}')

for i, el in enumerate(array[1:], 1):
    if max_ < el:
        max_ = el
        max_index = i
    elif min_ > el:
        min_ = el
        min_index = i
#    print(f'{i}\t{min_}__{max_}')
array[min_index], array[max_index] = max_, min_
print(array)

