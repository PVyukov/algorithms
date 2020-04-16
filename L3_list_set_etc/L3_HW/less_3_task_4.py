# Определить, какое число в массиве встречается чаще всего.
import random

SIZE = 10
MIN_ITEM = -10
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)
max_cnt = 0


for num_1 in array:
    cnt = 0
    for num_2 in array:
        if num_1 == num_2:
            cnt += 1
#    print(f'{num_1:>3}:\t{cnt}')
    if max_cnt < cnt:
        max_cnt = cnt
        most_freq = num_1
print(f'{most_freq}')

