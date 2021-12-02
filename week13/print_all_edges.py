'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
* 프로그램명 : print_all_edges.py
* 작성일 : 2021.12.02.Thur
* 프로그램 설명 : 인접행렬에서의 모든 간선을 출력하는 프로그램 작성하기
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def print_all_edges(vlist, W):
    for i in range(len(vlist)):
        for j in range(i+1, len(W[i])):
            if W[i][j] != None and W[i][j] != 0:
                print("(%s,%s,%d)" % (vlist[i], vlist[j], W[i][j]), end=' ')
    print()


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
print_all_edges(vertex, weight)
