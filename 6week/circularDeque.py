from circularQueueclass import CircularQueue


class CircularDeque(CircularQueue):  # CircularQueue 클래스 상속
    def __init__(self):
        super().__init__()  # 부모 클래스 생성자 호출

    # 재사용 멤버들 : isEmpty, isFull, size, clear, display

    # 인터페이스 변경 멤버들
    # 큐에 있는 기능이지만 이름만 바뀌기 때문에 부모 메소드 적절히 호출
    def addRear(self, item):
        self.enqueue(item)

    def deleteFront(self):
        return self.dequeue()

    def getFront(self):
        self.peek()

    # 추가 구현 메소드
    def addFront(self, item):  # 전단 삽입
        if not self.isFull():
            self.items[self.front] = item
            self.front = self.front - 1
            if self.front < 0:
                self.front = CircularQueue.MAX_QSIZE - 1

    def deleteRear(self):  # 후단 삭제
        if not self.isEmpty():
            item = self.items[self.rear]
            self.rear = self.rear - 1
            if self.rear < 0:
                self.rear = CircularQueue.MAX_QSIZE - 1
            return item

    def getRear(self):  # 후단 peek
        return self.items[self.rear]


dq = CircularDeque()

for i in range(9):
    if i % 2 == 0:
        dq.addRear(i)
    else:
        dq.addFront(i)

dq.display()

for i in range(2): dq.deleteFront()
for i in range(3): dq.deleteRear()
dq.display()
for i in range(9, 14): dq.addFront(i)
dq.display()
