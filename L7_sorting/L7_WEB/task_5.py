import random

def quick_sort(arr, first, last):
    print(arr[first:last+1])
    if first >= last:
        return

    pivot = array[random.randint(first, last)]
    i, j = first, last

    while i <= j:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    quick_sort(arr, first, j)
    quick_sort(arr, i, last)


array = [8, 9, 4, 1, 0, 3, 7, 6, 2, 5]
quick_sort(array, first=0, last=len(array) - 1)
print(array)
