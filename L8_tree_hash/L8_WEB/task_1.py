from binarytree import tree, bst, Node


class MyNode:
    def __init__(self, value, left=None, right=None, data=None):
        self.value = value
        self.left = left
        self.right = right


a = tree(height=3, is_perfect=True)
print(a)
b = bst(height=3, is_perfect=True)
print(b)

root = MyNode(10)
root.left = MyNode(5)
root.right = MyNode(12)
root.left.right = MyNode(8)
root.right.right = MyNode('42')
print(root)

print('*' * 50)
bt = bst(height=5, is_perfect=False)
print(bt)
num = int(input('Что искать: '))


def search(bin_tree, number, path=''):
    if bin_tree.value == number:
        return f'Число {number} найдено по следующему пути:\nКорень{path}'
    if bin_tree.value > number and bin_tree.left is not None:
        return search(bin_tree.left, number, path=f'{path}\nШаг влево')
    if bin_tree.value < number and bin_tree.right is not None:
        return search(bin_tree.right, number, path=f'{path}\nШаг вправо')
    return f'Число {number} отсутствует в дереве'


print(search(bt, num))
