# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел. Количество вводимых
# чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.


attempts = int(input("Enter quantities of numbers: "))
digit = int(input("Enter digit which we will cont: "))
total = 0

for i in range(1, attempts+1):
    num = int(input(f"Enter {i} number: "))
    while True:
        modulo = num % 10
        num = num // 10
        if modulo == digit:
            total += 1
        if num > 0:
            continue
        break
print(f'Total is {total}')
