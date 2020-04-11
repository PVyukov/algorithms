# 7. Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
# 1+2+...+n = n(n+1)/2, где n — любое натуральное число.


def rec(a):
    if a == 1:
        return a
    else:
        return a + rec(a - 1)


num = int(input("Enter natural number: "))


res_right = num*(num+1)/2
res_left = rec(num)
if res_left == res_right:
    print('correct')
else:
    print('incorrect')