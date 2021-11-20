'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
* 프로그램명 : binary_search.py
* 작성일 : 2021.11.18.Thur
* 프로그램 설명 : 이진탐색트리(binary search tree)의 탐색 연산과 맵
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

from TreeOrder import inorder, count_node


class BSTNode:  # 노드 구조 클래스
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


def search_bst(n, key):  # bst의 탐색연산 함수(순환 함수)
    if n == None:  # 탐색 실패
        return None
    elif key == n.key:  # 탐색 성공
        return n
    elif key < n.key:  # 왼쪽 서브트리 탐색
        return search_bst(n.left, key)
    else:  # 오른쪽 서브트리 탐색
        return search_bst(n.right, key)


def search_bst_iter(n, key):  # bst의 탐색연산 함수(반복 함수)
    while n != None:  # n이 None이 아닐 때까지 반복
        if key == n.key:  # 탐색 성공
            return n
        elif key < n.key:  # 왼쪽 서브트리로 이동
            n = n.left
        else:  # 오른쪽 서브트리로 이동
            n = n.right
    return None


def search_value_bst(n, value):  # bst의 탐색연산 함수 - 값을 이용한 탐색
    if n == None:
        return None
    elif value == n.value:
        return n
    res = search_value_bst(n.left, value)
    if res is not None:
        return res
    else:
        return search_value_bst(n.right, value)


def search_max_bst(n):  # 최대값의 노드 탐색
    while n != None and n.right != None:
        n = n.right
    return n


def search_min_bst(n):  # 최소값의 노드 탐색
    while n != None and n.left != None:
        n = n.left
    return n


def insert_bst(r, n):  # bst의 노드 삽입연산 - 순환구조 이용
    if n.key < r. key:
        if r.left is None:
            r.left = n
            return True
        else:
            return insert_bst(r.left, n)
    elif n.key > r.key:
        if r.right is None:
            r.right = n
            return True
        else:
            return insert_bst(r.right, n)
    else:
        return False


def delete_bst_case1(parent, node, root):  # 단말 노드의 삭제
    if parent is None:
        root = None
    else:
        if parent.left == node:
            parent.left = None
        else:
            parent.right = None
    return root


def delete_bst_case2(parent, node, root):  # 자식이 하나인 노드의 삭제
    if node.left is not None:
        child = node.left
    else:
        child = node.right

    if node == root:
        root = child
    else:
        if node is parent.left:
            parent.left = child
        else:
            parent.right = child
    return root


def delete_bst_case3(parent, node, root):  # 두 개의 사직을 모두 갖는 노드의 삭제
    succp = node
    succ = node.right
    while succ.left != None:
        succp = succ
        succ = succ.left

    if succp.left == succ:
        succp.left = succ.right
    else:
        succp.right = succ.right

    node.key = succ.key
    node.value = succ.value
    node = succ

    return root


def delete_bst(root, key):  # bst의 노드 삭제 연산 함수
    if root == None:
        return None
    parent = None
    node = root
    while node != None and node.key != key:
        parent = node
        if key < node.key:
            node = node.left
        else:
            node = node.right

    if node == None:
        return None
    if node.left == None and node.right == None:
        root = delete_bst_case1(parent, node, root)
    elif node.left == None or node.right == None:
        root = delete_bst_case2(parent, node, root)
    else:
        root = delete_bst_case3(parent, node, root)


class BSTMap:  # bst를 이용한 맵
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return self.root == None

    def clear(self):
        self.root = None

    def size(self):
        return count_node(self.root)

    def search(self, key):
        return search_bst(self.root, key)

    def searchValue(self, key):
        return search_value_bst(self.root, key)

    def findMax(self):
        return search_max_bst(self.root)

    def findMind(self):
        return search_min_bst(self.root)

    def insert(self, key, value=None):
        n = BSTNode(key, value)
        if self.isEmpty():
            self.root = n
        else:
            insert_bst(self.root, n)

    def delete(self, key):
        delete_bst(self.root, key)

    def display(self, msg='BSTMap:'):
        print(msg, end='')
        inorder(self.root)
        print()

if __name__ == '__main__':
    map = BSTMap()
    data = [35, 18, 7, 26, 12, 3, 68, 22, 30, 99]

    print('[삽입 연산] : ', data)
    for key in data:
        map.insert(key)
    map.display('[중위 순회] : ')

    if map.search(26) != None:
        print('[탐색 26 ] : 성공')
    else:
        print('[탐색 26 ] : 실패')
    if map.search(25) != None:
        print('[탐색 25 ] : 성공')
    else:
        print('[탐색 25 ] : 실패')

    map.delete(3)
    map.display('[3 삭제] : ')
    map.delete(68)
    map.display('[68 삭제] : ')
    map.delete(18)
    map.display('[18 삭제] : ')
    map.delete(35)
    map.display('[35 삭제] : ')
