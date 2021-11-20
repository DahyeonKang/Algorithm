'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
* 프로그램명 : AVL_tree.py
* 작성일 : 2021.11.18.Thur
* 프로그램 설명 : 이진탐색트리(binary search tree)의 탐색 연산과 맵
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

from binary_search import BSTMap, BSTNode
from TreeOrder import calc_height, levelorder, count_node, count_leaf


def rotateLL(A):
    B = A.left
    A.left = B.right
    B.right = A
    return B


def rotateRR(A):
    B = A.right
    A.right = B.left
    B.left = A
    return B


def rotateRL(A):
    B = A.right
    A.right = rotateLL(B)
    return rotateRR(A)


def rotateLR(A):
    B = A.left
    A.left = rotateRR(B)
    return rotateLL(A)


def calc_height_diff(n):
    if n == None:
        return 0
    return calc_height(n.left) - calc_height(n.right)


def reBalance(parent):
    hDiff = calc_height_diff(parent)

    if hDiff > 1:
        if calc_height_diff(parent.left) > 0:
            parent = rotateLL(parent)
        else:
            parent = rotateLR(parent)

    elif hDiff < -1:
        if calc_height_diff(parent.right) < 0:
            parent = rotateRR(parent)
        else:
            parent = rotateRL(parent)
    return parent


def insert_avl(parent, node):
    if node.key < parent.key:
        if parent.left != None:
            parent.left = insert_avl(parent.left, node)
        else:
            parent.left = node
        return reBalance(parent)

    elif node.key > parent.key:
        if parent.right != None:
            parent.right = insert_avl(parent.right, node)
        else:
            parent.right = node
        return reBalance(parent)
    else:
        print('중복된 키 에러')


class AVLMapo(BSTMap):
    def __init__(self):
        super().__init__()

    def insert(self, key, value=None):
        n = BSTNode(key, value)
        if self.isEmpty():
            self.root = n
        else:
            self.root = insert_avl(self.root, n)

    def display(self, msg='AVLMap : '):
        print(msg, end='')
        levelorder(self.root)
        print()


node = [7, 8, 9, 2, 1, 5, 3, 6, 4]
# node = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
map = AVLMapo()

for i in node:
    map.insert(i)
    map.display('AVL(%d): ' % i)

print(' 노드의 개수 = %d' % count_node(map.root))
print(' 단말의 개수 = %d' % count_leaf(map.root))
print(' 트리의 높이 = %d' % calc_height(map.root))
