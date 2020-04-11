# 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится
# с клавиатуры.

# с циклом
num = int(input("Enter natural number: "))
my_sum = 1
next_el = 1
k = 1

while k < num:
    next_el = next_el / 2
    my_sum += pow(-1, k) * next_el
    k += 1
print(my_sum)

# с рекурсией


def func(a, cnt, stop):
    if cnt == stop:
        return a
    else:
        return a + func(-1 * a / 2, cnt + 1, stop)


num = int(input("Enter quantity of elements: "))
my_sum = func(1, 1, num)
print(my_sum)
