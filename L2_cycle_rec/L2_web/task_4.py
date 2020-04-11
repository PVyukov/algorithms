# НОД GCD
# 42 12     42  12
# 30 12
# 18 12
#  6 12      6  12
#  6  6      6   0

def gcd_1(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


def gcd_2(a, b):
    if b == 0:
        return a
    return gcd_2(b, a % b)


def gcd_3(a, b):
    while b != 0:
        a, b = b, a % b
        # temp = b
        # b = a % b
        # a = temp
    return a


print(gcd_1(426454562, 12))
print(gcd_2(426454562, 12))
print(gcd_3(426454562, 12))
