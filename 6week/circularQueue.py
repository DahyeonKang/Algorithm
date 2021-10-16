MAX_QSIZE = 10  # 원형 큐의 크기


class CircularQueue:
    def __init__(self):
        self.front = 0  # 큐의 front(전단) 위치
        self.rear = 0  # 큐의 rear(후단) 위치
        self.items = [None] * MAX_QSIZE  # 항목 저장용 리스트 [ㅜㅐ

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
            out = self.items[self.front+1:self.rear+1] + self.items[0:self.rear+1]  # 슬라이싱
        print("[f=%s, r=%d] ==> " % (self.front, self.rear), out)


q = CircularQueue()  # 원형큐 만들기. f=0, r=0 : 공백상태
for i in range(8):  # 0~7 삽입. f=0, r=8
    q.enqueue(i)
q.display()
for i in range(5):  # 4번까지 삭제. f=5, r=8
    q.dequeue()
q.display()
for i in range(8, 14):  # 8~13 삽입. f=5, r=4 : 포화상태
    q.enqueue(i)  # 참고로 배열[0]에도 값이 올 수 있다.
q.display()
