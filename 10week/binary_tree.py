'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
* 프로그램명 : binary_tree.py
* 작성일 : 2021.11.10.Wed
* 프로그램 설명 : 이진트리의 연산 - 트리의 모든 노드를 방문하는 방법들을 각 함수로 
구현한 프로그램 작성하기
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# import sys, os
# sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
# from 6week import circularQueue.CircularQueue


MAX_QSIZE = 10  # 원형 큐의 크기


class CircularQueue:
    def __init__(self):
        self.front = 0  # 큐의 front(전단) 위치
        self.rear = 0  # 큐의 rear(후단) 위치
        self.items = [None] * MAX_QSIZE  # 항목 저장용 리스트

    def isEmpty(self):  # 공백상태
        return self.front == self.rear

    def isFull(self):  # 포화상태
        return self.front == (self.rear + 1) % MAX_QSIZE

    def clear(self):
        self.front = self.rear

    def enqueue(self, item):
        if not self.isFull():  # 포화상태가 아니면
            self.rear = (self.rear + 1) % MAX_QSIZE  # rear 회전
            self.items[self.rear] = item  # rear 위치에 삽입

    def dequeue(self):
        if not self.isEmpty():  # 공백상태가 아니면
            self.front = (self.front + 1) % MAX_QSIZE  # front 회전
            return self.items[self.front]  # front 위치의 항목 반환

    def peek(self):
        if not self.isEmpty():
            return self.items[(self.front + 1) % MAX_QSIZE]

    def size(self):
        return (self.rear - self.front + MAX_QSIZE) % MAX_QSIZE

    def display(self):
        out = []
        if self.front < self.rear:
            out = self.items[self.front+1:self.rear+1]  # 슬라이싱
        else:
            out = self.items[self.front+1:MAX_QSIZE] + self.items[0:self.rear+1]  # 슬라이싱
        print("[f=%s, r=%d] ==> " % (self.front, self.rear), out)


class TNode:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


def preorder(n):
    if n is not None:
        print(n.data, end=' ')
        preorder(n.left)
        preorder(n.right)


def inorder(n):
    if n is not None:
        inorder(n.left)
        print(n.data, end=' ')
        inorder(n.right)


def postorder(n):
    if n is not None:
        postorder(n.left)
        postorder(n.right)
        print(n.data, end=' ')


def levelorder(root):
    queue = CircularQueue()
    queue.enqueue(root)
    while not queue.isEmpty():
        n = queue.dequeue()
        if n is not None:
            print(n.data, end=' ')
            queue.enqueue(n.left)
            queue.enqueue(n.right)


def count_node(n):
    if n is None:
        return 0
    else:
        return 1 + count_node(n.left) + count_node(n.right)


def count_leaf(n):
    if n is None:
        return 0
    elif n.left is None and n.right is None:
        return 1
    else:
        return count_leaf(n.left) + count_leaf(n.right)


def calc_height(n):
    if n is None:
        return 0
    hLeft = calc_height(n.left)
    hRight = calc_height(n.right)

    if hLeft > hRight:
        return hLeft + 1
    else:
        return hRight + 1


d = TNode('D', None, None)
e = TNode('E', None, None)
b = TNode('B', d, e)
f = TNode('F', None, None)
c = TNode('C', f, None)
root = TNode('A', b, c)

print('\n   In-Order : ', end='')
inorder(root)
print('\n  Pre-Order : ', end='')
preorder(root)
print('\n Post-Order : ', end='')
postorder(root)
print('\nLevel-Order : ', end='')
levelorder(root)
print()

print("노드의 개수 = %d개" % count_node(root))
print("단말의 개수 = %d개" % count_leaf(root))
print("트리의 높이 = %d" % calc_height(root))
