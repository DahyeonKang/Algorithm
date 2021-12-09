'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
* 프로그램명 : radix_sort.py
* 작성일 : 2021.12.09.Thur
* 프로그램 설명 : 기수(radix) 정렬 프로그램 작성하기, 시간복잡도는 O(dn)이다.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

from queue import Queue  # queue 클래스 사용
import random


def radix_sort(A):
    queues = []
    for i in range(BUCKETS):
        queues.append(Queue())

    n = len(A)
    factor = 1
    for d in range(DIGITS):
        for i in range(n):
            queues[(A[i]//factor) % 10].put(A[i])
        i = 0
        for b in range(BUCKETS):
            while not queues[b].empty():
                A[i] = queues[b].get()
                i += 1
        factor *= 10
        print("step", d + 1, A)


BUCKETS = 10
DIGITS = 4
data = []
for i in range(10):
    data.append(random.randint(1, 9999))
print("Original data :", data)
radix_sort(data)
print("Radix Sort :", data)
