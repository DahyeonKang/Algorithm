'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
* 프로그램명 : connectedComponent.py
* 작성일 : 2021.11.24.Wed
* 프로그램 설명 : 그래프 연결 성분 검사 프로그램 작성하기
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


def find_connected_component(graph):
    visited = set()
    colorList = []

    for vtx in graph:
        if vtx not in visited:
            color = dfs_cc(graph, [], vtx, visited)
            colorList.append(color)

    print("그래프 연결성분 개수 = %d " % len(colorList))
    print(colorList)


def dfs_cc(graph, color, vertex, visited):
    if vertex not in visited:
        visited.add(vertex)
        color.append(vertex)
        nbr = graph[vertex] - visited
        for v in nbr:
            dfs_cc(graph, color, v, visited)
    return color


mygraph = {'A': set(['B', 'C']),
           'B': set(['A']),
           'C': set(['A']),
           'D': set(['E']),
           'E': set(['D']),
           }
print('find connected component :')
find_connected_component(mygraph)