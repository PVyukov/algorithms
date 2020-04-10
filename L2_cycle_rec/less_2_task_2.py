# https://drive.google.com/file/d/1JAsbDcIg3NlrUlOKjt2I4ypCiwKEc2ld/view?usp=sharing

# 2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, в нем 3
# четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).


a_init = int(input("Enter natural number: "))
a = a_init
cnt_odd = 0
cnt_event = 0

while True:
    a1 = a % 10
    a = a // 10
    if a1 % 2 == 0:
        cnt_event += 1
    else:
        cnt_odd += 1
    if a != 0:
        continue
    break

print(f'In number {a_init}: {cnt_event} event digit(s) and {cnt_odd} odd digit(s)')