class Node:
    def __init__(self, elem, link=None):
        self.data = elem
        self.link = link


class CircularLinkedQueue:
    def __init__(self):
        self.tail = None

    def isEmpty(self):  # 공백상태 검사
        return self.tail == None

    def clear(self):  # 큐 초기화
        self.tail = None

    def peek(self):
        if not self.isEmpty():
            return self.tail.link.data  # front 데이터 반환

    def enqueue(self, item):  # 삽입 연산
        node = Node(item, None)
        if self.isEmpty():  # 공백상태일 때
            node.link = node
            self.tail = node
        else:  # 공백상태가 아닐 때
            node.link = self.tail.link
            self.tail.link = node
            self.tail = node

    def dequeue(self):  # 삭제 연산
        if not self.isEmpty():  # 공백상태가 아닐 때
            data = self.tail.link.data
            if self.tail.link == self.tail:  # 하나의 항목 갖을 때
                self.tail = None
            else:  # 여러 개의 항목 갖을 때
                self.tail.link = self.tail.link.link
            return data

    def size(self):
        if self.isEmpty():  # 공백상태일 때
            return 0
        else:  # 공백상태가 아닐 때
            count = 1
            node = self.tail.link  # node는 front부터 출발
            while not node == self.tail:  # node가 rear가 아닌 동안
                node = node.link
                count += 1
            return count

    def display(self, msg='CircularLinkedQueue: '):
        print(msg, end='')
        if not self.isEmpty():
            node = self.tail.link
            while not node == self.tail:
                print(node.data, end=' ')
                node = node.link
            print(node.data, end=' ')
        print()


q = CircularLinkedQueue()  # 연결된 원형큐 객체 생성

for i in range(8): q.enqueue(i)
q.display()
for i in range(5): q.dequeue()
q.display()
for i in range(8, 14): q.enqueue(i)
q.display()