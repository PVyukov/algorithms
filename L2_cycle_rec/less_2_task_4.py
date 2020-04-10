# 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится
# с клавиатуры.

num = int(input("Enter natural number: "))
my_sum = 1
next_el = 1
k = 1

while k < num:
    next_el = next_el / 2
    my_sum += pow(-1, k) * next_el
    k += 1
    print(f'next is {next_el}, summ is {my_sum}')

print(my_sum)
