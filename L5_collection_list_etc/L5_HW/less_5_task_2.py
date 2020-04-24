# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как
# коллекция, элементы которой — цифры числа. Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’,
# ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’,
# ‘E’].
from collections import deque

hex_decimal = {'0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9',
               'A': '10', 'B': '11', 'C': '12', 'D': '13', 'E': '14', 'F': '15'}


def hex_2_decimal(hex_list):
    decimal_list = []
    for i in hex_list:
        decimal_list.append(int(hex_decimal[i]))
    return decimal_list


def decimal_2_hex(decimal_list):
    hex_list = []
    for i in decimal_list:
        for my_hex, decimal in hex_decimal.items():
            if i == int(decimal):
                hex_list.append(my_hex)
    return hex_list


# создаем массивы
num1 = deque([i for i in input('Enter number 1-st: ')])
num2 = deque([i for i in input('Enter number 2-nd: ')])
sum_num = deque([])

# приводим массивы к одному размеру: набиваем меньший массив нулями
len_num1 = len(num1)
len_num2 = len(num2)
len_max = len_num2

while len_num1 > len_num2:
    len_max = len_num1
    len_num2 += 1
    num2.appendleft('0')
while len_num1 < len_num2:
    len_num1 += 1
    num1.appendleft('0')

# меняем порядок элементов и приводим каждый элемент массива к числу
num1.reverse()
num1 = hex_2_decimal(num1)
num2.reverse()
num2 = hex_2_decimal(num2)

# складываем числа
in_memory = 0
for i in range(len_max):
    my_sum = num1[i] + num2[i] + in_memory
    if my_sum // 16:
        in_memory = 1
    else:
        in_memory = 0
    sum_num.append(my_sum % 16)
if in_memory > 0:
    sum_num.append(in_memory)
# меняем порядок элементов и приводим каждый элемент массива к hex строке
sum_num.reverse()
sum_num = decimal_2_hex(sum_num)

print(''.join(sum_num))
