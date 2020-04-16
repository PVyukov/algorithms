import timeit
import cProfile

a = [i for i in range(1000)]

print(timeit.timeit('a = [i for i in range(10)]', number=100))
print(timeit.timeit('a = [i for i in range(100)]', number=100))
print(timeit.timeit('a = [i for i in range(1000)]', number=100))
print(timeit.timeit('a = [i for i in range(10000)]', number=100))
print(timeit.timeit('a = [i for i in range(100000)]', number=100))


def func(N):
    for i in range(N):
        for j in range(N):
            for k in range(N):
                a = 0


print('*' * 50)
print(timeit.timeit('func(2)', number=100, globals=globals()))
print(timeit.timeit('func(4)', number=100, globals=globals()))
print(timeit.timeit('func(6)', number=100, globals=globals()))
print(timeit.timeit('func(8)', number=100, globals=globals()))
print(timeit.timeit('func(10)', number=100, globals=globals()))


def my_len(a):
    return len(a)


def my_sum(a):
    s = 0
    for item in a:
        s += item
    return s


def main():
    array = [i for i in range(1000000)]
    len_ = my_len(array)
    sum_ = my_sum(array)

cProfile.run('main()')

