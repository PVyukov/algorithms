import sys

a = 42.0
b = a
c = a
print(sys.getrefcount(a))

print(sys.getrefcount('eegrwegerg'))

print(sys.getsizeof(a))

def show(x):
    print(f'type={type(x)}, size={sys.getsizeof(x)}, obj={x}')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                show(key)
                show(value)
        elif not isinstance(x, str):
            for item in x:
                show(item)


show(a)

d = [i for i in range(10)]
show(d)
e = tuple(d)
show(e)
f = {str(i): i for i in range(10)}
show(f)
g = set(d)
show(g)

