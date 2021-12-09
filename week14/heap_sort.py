'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
* 프로그램명 : heap_sort.py
* 작성일 : 2021.12.09.Thur
* 프로그램 설명 : 힙 클래스를 이용한 정렬 프로그램 작성하기, 힙정렬의 시간복잡도는
O(nlogn)이다.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(__file__)))))

from week10.max_heap import MaxHeap


def heap_sort(data):
    heap = MaxHeap()				
    for n in data:
        heap.insert(n)
        
    for i in range(1, len(data) + 1):
        data[-i] = heap.delete()
    return data


data = [2, 4, 6, 8, 9, 7, 5, 3, 1]
print('original data: ', data)
print('Heap Sort data: ', heap_sort(data))
