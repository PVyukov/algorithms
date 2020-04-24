my_list = [1]
my_list.extend([2, 3, 4])
my_list.insert(1, 5)
spam = my_list.pop()
eggs = my_list.pop()
my_list.remove(5)

allocated = 0
for new_size in range(1000):
    if allocated < new_size:
        new_allocated = (new_size >> 3) + (3 if new_size < 9 else 6)
        allocated = new_size + new_allocated
    print(f'{new_size}\t{allocated}')
