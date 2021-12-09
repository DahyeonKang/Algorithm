'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
* 프로그램명 : quick_sort.py
* 작성일 : 2021.12.09.Thur
* 프로그램 설명 : 2개의 피벗을 사용하는 퀵 정렬 프로그램 작성하기
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


def dp_quick_sort(A, low, high):
    if low < high:
        lp, rp = partitionDP(A, low, high)
        dp_quick_sort(A, low, lp - 1)
        dp_quick_sort(A, lp + 1, rp - 1)
        dp_quick_sort(A, rp + 1, high)


def partitionDP(A, low, high):
    if A[low] > A[high]:
        A[low], A[high] = A[high], A[low]

    j = low + 1
    g = high - 1
    k = low + 1
    lpVal = A[low]
    rpVal = A[high]
    while k <= g:
        if A[k] < lpVal:
            A[k], A[j] = A[j], A[k]
            j += 1

        elif A[k] >= rpVal:
            while A[g] > rpVal and k < g:
                g -= 1
            A[k], A[g] = A[g], A[k]
            g -= 1

            if A[k] < lpVal:
                A[k], A[j] = A[j], A[k]
                j += 1
        k += 1

    j -= 1
    g += 1
    A[low], A[j] = A[j], A[low]
    A[high], A[g] = A[g], A[high]

    return j, g


arr = [5, 3, 8, 4, 9, 1, 6, 2, 7]
dp_quick_sort(arr, 0, len(arr) - 1)
print("Dual-pivot Quick Sort :", arr)
