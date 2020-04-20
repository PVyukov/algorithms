from collections import defaultdict

a = defaultdict()
print(a)

# b = defaultdict(func)  # b = dict()

s = 'jdsvnqwibeoivnwoidvoeipvadsxvnaivnqwoivnqivbnqvniovwviebwdnveoi'
c = defaultdict(int)
for char in s:
    c[char] += 1
print(c)

list_1 = [('cat', 1), ('dog', 5), ('cat', 4), ('dog', 8), ('cat', 2), ('dog', 4), ('cat', 2), ('dog', 9)]
d = defaultdict(list)
for animal, distance in list_1:
    d[animal].append(distance)
print(d)

e = defaultdict(lambda: "i don't know")
e['cat'] = 'Boris'
print(e['cat'])
print(e['dog'])

