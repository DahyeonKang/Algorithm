'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
* 프로그램명 : spanning_tree.py
* 작성일 : 2021.11.24.Wed
* 프로그램 설명 : 신장 트리(spanning tree) 프로그램 작성하기
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import collections


def bfsST(graph, start):
    visit = set([start])
    queue = collections.deque([start])
    while queue:
        v = queue.popleft()
        nbr = graph[v] - visit
        # print('출력:', nbr)
        for u in list(nbr):
            print("(", v, ",", u, ")", end="")
            visit.add(u)
            queue.append(u)


graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D']),
         'C': set(['A', 'D', 'E']),
         'D': set(['B', 'C', 'F']),
         'E': set(['C', 'G', 'H']),
         'F': set(['D']),
         'G': set(['E', 'H']),
         'H': set(['E', 'G'])
         }

bfsST(graph, 'A')
