'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
* 프로그램명 : graph_search.py
* 작성일 : 2021.11.24.Wed
* 프로그램 설명 : 그래프의 탐색을 깊이우선탐색과 너비우선탐색로 수행한 프로그램 작성하기
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import collections as cols  # 덱을 클래스로 이용하기 위해


def dfs(graph, start, visited=set()):  # 함수 - 깊이우선 탐색
    if start not in visited:
        visited.add(start)
        print(start, end=' ')
        nbr = graph[start] - visited  # v <= {인접정점} - {방문정점}
        for v in nbr:
            dfs(graph, v, visited)


def bfs(graph, start):  # 함수 - 너비우선 탐색
    visited = set([start])
    queue = cols.deque([start])  # 덱 객체 생성
    while queue:  # 공백이 아닐 때까지
        vertex = queue.popleft()  # 큐에서 하나의 vertex 빼냄
        print(vertex, end=' ')
        nbr = list(graph[vertex] - visited)
        for v in nbr:
            visited.add(v)
            queue.append(v)


mygraph = {'A': set(['B', 'C']),
           'B': set(['A', 'D']),
           'C': set(['A', 'D', 'E']),
           'D': set(['B', 'C', 'F']),
           'E': set(['C', 'G', 'H']),
           'F': set(['D']),
           'G': set(['E', 'H']),
           'H': set(['E', 'G'])}

print("깊이우선 탐색(DFS) : ", end=' ')
dfs(mygraph, "A")
print()
print("너비우선 탐색(BFS) : ", end=' ')
bfs(mygraph, "A")
