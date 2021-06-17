# # https://www.codewars.com/kata/551f23362ff852e2ab000037/
# from pprint import pprint


# def longest_slide_down(pyramid: list):
#     graph = make_graph(pyramid)
#     pprint(graph)
#     paths = dfs(graph, '[0, 0]')
#     print(paths)
#     for i in range(0, len(pyramid)):
#         for j in range(0, len(pyramid)):
#             pass
#     return None


# def dfs(graph, start, visited=None):
#     if visited is None:
#         visited = list()
#     visited.append(start)
#     print(start)
#     graph_visited = list()
#     if not str(start) in graph.keys():
#         return visited
#     for el in graph[str(start)]:
#         if not el in visited:
#             graph_visited.append(el)
#     for next in graph_visited:
#         dfs(graph, next, visited)
#     return visited


# def make_graph(pyramid, graph={}, cur=[0, 0]):
#     graph = graph
#     for i in range(0, len(pyramid)):
#         if i <= cur[0] or i - 1 > cur[0]:
#             continue
#         for j in range(0, len(pyramid)):
#             if abs(i-cur[0]) <= 1:
#                 if j == cur[1] or j - 1 == cur[1]:
#                     if not f'[{cur[0]}, {cur[1]}]' in graph.keys():
#                         graph[f'[{cur[0]}, {cur[1]}]'] = [[i,j]]
#                     else:
#                         if [i, j] not in graph[f'[{cur[0]}, {cur[1]}]']:
#                             graph[f'[{cur[0]}, {cur[1]}]'].append([i,j])
#                     make_graph(pyramid, graph, [i, j])
#     return graph


# data = [[3],
#         [7, 4],
#         [2, 4, 6],
#         [8, 5, 9, 3],
#         [1, 2, 3, 4, 5]]
# print(longest_slide_down(data))
import numpy as np


def longest_slide_down(pyramid):
    if len(pyramid) == 1:
        return pyramid[0][0]

    pyramid = np.array(pyramid)
    pyramid[-2] += np.maximum(pyramid[-1][:-1], pyramid[-1][1:])
    return longest_slide_down(pyramid[:-1])
