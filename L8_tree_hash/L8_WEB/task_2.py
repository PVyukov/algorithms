h_list = [None] * 26


def hash_1(value):
    index = ord(value[0]) - ord('a')
    h_list[index] = value
    print(h_list)


a = 'apple'
hash_1(a)
b = 'banana'
hash_1(b)
c = 'apricot'
hash_1(c)

print(9245 == 9*10**3 + 2*10**2 + 4*10**1 + 5*10**0)

def hash_2(value):
    letter = 26
    index = 0
    size = 10000
    for i, char in enumerate(value):
        index += (ord(char) - ord('a') + 1) * letter ** i
    return index % size

print(hash_2(a))
print(hash_2(b))
print(hash_2(c))
print(hash_2('jkebvdbeqiuvewiubsdiu ib dv'))