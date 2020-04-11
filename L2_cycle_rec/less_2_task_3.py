# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например, если
# введено число 3486, надо вывести 6843.

# с циклом

# a = int(input("Enter natural number: "))
# b = 0
#
# while a//10 != 0:
#     b = (b + a % 10)*10
#     a = a//10
# b = b + a % 10
#
#
# print (b)


# с рекурсией


def reverse(x, k):
    if x // 10 == 0:
        return x
    else:
        return 10 ** k * (x % 10) + reverse(x // 10, k - 1)


a = int(input("Enter natural number: "))
cnt = 1
tmp_a = a


while tmp_a // 10 != 0:
    cnt += 1
    tmp_a //= 10
b = reverse(a, cnt - 1)
print(f'Old number is {a}; new number is {b}')


