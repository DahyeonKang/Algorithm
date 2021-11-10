class CircularQueue:
    MAX_QSIZE = 10

    def __init__(self):
        self.front = 0  # 큐의 front(전단) 위치
        self.rear = 0  # 큐의 rear(후단) 위치
        self.items = [None] * CircularQueue.MAX_QSIZE  # 항목 저장용 리스트

    def isEmpty(self):  # 공백상태
        return self.front == self.rear

    def isFull(self):  # 포화상태
        return self.front == (self.rear + 1) % CircularQueue.MAX_QSIZE

    def clear(self):
        self.front = self.rear

    def enqueue(self, item):
        if not self.isFull():  # 포화상태가 아니면
            self.rear = (self.rear + 1) % CircularQueue.MAX_QSIZE  # rear 회전
            self.items[self.rear] = item  # rear 위치에 삽입

    def dequeue(self):
        if not self.isEmpty():  # 공백상태가 아니면
            self.front = (self.front + 1) % CircularQueue.MAX_QSIZE  # front 회전
            return self.items[self.front]  # front 위치의 항목 반환

    def peek(self):
        if not self.isEmpty():
            return self.items[(self.front + 1) % CircularQueue.MAX_QSIZE]

    def size(self):
        return (self.rear - self.front + CircularQueue.MAX_QSIZE) % CircularQueue.MAX_QSIZE

    def display(self):
        out = []
        if self.front < self.rear:
            out = self.items[self.front+1:self.rear+1]  # 슬라이싱
        else:
            out = self.items[self.front+1:CircularQueue.MAX_QSIZE] + self.items[0:self.rear+1]  # 슬라이싱
        print("[f=%s, r=%d] ==> " % (self.front, self.rear), out)

