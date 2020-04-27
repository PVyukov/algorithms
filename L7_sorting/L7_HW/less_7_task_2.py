# Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на
# промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
from random import random

N = 1
mass = [50*random() for i in range(0, N)]

print(mass)

def merge(a, b):
    cnt_a = len(a)
    cnt_b = len(b)
    result = []
    while cnt_a > 0:
        while cnt_b > 0:
            if a[0] <= b[0]:
                result.append(a.pop(0))
                cnt_a -= 1
                break
            else:
                result.append(b.pop(0))
                cnt_b -= 1
        else:
            result = result + a
            break
    else:
        result = result + b
    return result


def sort_merge(a):
    l_a = len(a)
    if l_a == 1:
        return a
    else:
        return merge(sort_merge(a[:l_a//2]), sort_merge(a[l_a//2:]))


print(sort_merge(mass))
