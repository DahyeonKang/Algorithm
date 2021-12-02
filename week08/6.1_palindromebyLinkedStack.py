'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
* 프로그램명 : 6.1_palindromebyLinkedStack.py
* 이름 : 강다현
* 작성일 : 2021.10.27.Wed
* 프로그램 설명 : 회문(palindrome)이란 앞뒤 어느 쪽에서 읽어도 같은 말 . 구. 문 등을
의미한다. 예를 들어 “eye”, “ madam, I’m Adam”, “race car” 등이다. 여기서 물론 
구두점이나 스페이스, 대소문자는 무시하여야 한다. 연결된 스택을 이용하여 회문인지 아닌지를 
결정하는 프로그램을 작성하라.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Node:
    def __init__(self, elem, link=None):
        self.data = elem  # 마지막으로 삽입된 항목
        self.link = link


class LinkedStack:
    def __init__(self):
        self.top = None  # top 생성 및 초기화

    def isEmpty(self):  # 공백상태 검사
        return self.top == None

    def clear(self):  # 스택 초기화
        self.top = None

    def push(self, item):  # 삽입
        n = Node(item, self.top)
        self.top = n

    def pop(self):  # 삭제
        if not self.isEmpty():
            n = self.top
            self.top = n.link
            return n.data

    def peek(self):  # 시작노드 데이터 반환
        if not self.isEmpty():
            return self.top.data

    def size(self):  # 스택의 항목 수 반환
        node = self.top
        count = 0
        while not node == None:
            node = node.link
            count += 1
        return count

    def display(self, msg='LinkedStack: '):
        print(msg, end='')
        node = self.top
        while not node == None:
            print(node.data, end=' ')
            node = node.link
        print()


def palindrome(string):
    stack = LinkedStack()
    string = string.lower()  # 문자가 아닌 것은 그대로 넣어진다.

    for ch in string:
        if ord(ch) < ord('a') or ord(ch) > ord('z'):  # 소문자가 아니면
            continue  # 건너뛰기
        stack.push(ch)  # 스택 리스트에 추가

    for ch in string:
        if ord(ch) < ord('a') or ord(ch) > ord('z'):
            continue
        if ch != stack.pop():
            print("회문이 아님")
            exit()
    print("회문이 맞음")


instr = input('문자열 입력: ')
palindrome(instr)