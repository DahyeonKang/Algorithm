'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
* 프로그램명 : sequential_search.py
* 작성일 : 2021.11.03.Wed
* 프로그램 설명 : 순차 탐색 프로그램 작성하기
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# A : 리스트
# key : 탐색 키
# low, high : 탐색 범위 인덱스가 low부터 high까지


def sequential_search(A, key, low, high):
    for i in range(low, high):  # low부터 high까지의 수
        if A[i] == key:  # 탐색 성공하면
            return i  # 해당 인덱스 반환
    return None  # 실패하면 None 반환


sample = [9, 5, 8, 3, 7]
print("리스트 : ", sample)
print("인덱스 값 : ", sequential_search(sample, 8, 0, 4))
