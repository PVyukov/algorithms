# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два
# абсолютно разных значения.


import random

SIZE = 10
MIN_ITEM = -10
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)


# ----не верно, т.к. если первый элемент сразу берется как максимальный, н он может быть >0 -------
index = 0
max_el = array[0]

for i, el in enumerate(array[1:], 1):
    if el < 0:
        if max_el < el:
            max_el = el
            index = i

print(f'max el is {max_el}; index is {index}')


# ----вариант учителя--------
# вариант 1
# i = 0
# index = -1
# while i < len(array):   # или for i in range(len(array)):
#     if array[i] < 0 and index == -1:
#         index = i
#     elif 0 > array[i] > array[index]:
#         index = i
#     i += 1
#
# if index != -1:
#     print(f'Максимальное отрицательное число {array[index]} '
#           f'находится в ячейке {index}')
#
# # вариант 2
# num = float('-inf')
# for i, item in enumerate(array):
#     if 0 > item > num:
#         num = item
#         index = i
#
# if num != float('-inf'):
#     print(f'Максимальное отрицательное число {num} '
#           f'находится в ячейке {index}')