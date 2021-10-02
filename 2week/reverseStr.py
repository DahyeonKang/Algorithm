'''
* 프로그램명 : reverseStr.py
* 작성일 : 2021.09.15
* 프로그램 설명 : 문자열의 내용을 역으로 바꾸는 순환함수 구현하기
'''

def reverse(str):
    n = len(str)
    if n == 1:
        return str
    return str[-1] + reverse(str[0:n-1])

str = 'When in Rome, do as the Romans do.'

print()
print("원문장: ", str)
print("역문장: ", reverse(str))
