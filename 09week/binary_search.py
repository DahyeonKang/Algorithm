'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
* 프로그램명 : binary_search.py
* 작성일 : 2021.11.03.Wed
* 프로그램 설명 : 이진 탐색 프로그램을 두 가지 버전으로 작성하기
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


def binary_search(A, key, low, high):
    if low <= high:  # 찾을 항목이 남으면
        middle = (low + high) // 2
        if key == A[middle]:
            return middle
        elif key < A[middle]:
            return binary_search(A, key, low, middle - 1)
        else:
            return binary_search(A, key, middle + 1, high)
    return None


def binary_search_iter(A, key, low, high):
    while low <= high:
        middle = (low + high) // 2
        if key == A[middle]:
            return middle
        elif key > A[middle]:
            low = middle + 1
        else:
            high = middle + 1
    return None


sample = [2, 6, 11, 13, 18, 20, 22, 27, 29, 30, 34, 38, 41, 42, 45, 47]
print("34의 인덱스 값 :", binary_search(sample, 34, 0, 15))
print("34의 인덱스 값 :", binary_search_iter(sample, 34, 0, 15))
print("20의 인덱스 값 :", binary_search(sample, 20, 0, 15))
