'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
* 프로그램명 : counting_sort.py
* 작성일 : 2021.12.09.Thur
* 프로그램 설명 : 분배 기반 정렬인 카운팅(counting) 정렬 프로그램 작성하기
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


import random


def counting_sort(A):
    output = [0] * MAX_VAL
    count = [0] * MAX_VAL

    for i in A:
        count[i] += 1

    for i in range(MAX_VAL):
        count[i] += count[i - 1]

    for i in range(len(A)):
        output[count[A[i]] - 1] = A[i]
        count[A[i]] -= 1

    for i in range(len(A)):
        A[i] = output[i]


MAX_VAL = 1000

org = [random.randint(0, MAX_VAL - 1) for _ in range(10)]
data = list(org)
print("Data : ", data)
counting_sort(data)
print("Counting Sort : ", data)
