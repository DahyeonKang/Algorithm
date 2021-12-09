'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
* 프로그램명 : heapify_heap_sort.py
* 작성일 : 2021.12.09.Thur
* 프로그램 설명 : 제자리 정렬로 구현한 힙 클래스를 이용한 정렬 프로그램 작성하기
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)
    print("i=", 0, arr)
    for i in range(n//2, -1, -1):
        heapify(arr, n, i)
        print("i=", i, arr)
    print()

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
        print("i=", i, arr)


arr = [5, 3, 8, 4, 9, 1, 6, 2, 7]
heap_sort(arr)
print("HeapSort: ", arr)
