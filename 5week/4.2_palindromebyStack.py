'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
* 프로그램명 : 4.2_palindromebyStack.py
* 작성일 : 2021.10.06.Wed
* 프로그램 설명 : 회문(palindrome)이란 앞뒤 어느 쪽에서 읽어도 같은 말 . 구. 문 등을
의미한다. 예를 들어 “eye”, “ madam, I’m Adam”, “race car” 등이다. 여기서 물론 
구두점이나 스페이스, 대소문자는 무시하여야 한다. 스택을 이용하여 회문인지 아닌지를 
결정하는 프로그램을 스택으로 작성하라.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
from stackclass import Stack


## 첫번째 방법
def palindrome(string):
    s = Stack()
    prestr = list(string.lower())

    for i in prestr:
        if i.isalpha():
            s.push(i)
    prestr = list(''.join(char for char in prestr if char.isalnum()))

    for i in prestr:
        if s.pop() != i:
            return print("회문이 아님")
    print("회문이 맞음")


instr = input('문자열 입력: ')
palindrome(instr)

## 두번째 방법
# instr = input("문자열 입력: ")
# s = Stack()
#
# instr = instr.lower()
# for ch in instr:  # 소문자로 변환
#     if ord(ch) < ord('a') or ord(ch) > ord('z'):  # 소문자가 아니면
#         continue  # 건너뛰기
#     s.push(ch)  # 스택 리스트에 추가
#
# for ch in instr:
#     if ord(ch) < ord('a') or ord(ch) > ord('z'):
#         continue
#     if ch != s.pop():
#         print("회문이 아님")
#         exit()
# print("회문이 맞음")
