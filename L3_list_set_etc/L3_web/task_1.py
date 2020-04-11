a = [1, 2, 3]
b = a
a = a + [4, 5]
a += [6, 7]
print(a, b, sep='\n')

a = [1, 2, 3]
b = a
a += [4, 5]  # a.extend([4, 5])
print(a, b, sep='\n')

# 2
print('*' * 50)
row = ['_'] * 3
print(row)
board = [row] * 3
print(board)
board[1][2] = 'X'
print(board)
board = [['_'] * 3 for _ in range(3)]
print(board)
board[1][2] = 'X'
print(board)
