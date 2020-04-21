# Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать
# на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.

import timeit
import cProfile


# Первый — с помощью алгоритма «Решето Эратосфена».


def sieve(index):
    n = index ** 2 + 2  # "ошибка в безопасную сторону"; берем размерность списка со значительным запасом
    sieve = [i for i in range(n)]
    sieve[1] = 0
    for i in range(2, n):
        if sieve[i] != 0:
            j = i + i
            while j < n:
                sieve[j] = 0
                j += i

    #    print(sieve)
    res = [i for i in sieve if i != 0]
    return res[index - 1]


# Второй — без использования «Решета Эратосфена»


def prime(index):
    prime_mas = [2]
    number = prime_mas[0]

    while len(prime_mas) < index:
        number += 1
        for num in prime_mas:
            if number % num == 0:
                break
        else:
            prime_mas.append(number)
    return prime_mas[index - 1]


position = int(input("Enter position  of prime number:"))
print(sieve(position))
print(prime(position))

print("=" * 100)
# Заисимость явно не линейная
# print(timeit.timeit('sieve(5)', number=100, globals=globals()))   # 0.00047999899999999485
# print(timeit.timeit('sieve(10)', number=100, globals=globals()))  # 0.001851147999999997
# print(timeit.timeit('sieve(15)', number=100, globals=globals()))  # 0.0045182970000000044
# print(timeit.timeit('sieve(20)', number=100, globals=globals()))  # 0.008661805999999994
# print(timeit.timeit('sieve(30)', number=100, globals=globals()))  # 0.021804574000000007
# print(timeit.timeit('sieve(40)', number=100, globals=globals()))  # 0.045231934000000015
# print(timeit.timeit('sieve(200)', number=100, globals=globals())) # 1.274371964
# print(timeit.timeit('sieve(400)', number=100, globals=globals())) # 5.40157081
# Время выполения сильно заивсит от размерности решета «Решета Эратосфена»
# cProfile.run('sieve(5)')    # 1    0.000    0.000    0.000    0.000 less_4_task_2.py:12(<listcomp>)
# cProfile.run('sieve(10)')   # 1    0.000    0.000    0.000    0.000 less_4_task_2.py:12(<listcomp>))
# cProfile.run('sieve(15)')   # 1    0.000    0.000    0.000    0.000 less_4_task_2.py:12(<listcomp>)
# cProfile.run('sieve(20)')   # 1    0.000    0.000    0.000    0.000 less_4_task_2.py:12(<listcomp>)
# cProfile.run('sieve(30)')   # 1    0.000    0.000    0.000    0.000 less_4_task_2.py:12(<listcomp>)
# cProfile.run('sieve(40)')   # 1    0.000    0.000    0.000    0.000 less_4_task_2.py:12(<listcomp>)
# cProfile.run('sieve(200)')  # 1    0.001    0.001    0.001    0.001 less_4_task_2.py:12(<listcomp>)
# cProfile.run('sieve(400)')  # 1    0.007    0.007    0.007    0.007 less_4_task_2.py:12(<listcomp>)


# Заисимость практически линейная
# print(timeit.timeit('prime(5)', number=100, globals=globals()))   # 0.00019878799999999142
# print(timeit.timeit('prime(10)', number=100, globals=globals()))  # 0.0006104229999999988
# print(timeit.timeit('prime(15)', number=100, globals=globals()))  # 0.001186907000000001
# print(timeit.timeit('prime(20)', number=100, globals=globals()))  # 0.0021139360000000107
# print(timeit.timeit('prime(30)', number=100, globals=globals()))  # 0.003569933999999997
# print(timeit.timeit('prime(40)', number=100, globals=globals()))  # 0.007266897999999994
# print(timeit.timeit('prime(200)', number=100, globals=globals())) # 0.10239888100000001
# print(timeit.timeit('prime(400)', number=100, globals=globals())) # 0.3825085349999999
# Оптимизировать ничего, т.к. единственное на что тратиится время- это встроенная ф-я exec.
# cProfile.run('prime(5)')    # 1    0.000    0.000    0.000    0.001 {built-in method builtins.exec}
# cProfile.run('prime(10)')   # 1    0.000    0.000    0.000    0.001 {built-in method builtins.exec}
# cProfile.run('prime(15)')   # 1    0.000    0.000    0.000    0.001 {built-in method builtins.exec}
# cProfile.run('prime(20)')   # 1    0.000    0.000    0.000    0.001 {built-in method builtins.exec}
# cProfile.run('prime(30)')   # 1    0.000    0.000    0.000    0.001 {built-in method builtins.exec}
# cProfile.run('prime(40)')   # 1    0.000    0.000    0.000    0.001 {built-in method builtins.exec}
# cProfile.run('prime(200)')  # 1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
# cProfile.run('prime(400)')  # 1    0.000    0.000    0.004    0.004 {built-in method builtins.exec}


# Вывод: ф-я prime во много раз эффективней ф-ии sieve. Ф-я sieve может быть улучшена, если получится корретнее
# размерность изначального массива (решета)
