'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
* 프로그램명 : bubble_sort.py
* 작성일 : 2021.11.03.Wed
* 프로그램 설명 : 버블 정렬 프로그램 작성하기
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

from printStep import printStep


def bubble_sort(A):
    n = len(A)
    for i in range(n-1, 0, -1):
        bChanged = False
        for j in range(i):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
                bChanged = True

        if not bChanged:
            break
        printStep(A, n - i)


data = [5, 3, 8, 4, 9, 1, 6, 2, 7]
print("Original : ", data)
bubble_sort(data)
print("Bubble : ", data)