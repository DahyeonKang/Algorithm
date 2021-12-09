'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
* 프로그램명 : shell_sort.py
* 작성일 : 2021.12.09.Thur
* 프로그램 설명 : 리스트를 일정 간격(gap)의 부분 리스트로 나눠서 먼저 정렬하고 전체를 
정렬하는 셸 정렬 프로그램 작성하기, 셸정렬의 시간 복잡도는 최악은 O(n^2), 평균적으로는 
O(n^1.5)이다.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


def shell_sort(A):
    n = len(A)
    gap = n//2
    while gap > 0:
        if (gap % 2) == 0:
            gap += 1
        for i in range(gap):
            sortGapInsertion(A, i, n - 1, gap)
        print('     Gap=', gap, A)
        gap = gap//2


def sortGapInsertion(A, first, last, gap):
    for i in range(first+gap, last+1, gap):
        key = A[i]
        j = i - gap
        while j >= first and key < A[j]:
            A[j + gap] = A[j]
            j = j - gap
        A[j + gap] = key


data = [5, 3, 8, 4, 9, 1, 6, 2, 7]
print("Original  :", data)
shell_sort(data)
print("Shell     :", data)
