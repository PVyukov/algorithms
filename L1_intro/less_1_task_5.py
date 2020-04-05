# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят,
# и сколько между ними находится букв.

a1 = input("Enter first character: ")
a2 = input("Enter second character: ")

a1 = ord(a1)-96
a2 = ord(a2)-96
cnt = abs(a1-a2)

print(f"{a1}, {a2}, {cnt}")
