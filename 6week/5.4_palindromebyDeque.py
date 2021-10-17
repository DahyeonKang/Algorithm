'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
* 프로그램명 : 5.4_palindromebyDeque.py
* 작성일 : 2021.10.17.Sun
* 프로그램 설명 : 회문(palindrome)이란 앞뒤 어느 쪽에서 읽어도 같은 말 . 구. 문 등을
의미한다. 예를 들어 “eye”, “ madam, I’m Adam”, “race car” 등이다. 여기서 물론 
구두점이나 스페이스, 대소문자는 무시하여야 한다. 덱을 이용하여 회문인지 아닌지를 
결정하는 프로그램을 덱으로 작성하라.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
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


def palindrome(s):
    dq = CircularDeque()  # 덱 객체 생성
    word = list(''.join(char.lower() for char in s if char.isalnum()))  # input 문자열을 조건에 맞게 처리해 리스트에 저장

    if dq.isEmpty():  # 덱이 비어있다면
        [dq.addRear(i.lower()) for i in filter(str.isalnum, s)]  # 덱에 조건에 맞게 후단부터 넣는다.

    for i in range(dq.size()//2):  # 덱과 word를 비교해서 회문 여부 판단
        if word[i] != dq.deleteRear():
            return print("회문이 아님")
    return print("회문이 맞음")


inputstr = input('문자열 입력: ')
palindrome(inputstr)