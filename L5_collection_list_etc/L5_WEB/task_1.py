from collections import Counter

a = Counter()
b = Counter('arbakadabra')
c = Counter({'cats': 10, 'dogs': 5})

print(a, b, c, sep='\n')

print(b['z'])
b['z'] = 3
print(b)

print(b.most_common(3))

d = Counter(a=4, b=-2, c=3)
e = Counter(a=2, b=3, c=4)
print(d, e, sep='\n')
print(d + e)
print(d - e)
print(d & e)
print(d | e)




