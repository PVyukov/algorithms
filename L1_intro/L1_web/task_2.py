a = float(input('Ведите число а: '))
b = float(input('Ведите число b: '))
c = float(input('Ведите число c: '))

m = a
if b > m:
    m = b
if c > m:
    m = c

print(f'{m=}')
