a = float(input('Ведите число а: '))
b = float(input('Ведите число b: '))
c = float(input('Ведите число c: '))

if a > b:
    if a > c:
        print(f'max={a}')
    else:
        print(f'max={c}')
else:
    if b > c:
        print(f'max={b}')
    else:
        print(f'max={c}')
