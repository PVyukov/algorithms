# 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится
# с клавиатуры.

# Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых
# трех уроков. Примечание. Идеальным решением будет:
# ● выбрать хорошую задачу, которую имеет смысл оценивать,
# ● написать 3 варианта кода (один у вас уже есть),
# ● проанализировать 3 варианта и выбрать оптимальный,
# ● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили
# замеры),
# ● написать общий вывод: какой из трёх вариантов лучше и почему. с циклом

import timeit
import cProfile


# с циклом
def sum_loop(num):
    my_sum = 1
    next_el = 1
    k = 1
    while k < num:
        next_el = next_el / 2
        my_sum += pow(-1, k) * next_el
        k += 1
    return my_sum


# print('*' * 50)   # Линейная зависимость
# print(timeit.timeit('sum_loop(5)', number=100, globals=globals()))    # 0.0001784240000000034
# print(timeit.timeit('sum_loop(10)', number=100, globals=globals()))   # 0.0003616959999999947
# print(timeit.timeit('sum_loop(15)', number=100, globals=globals()))   # 0.0006332119999999941
# print(timeit.timeit('sum_loop(20)', number=100, globals=globals()))   # 0.0009144229999999975
# print(timeit.timeit('sum_loop(200)', number=100, globals=globals()))  # 0.009336229000000001
# print(timeit.timeit('sum_loop(400)', number=100, globals=globals()))  # 0.021028332999999996

# cProfile.run('sum_loop(5)')   # 4    0.000    0.000    0.000    0.000 {built-in method builtins.pow}
# cProfile.run('sum_loop(10)')  # 9    0.000    0.000    0.000    0.000 {built-in method builtins.pow}
# cProfile.run('sum_loop(15)')  # 14    0.000    0.000    0.000    0.000 {built-in method builtins.pow}
# cProfile.run('sum_loop(20)')  # 19    0.000    0.000    0.000    0.000 {built-in method builtins.pow}
# cProfile.run('sum_loop(200)') # 199    0.000    0.000    0.000    0.000 {built-in method builtins.pow}
# cProfile.run('sum_loop(400)') # 399    0.000    0.000    0.000    0.000 {built-in method builtins.pow}



# с рекурсией
def sum_rec1(num):
    def _func(a, cnt, stop):
        if cnt == stop:
            return a
        else:
            return a + _func(-1 * a / 2, cnt + 1, stop)

    return _func(1, 1, num)

# print('*' * 50)   # Линейная зависимость, но время выполенеия в разу меньше, чем sum_loop
# print(timeit.timeit('sum_rec1(5)', number=100, globals=globals()))    # 0.00010424199999999745
# print(timeit.timeit('sum_rec1(10)', number=100, globals=globals()))   # 0.00017745399999999356
# print(timeit.timeit('sum_rec1(15)', number=100, globals=globals()))   # 0.0002613330000000025
# print(timeit.timeit('sum_rec1(20)', number=100, globals=globals()))   # 0.0003830300000000064
# print(timeit.timeit('sum_rec1(200)', number=100, globals=globals()))  # 0.0035893280000000027
# print(timeit.timeit('sum_rec1(400)', number=100, globals=globals()))  # 0.007688232000000003

# cProfile.run('sum_rec1(5)')   # 5/1    0.000    0.000    0.000    0.000 less_4_task_1.py:47(_func)
# cProfile.run('sum_rec1(10)')  # 10/1    0.000    0.000    0.000    0.000 less_4_task_1.py:47(_func)
# cProfile.run('sum_rec1(15)')  # 15/1    0.000    0.000    0.000    0.000 less_4_task_1.py:47(_func)
# cProfile.run('sum_rec1(20)')  # 20/1    0.000    0.000    0.000    0.000 less_4_task_1.py:47(_func)
# cProfile.run('sum_rec1(200)') # 200/1    0.000    0.000    0.000    0.000 less_4_task_1.py:47(_func)
# cProfile.run('sum_rec1(400)') # 400/1    0.000    0.000    0.000    0.000 less_4_task_1.py:47(_func)


# рекурсия  + словарь: заполняем словарь нужной нам последовательностью, а потом суммируем все его элеименты
def sum_dic(num):
    my_dic = {1: 1}

    def _fil_dic(num):
        if num in my_dic:
            return my_dic[num]
        else:
            my_dic[num] = (-1/2) * _fil_dic(num - 1)
            return my_dic[num]
    _fil_dic(num)
    return sum(my_dic.values())  # решил использовать встроенную ф-ю, т.к. и так понятно как ее реазизовать и
                                 # она не сильно влияет на оценку алгоритма; +O(N)


# print('*' * 50)   # Линейная зависимость, время выполенеия чуть больше чем у sum_rec1, связано с дополнительным
# перебором по словарю
# print(timeit.timeit('sum_dic(5)', number=100, globals=globals()))    # 0.00013624300000000117
# print(timeit.timeit('sum_dic(10)', number=100, globals=globals()))   # 0.00021333300000000305
# print(timeit.timeit('sum_dic(15)', number=100, globals=globals()))   # 0.0003427870000000041
# print(timeit.timeit('sum_dic(20)', number=100, globals=globals()))   # 0.00039418099999999345
# print(timeit.timeit('sum_dic(200)', number=100, globals=globals()))  # 0.0042763570000000015
# print(timeit.timeit('sum_dic(400)', number=100, globals=globals()))  # 0.008888229999999997
#
# cProfile.run('sum_dic(5)')   # 5/1    0.000    0.000    0.000    0.000 less_4_task_1.py:47(_func)
# cProfile.run('sum_dic(10)')  # 10/1    0.000    0.000    0.000    0.000 less_4_task_1.py:47(_func)
# cProfile.run('sum_dic(15)')  # 15/1    0.000    0.000    0.000    0.000 less_4_task_1.py:47(_func)
# cProfile.run('sum_dic(20)')  # 20/1    0.000    0.000    0.000    0.000 less_4_task_1.py:47(_func)
# cProfile.run('sum_dic(200)') # 200/1    0.000    0.000    0.000    0.000 less_4_task_1.py:47(_func)
# cProfile.run('sum_dic(400)') # 400/1    0.000    0.000    0.000    0.000 less_4_task_1.py:47(_func)


# ------------------------------------------------ #
# Выводы: Рекурсивная функция sum_rec1 окзалась самая эффетивная. Даже sum_dic, котрая использует дополнительный
# перебор по словарю, работает быстрее чем ф-я с циклом. Возможно, это связано с релизацией встроенной ф-ии pow(-1, k)
# или с тем, что в ф-ии sum_loop используется больше переменных.
# Все алгоритмы простые, т.к. cProfile.run во всех прогонах показывает 0.
