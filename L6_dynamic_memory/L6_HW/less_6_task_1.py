# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех
# уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

# 2.4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится
# с клавиатуры.
import sys


def show(*x):
    global total_size
    for i in x:
        total_size += sys.getsizeof(i)
        print(f'type={type(i)}, size={sys.getsizeof(i)}, obj={i}')
        if hasattr(i, '__iter__'):
            if hasattr(i, 'items'):
                for key, value in i.items():
                    show(key)
                    show(value)
            elif not isinstance(i, str):
                for item in i:
                    show(item)


# num = int(input("Enter natural number: "))
num = 110

# --- с циклом --- #
# Total consumed memory : 128

total_size = 0
my_sum = 1
next_el = 1
k = 1

while k < num:
    next_el = next_el / 2
    my_sum += pow(-1, k) * next_el
    k += 1

variables = [num, total_size, my_sum, next_el, k]

print('-' * 100)
# print(my_sum)
show(*variables)
print(f'Total consumed memory : {total_size}')
print('-' * 100)


# --- с рекурсией --- #
# Total consumed memory : 23844

def func(a, cnt, stop):
    # print('>'*10, id(a))
    variables = [a, cnt, stop, func]
    print(f'\t {cnt} cycle')
    show(*variables)
    if cnt == stop:
        return a
    else:
        return a + func(-1 * a / 2, cnt + 1, stop)


total_size = 0
my_sum = func(1, 1, num)
variables = [num, total_size, my_sum]

# print(my_sum)
show(*variables)
print(f'Total consumed memory : {total_size}')
print('-' * 100)


# рекурсия  + словарь: заполняем словарь нужной нам последовательностью, а потом суммируем все его элеименты
# Total consumed memory : 28604
def sum_dic(num):
    my_dic = {1: 1}

    def _fil_dic(num):
        variables = [num, _fil_dic]
        show(*variables)
        if num in my_dic:
            return my_dic[num]
        else:
            my_dic[num] = (-1 / 2) * _fil_dic(num - 1)
            return my_dic[num]

    _fil_dic(num)
    variables = [my_dic, sum_dic]
    show(*variables)
    return sum(my_dic.values())


total_size = 0
my_sum = sum_dic(num)
variables = [num, total_size, my_sum]

# print(my_sum)
print(f'Total consumed memory : {total_size}')

# Вывод: Наиболее оптимальное решени с точки зрения потребления ОЗУ - решения с помощью цикла. Вся работа происходит
# с одними и теми же небольшим количеством переменных. Решение с помощью sum_dic- наименее эффектвно, т.к. на равне с
# рекурией, аналагочной в ф-ии func, введены дополнителные переменные, в том числе словарь. Рекурсия потребляет много
# ОЗУ т.к. при каждом рекурсивно вызове  необходимо инициализировать все перемнные снова.
