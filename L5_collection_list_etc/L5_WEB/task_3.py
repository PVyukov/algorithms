from collections import deque

a = deque()
b = deque('abrakadabra')
c = deque([1, 2, 3, 4, 5])

print(a, b, c, sep='\n')

d = deque([1, 2, 3])
print(d)
d.append(4)
print(d)
d.appendleft(5)
print(d)
d.extend([6, 7])
print(d)
d.extendleft([8, 9])
print(d)
spam = d.pop()
print(d, spam)
eggs = d.popleft()  # для списка list d[1:] === d.pop(0)
print(d, eggs)

d.reverse()
print(d)
d.rotate(2)
print(d)
print(d[2])

