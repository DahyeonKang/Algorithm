'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
* 프로그램명 : weight_sum.py
* 작성일 : 2021.12.02.Thur
* 프로그램 설명 : 인접행렬에서의 가중치의 합 계산하는 프로그램 작성하기
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


def weight_sum(vlist, W):
    sum = 0
    for i in range(len(vlist)):
        for j in range(i+1, len(vlist)):
            if W[i][j] != None:
                sum += W[i][j]
    return sum


vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
weight = [
    [None, 29, None, None, None, 10, None],
    [29, None, 16, None, None, None, 15],
    [None, 16, None, 12, None, None, None],
    [None, None, 12, None, 22, None, 18],
    [None, None, None, 22, None, 27, 25],
    [10, None, None, None, 27, None, None],
    [None, 15, None, 18, 25, None, None]
]
graph = (vertex, weight)

print('AM : weight sum = ', weight_sum(vertex, weight))
