'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
* 프로그램명 : MST_prim.py
* 작성일 : 2021.12.02.Thur
* 프로그램 설명 : Prim의 최소 비용 신장 트리(MST) 프로그램 작성하기
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


def getMinVertex(dist, selected):
    minv = 0
    mindist = float('inf')
    for v in range(len(dist)):
        if not selected[v] and dist[v] < mindist:
            mindist = dist[v]
            minv = v
    return minv


def MST_prim(veretx, adj):
    vsize = len(vertex)
    dist = [float('inf')] * vsize
    selected = [False] * vsize
    dist[0] = 0

    for i in range(vsize):
        u = getMinVertex(dist, selected)

        selected[u] = True
        print(vertex[u], end=' ')

        for v in range(vsize):
            if adj[u][v] != None:
                if selected[v] == False and adj[u][v] < dist[v]:
                    dist[v] = adj[u][v]



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
print("MST by Prim's Algorithm")
MST_prim(vertex, weight)
