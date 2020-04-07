#  Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

number = int(input("Enter a three-digit number: "))

a1 = number // 100
number %= 100
a2 = number // 10
a3 = number % 10
sum_my = a1 + a2 + a3
prod_my = a1 * a2 * a3

print(f'Summary of digits is: {sum_my};\nProduction is: {prod_my} ')