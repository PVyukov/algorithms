import hashlib

print(hash('dgbrfewrdb'))
print(hash('dgbrfewrdb'))
print(hash('dgbrfewrdb'))
print(hash('dgbrfewrdb'))
print(hash('dgbrfewrdb'))
print(hash('dgbrfewrdb'))

# 701191138
# 760292634

print(hashlib.sha1('Hello Worldж'.encode('utf-8')).hexdigest())

a = hashlib.sha1(b'Hello World').hexdigest()
b = hashlib.sha1(b'Hello World').hexdigest()
print(a == b)

print(hashlib.sha1('Привет, мир!'.encode('utf-8')).hexdigest())
print(hashlib.sha256('Привет, мир!'.encode('utf-8')).hexdigest())
print(hashlib.sha512('Привет, мир!'.encode('utf-8')).hexdigest())

s = input('Текст: ')
print(hashlib.sha512(s.encode('utf-8')).hexdigest())
