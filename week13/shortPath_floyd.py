'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
* 프로그램명 : shortPath_floyd.py
* 작성일 : 2021.12.02.Thur
* 프로그램 설명 : Floyd의 최단 경로 프로그램 작성하기
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


def shortest_path_floyd(vertex, adj):
    vsize = len(vertex)
    A = list(adj)
    for i in range(vsize):
        A[i] = list(adj[i])

    for k in range(vsize):
        for i in range(vsize):
            for j in range(vsize):
                if A[i][k] + A[k][j] < A[i][j]:
                    A[i][j] = A[i][k] + A[k][j]

        print("====", A)


vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
weight = [
    [0, 7, float('inf'), float('inf'), 3, 10, float('inf')],
    [7, 0, 4, 10, 2, 6, float('inf')],
    [float('inf'), 4, 0, 2, float('inf'), float('inf'), float('inf')],
    [float('inf'), 10, 2, 0, 11, 9, 4],
    [3, 2, float('inf'), 11, 0, 13, 5],
    [10, 6, float('inf'), 9, 13, 0, float('inf')],
    [float('inf'), float('inf'), float('inf'), 4, 5, float('inf'), 0]
]

print("Shortest Path By Floyd Algorithm")
shortest_path_floyd(vertex, weight)

