array = [8, 9, 4, 1, 0, 3, 7, 6, 2, 5]

n = 1
while n < len(array):
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            array[i], array[i + 1] = array[i + 1], array[i]
    n += 1
    print(array)

print(array)

