def shell_sort(arr):
    assert len(arr) < 4000, 'Массив слишком большой'

    def new_increment(arr):
        inc = [1, 4, 10, 23, 57, 132, 301, 701, 1750]
        while len(arr) <= inc[-1]:
            inc.pop()
        while len(inc) > 0:
            yield inc.pop()

    for increment in new_increment(arr):
        print(f'increment: {increment}')
        for i in range(increment, len(arr)):
            print(f'\ti: {i}')
            for j in range(i, increment - 1, -increment):
                print(f'\t\t\tj: {j}')
                print(f'\t\t\tarr[j - increment]: {arr[j - increment]}')
                print(f'\t\t\tarr[j]: {arr[j]}')
                if arr[j - increment] <= arr[j]:
                    break   # нужен break, т.к. если проход >1, то на предыдущих шагах мы уже все упорядочили
                arr[j], arr[j - increment] = arr[j - increment], arr[j]
                print(array)
        print(f'i arr {arr}')


array = [8, 9, 4, 1, 0, 3, 7, 6, 2, 5]
print(array)
shell_sort(array)
print(array)
