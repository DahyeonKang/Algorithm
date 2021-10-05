'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
* 프로그램명 : 3.7_comparison.py
* 작성일 : 2021.09.29.Wed
* 프로그램 설명 : 두개의 리스트를 입력 받아 두 리스트에 동일 항목이 있으면 True를 없으면
False를 반환하는 함수를 작성하라.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def comparison1(l1, l2):
    return bool(set(l1) & set(l2))

def comparison2(l1, l2):
    return set(l1).intersection(set(l2)) != set()

def comparison3(l1, l2):
    return len([i for i in l1 if i in l2]) != 0

list1 = list(map(int, input("공백을 기준으로 첫번째 리스트를 입력: ").split()))  # split()으로 공백 단위로 나누어서 리스트에 넣는다.
list2 = list(map(int, input("공백을 기준으로 두번째 리스트를 입력: ").split()))
print("첫번째 리스트:", list1)
print("두번째 리스트:", list2)
print(comparison1(list1, list2))
print(comparison2(list1, list2))
print(comparison3(list1, list2))