'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
* 프로그램명 : quick_sort.py
* 작성일 : 2021.12.09.Thur
* 프로그램 설명 : 분할 정복법을 사영한 퀵 정렬 프로그램 작성하기, 퀵 정렬의 시간복잡도는 
최선은 O(n log n), 최악은 O(n^2)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


def quick_sort(A, left, right):
    if left < right:
        q = partition(A, left, right)
        quick_sort(A, left, q - 1)
        quick_sort(A, q + 1, right)


def partition(A, left, right):
    low = left + 1
    high = right
    pivot = A[left]
    while low <= high:
        while low <= right and A[low] < pivot:
            low += 1
        while high >= left and A[high] > pivot:
            high -= 1

        if low < high:
            A[low], A[high] = A[high], A[low]

    A[left], A[high] = A[high], A[left]
    return high


arr = [5, 3, 8, 4, 9, 1, 6, 2, 7]
quick_sort(arr, 0, len(arr)-1)
print("Quick Sort: ", arr)
