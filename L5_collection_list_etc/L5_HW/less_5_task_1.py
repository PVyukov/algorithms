# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа) для
# каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести
# наименования предприятий, чья прибыль выше среднего и ниже среднего.
from collections import defaultdict
QUARTER = 4

num_company = int(input('Enter number of companies:'))
companies = defaultdict(list)
total_profit = 0


for company in range(1, num_company+1):
    sum_profit = 0
    name_company = input(f'Enter name of {company} company: ')
    for q in range(1, QUARTER+1):
        profit = float(input(f'Enter  {name_company} profit for the {q}  quarter: '))
        companies[name_company].append(profit)
        sum_profit += profit
    companies[name_company].append(sum_profit)
    total_profit += sum_profit

avg_profit = total_profit / num_company
print(f'Average profit is: {avg_profit}')
for n, profit in companies.items():
    profit = profit[4]
    if profit > avg_profit:
        print(f'+ {n}')
    else:
        print(f'- {n}')


