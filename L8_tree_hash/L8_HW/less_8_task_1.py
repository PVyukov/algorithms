# Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке. Примечание: в сумму не включаем пустую строку и
# строку целиком. Пример работы функции:
#
# func("papa")
# 6
# func("sova")
# 9
import hashlib

def cnt_unique(my_str):
    l_str = len(my_str)
    my_hash = set()
    print('*'*50)
    for i in range(l_str):
        for j in range(i+1, l_str+1):
#            print(my_str[i:j])
            hash_s = hashlib.sha512(my_str[i:j].encode('utf-8')).hexdigest()
            my_hash.add(hash_s)
    return len(my_hash) - 1


print(cnt_unique('sova'))
print(cnt_unique('a a'))