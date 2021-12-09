'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
* 프로그램명 : merge_sort.py
* 작성일 : 2021.12.09.Thur
* 프로그램 설명 : 분할 정복 방법을 이용한 병합 정렬(merge sort) 프로그램 작성하기, 
병합 정렬의시간복잡도는 O(nlogn)이다.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


def merge_sort(A, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(A, left, mid)
        merge_sort(A, mid + 1, right)
        merge(A, left, mid, right)


def merge(A, left, mid, right):
    global sorted
    k = left
    i = left
    j = mid + 1
    while i <= mid and j <= right:
        if A[i] <= A[j]:
            sorted[k] = A[i]
            i, k = i+1, k+1
        else:
            sorted[k] = A[j]
            j, k = j+1, k+1

    if i > mid:
        sorted[k:k+right-j+1] = A[j:right+1]
    else:
        sorted[k:k+mid-i+1] = A[i:mid+1]
    A[left:right+1] = sorted[left:right+1]


sorted = []
arr = [5, 3, 8, 4, 9, 1, 6, 2, 7]
sorted = [0] * len(arr)
merge_sort(arr, 0, len(arr) - 1)
print("Merge Sort :", arr)
