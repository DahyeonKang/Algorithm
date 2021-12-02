'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
* 프로그램명 : graph_by_dict.py
* 작성일 : 2021.12.02.Thur
* 프로그램 설명 : 딕셔너리, 집합, 튜플, 리스트를 이용해서 그래프를 표현하고 이를 이용해 
인접 리스트의 가중치합 계산 프로그램과 모든 간선 출력 프로그램 작성하기
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


def weight_sum_dict(graph):
    sum = 0
    for v in graph:
        for e in graph[v]:
            sum += e[1]
    return sum // 2


def print_all_edges_dict(graph):
    for v in graph:
        for e in graph[v]:
            print("(%s,%s,%d)" % (v, e[0], e[1]), end=' ')


graph = {
    'A': set([('B', 29), ('F', 10)]),
    'B': set([('A', 29), ('C', 16), ('G', 15)]),
    'C': set([('B', 16), ('D', 12)]),
    'D': set([('C', 12), ('E', 22), ('G', 18)]),
    'E': set([('D', 22), ('F', 27), ('G', 25)]),
    'F': set([('A', 10), ('E', 27)]),
    'G': set([('B', 15), ('D', 18), ('E', 25)]),
}
print('AL : weight sum = ', weight_sum_dict(graph))
print_all_edges_dict(graph)
