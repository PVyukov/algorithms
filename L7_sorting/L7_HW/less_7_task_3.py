# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану. Медианой
# называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы,
# в другой — не больше медианы.
#
# Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно, используйте метод
# сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима)
from random import randint

N = 10
mass = [randint(-10, 10) for i in range(0, 2*N + 1)]

print(f'Initial array: {mass}')
check_mass = mass[::]
check_mass.sort()
print(f'Sorted array: {check_mass}')
print(f'Result for verification: {check_mass[len(check_mass)//2]}')


def f_med(mass):
    len_mass = len(mass)
    cnt_max = cnt_min = cnt_eq = 0
    for i in range(0, len_mass):
        for j in range(0, len_mass):
            if i == j:
                continue
            if mass[i] > mass[j]:
                cnt_max += 1
            elif mass[i] < mass[j]:
                cnt_min += 1
            else:
                cnt_eq += 1
#        print(cnt_max, cnt_min, cnt_eq)
        if cnt_max - cnt_min == 0 or abs(cnt_max - cnt_min) <= cnt_eq:
            return mass[i]
        else:
            cnt_max = cnt_min = cnt_eq = 0


print(f'My result: {f_med(mass)}')
