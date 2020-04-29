import hashlib


def rabin_karp(s, subs):
    len_sub = len(subs)
    hash_subs = hashlib.sha512(subs.encode('utf-8')).hexdigest()

    for i in range(len(s) - len_sub + 1):
        hash_s = hashlib.sha512(s[i:i + len_sub].encode('utf-8')).hexdigest()
        if hash_subs == hash_s:
            return i


s_1 = 'Hello world!'
s_2 = 'world'

print(rabin_karp(s_1, s_2))
