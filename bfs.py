from collections import deque

def bfs(graph, start):
    visited, q = set(), deque([start])
    while q:
        node = q.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            q.extend(graph[node])

graph = {
  'A': ['B','C'],
  'B': ['D','E'],
  'C': ['F'],
  'D': [], 'E': ['F'], 'F': []
}

bfs(graph, 'A')
