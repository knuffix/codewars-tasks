# https://www.codewars.com/kata/551f23362ff852e2ab000037/
def longest_slide_down(pyramid: list):
    graph = make_graph(pyramid)
    print(graph)
    paths = dfs(graph, '0.0')
    print(paths)
    for i in range(0, len(pyramid)):
        for j in range(0, len(pyramid)):
            pass
    return None


def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited


def make_graph(pyramid, graph={}, cur='0.0'):
    graph = graph
    zero = int(cur.split('.')[0])
    first = int(cur.split('.')[1])
    for i in range(0, len(pyramid)):
        if i <= zero:
            continue
        for j in range(0, len(pyramid)):
            if abs(i-zero) <= 1:
                if j == first or j - 1 == first:
                    if not f'{zero}.{first}' in graph.keys():
                        graph[f'{zero}.{first}'] = set(f'{i}.{j}')
                    else:
                        graph[f'{zero}.{first}'].add(f'{i}.{j}')
                    make_graph(pyramid, graph, f'{i}.{j}')
    return graph


data = [[3],
        [7, 4],
        [2, 4, 6],
        [8, 5, 9, 3],
        [1, 2, 3, 4, 5]]
print(longest_slide_down(data))
