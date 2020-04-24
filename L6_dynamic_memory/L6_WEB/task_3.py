import sys
import ctypes
import struct

a = 42
b = a

print(id(a))
print(sys.getsizeof(a))
print(ctypes.string_at(id(a), sys.getsizeof(a)))
print(struct.unpack('HHLHHh', ctypes.string_at(id(a), sys.getsizeof(a))))
print(id(int))


a = 'Hello'

print(id(a))
print(sys.getsizeof(a))
print(ctypes.string_at(id(a), sys.getsizeof(a)))
print(struct.unpack('HHLHHHHHHHh' + 'c' * 6, ctypes.string_at(id(a), sys.getsizeof(a))))
print(id(str))
